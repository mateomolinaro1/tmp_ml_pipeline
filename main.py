from collections.abc import Callable

import pandas as pd
from pydantic import BaseModel, ConfigDict

from ml_pipeline.evaluation.ranking import information_coefficient
from ml_pipeline.evaluation.ranking import rank_information_coefficient
from ml_pipeline.evaluation.regression import mae
from ml_pipeline.evaluation.regression import mse
from ml_pipeline.evaluation.regression import r2
from ml_pipeline.evaluation.regression import rmse


class Scorer(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        arbitrary_types_allowed=True,
    )

    name: str

    fn: Callable[
        [pd.Series, pd.Series],
        float,
    ]

    greater_is_better: bool


SCORERS: dict[str, Scorer] = {
    "mse": Scorer(
        name="mse",
        fn=mse,
        greater_is_better=False,
    ),
    "rmse": Scorer(
        name="rmse",
        fn=rmse,
        greater_is_better=False,
    ),
    "mae": Scorer(
        name="mae",
        fn=mae,
        greater_is_better=False,
    ),
    "r2": Scorer(
        name="r2",
        fn=r2,
        greater_is_better=True,
    ),
    "ic": Scorer(
        name="ic",
        fn=information_coefficient,
        greater_is_better=True,
    ),
    "rank_ic": Scorer(
        name="rank_ic",
        fn=rank_information_coefficient,
        greater_is_better=True,
    ),
}


def get_scorer(
    name: str,
) -> Scorer:
    try:
        return SCORERS[name]
    except KeyError as exc:
        available = ", ".join(sorted(SCORERS))

        raise ValueError(
            f"Unknown scorer '{name}'. "
            f"Available scorers: {available}."
        ) from exc
        
        
import pytest

from ml_pipeline.evaluation.scoring import SCORERS
from ml_pipeline.evaluation.scoring import Scorer
from ml_pipeline.evaluation.scoring import get_scorer


def test_get_scorer_returns_scorer() -> None:
    scorer = get_scorer("rmse")

    assert isinstance(scorer, Scorer)
    assert scorer.name == "rmse"


def test_rmse_is_lower_is_better() -> None:
    scorer = get_scorer("rmse")

    assert scorer.greater_is_better is False


def test_r2_is_higher_is_better() -> None:
    scorer = get_scorer("r2")

    assert scorer.greater_is_better is True


def test_ic_is_higher_is_better() -> None:
    scorer = get_scorer("ic")

    assert scorer.greater_is_better is True


def test_all_registered_scorers_have_consistent_names() -> None:
    for name, scorer in SCORERS.items():
        assert scorer.name == name


def test_unknown_scorer_raises() -> None:
    with pytest.raises(ValueError):
        get_scorer("unknown")
        
from typing import Any

import pandas as pd
from pydantic import BaseModel, ConfigDict, Field


class TuningResult(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        arbitrary_types_allowed=True,
    )

    best_params: dict[str, Any] = Field(default_factory=dict)
    best_score: float
    scoring: str
    greater_is_better: bool
    results_frame: pd.DataFrame
    
from abc import ABC, abstractmethod

import pandas as pd

from ml_pipeline.core import PredictionTask
from ml_pipeline.tuning.result import TuningResult


class BaseTuner(ABC):
    @abstractmethod
    def fit(
        self,
        train_data: pd.DataFrame,
        validation_data: pd.DataFrame,
        task: PredictionTask,
        feature_columns: list[str],
    ) -> TuningResult:
        raise NotImplementedError
        
import math
from collections.abc import Callable
from itertools import product
from typing import Any

import pandas as pd
from pydantic import BaseModel, ConfigDict, Field

from ml_pipeline.core import PredictionTask
from ml_pipeline.evaluation.scoring import get_scorer
from ml_pipeline.models import BaseModelAdapter
from ml_pipeline.tuning.base import BaseTuner
from ml_pipeline.tuning.exceptions import TuningError
from ml_pipeline.tuning.result import TuningResult


class GridSearchTuner(BaseModel, BaseTuner):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        arbitrary_types_allowed=True,
    )

    model_factory: Callable[..., BaseModelAdapter]
    param_grid: dict[str, list[Any]] = Field(default_factory=dict)
    scoring: str = "rmse"

    def fit(
        self,
        train_data: pd.DataFrame,
        validation_data: pd.DataFrame,
        task: PredictionTask,
        feature_columns: list[str],
    ) -> TuningResult:
        scorer = get_scorer(self.scoring)

        records: list[dict[str, Any]] = []

        best_score: float | None = None
        best_params: dict[str, Any] | None = None

        for params in self._iter_param_combinations():
            model = self.model_factory(**params)

            fitted_model = model.fit(
                train_data=train_data,
                validation_data=validation_data,
                task=task,
                feature_columns=feature_columns,
            )

            predictions = fitted_model.predict(
                data=validation_data,
                task=task,
                feature_columns=feature_columns,
            )

            if "prediction" not in predictions.columns:
                raise TuningError("Model predictions must contain a 'prediction' column.")

            score = scorer.fn(
                validation_data[task.target_col],
                predictions["prediction"],
            )

            records.append(
                {
                    **params,
                    "score": score,
                    "scoring": self.scoring,
                    "greater_is_better": scorer.greater_is_better,
                }
            )

            if math.isnan(score):
                continue

            if best_score is None or self._is_better(
                score=score,
                best_score=best_score,
                greater_is_better=scorer.greater_is_better,
            ):
                best_score = score
                best_params = params

        if best_score is None or best_params is None:
            raise TuningError("No valid model score found during grid search.")

        return TuningResult(
            best_params=best_params,
            best_score=best_score,
            scoring=self.scoring,
            greater_is_better=scorer.greater_is_better,
            results_frame=pd.DataFrame.from_records(records),
        )

    def _iter_param_combinations(self) -> list[dict[str, Any]]:
        if not self.param_grid:
            return [{}]

        keys = list(self.param_grid)
        values = [self.param_grid[key] for key in keys]

        return [
            dict(zip(keys, combination, strict=True))
            for combination in product(*values)
        ]

    @staticmethod
    def _is_better(
        score: float,
        best_score: float,
        greater_is_better: bool,
    ) -> bool:
        if greater_is_better:
            return score > best_score

        return score < best_score

from ml_pipeline.tuning.base import BaseTuner as BaseTuner
from ml_pipeline.tuning.exceptions import TuningError as TuningError
from ml_pipeline.tuning.grid_search import GridSearchTuner as GridSearchTuner
from ml_pipeline.tuning.result import TuningResult as TuningResult

__all__ = [
    "BaseTuner",
    "GridSearchTuner",
    "TuningResult",
    "TuningError",
]

from abc import ABC, abstractmethod

import pandas as pd

from ml_pipeline.core import PredictionTask
from ml_pipeline.models import BaseModelAdapter
from ml_pipeline.tuning.result import TuningResult


class BaseTuner(ABC):
    @abstractmethod
    def fit(
        self,
        model: BaseModelAdapter,
        train_data: pd.DataFrame,
        validation_data: pd.DataFrame,
        task: PredictionTask,
        feature_columns: list[str],
    ) -> TuningResult:
        raise NotImplementedError
        
import math
from itertools import product
from typing import Any

import pandas as pd
from pydantic import BaseModel, ConfigDict, Field

from ml_pipeline.core import PredictionTask
from ml_pipeline.evaluation.scoring import get_scorer
from ml_pipeline.models import BaseModelAdapter
from ml_pipeline.tuning.base import BaseTuner
from ml_pipeline.tuning.exceptions import TuningError
from ml_pipeline.tuning.result import TuningResult


class GridSearchTuner(BaseModel, BaseTuner):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        arbitrary_types_allowed=True,
    )

    param_grid: dict[str, list[Any]] = Field(default_factory=dict)
    scoring: str = "rmse"

    def fit(
        self,
        model: BaseModelAdapter,
        train_data: pd.DataFrame,
        validation_data: pd.DataFrame,
        task: PredictionTask,
        feature_columns: list[str],
    ) -> TuningResult:
        scorer = get_scorer(self.scoring)

        records: list[dict[str, Any]] = []

        best_score: float | None = None
        best_params: dict[str, Any] | None = None

        for params in self._iter_param_combinations():
            candidate_model = model.model_copy(
                update=params,
            )

            fitted_model = candidate_model.fit(
                train_data=train_data,
                validation_data=validation_data,
                task=task,
                feature_columns=feature_columns,
            )

            predictions = fitted_model.predict(
                data=validation_data,
                task=task,
                feature_columns=feature_columns,
            )

            if "prediction" not in predictions.columns:
                raise TuningError(
                    "Model predictions must contain a 'prediction' column."
                )

            score = scorer.fn(
                validation_data[task.target_col],
                predictions["prediction"],
            )

            records.append(
                {
                    **params,
                    "score": score,
                    "scoring": self.scoring,
                    "greater_is_better": scorer.greater_is_better,
                }
            )

            if math.isnan(score):
                continue

            if best_score is None or self._is_better(
                score=score,
                best_score=best_score,
                greater_is_better=scorer.greater_is_better,
            ):
                best_score = score
                best_params = params

        if best_score is None or best_params is None:
            raise TuningError("No valid model score found during grid search.")

        return TuningResult(
            best_params=best_params,
            best_score=best_score,
            scoring=self.scoring,
            greater_is_better=scorer.greater_is_better,
            results_frame=pd.DataFrame.from_records(records),
        )

    def _iter_param_combinations(self) -> list[dict[str, Any]]:
        if not self.param_grid:
            return [{}]

        keys = list(self.param_grid)
        values = [self.param_grid[key] for key in keys]

        return [
            dict(zip(keys, combination, strict=True))
            for combination in product(*values)
        ]

    @staticmethod
    def _is_better(
        score: float,
        best_score: float,
        greater_is_better: bool,
    ) -> bool:
        if greater_is_better:
            return score > best_score

        return score < best_score
        
from typing import Any

import pandas as pd
import pytest

from ml_pipeline.core import PredictionTask, PredictionType, TaskType
from ml_pipeline.models import BaseModelAdapter, FittedModelAdapter
from ml_pipeline.tuning import GridSearchTuner, TuningError


class DummyFittedModel(FittedModelAdapter):
    def __init__(self, prediction_value: float) -> None:
        self.prediction_value = prediction_value

    def predict(
        self,
        data: pd.DataFrame,
        task: PredictionTask,
        feature_columns: list[str],
    ) -> pd.DataFrame:
        return pd.DataFrame(
            {
                "prediction": [self.prediction_value] * len(data),
            },
            index=data.index,
        )


class DummyModel(BaseModelAdapter):
    def __init__(
        self,
        alpha: float = 0.0,
        prediction_value: float | None = None,
    ) -> None:
        self.alpha = alpha
        self.prediction_value = prediction_value

    def fit(
        self,
        train_data: pd.DataFrame,
        task: PredictionTask,
        feature_columns: list[str],
        validation_data: pd.DataFrame | None = None,
    ) -> FittedModelAdapter:
        prediction_value = (
            self.alpha
            if self.prediction_value is None
            else self.prediction_value
        )

        return DummyFittedModel(
            prediction_value=prediction_value,
        )

    def with_params(
        self,
        params: dict[str, Any],
    ) -> BaseModelAdapter:
        return DummyModel(
            alpha=params.get("alpha", self.alpha),
            prediction_value=params.get("prediction_value", self.prediction_value),
        )


class DummyNaNModel(BaseModelAdapter):
    def fit(
        self,
        train_data: pd.DataFrame,
        task: PredictionTask,
        feature_columns: list[str],
        validation_data: pd.DataFrame | None = None,
    ) -> FittedModelAdapter:
        return DummyFittedModel(
            prediction_value=float("nan"),
        )

    def with_params(
        self,
        params: dict[str, Any],
    ) -> BaseModelAdapter:
        return self


def make_task() -> PredictionTask:
    return PredictionTask(
        target_col="target",
        date_col="date",
        entity_col="asset_id",
        task_type=TaskType.REGRESSION,
        prediction_type=PredictionType.SCORE,
    )


def make_train_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "date": pd.to_datetime(["2020-01-01", "2020-01-02"]),
            "asset_id": ["A", "B"],
            "x": [1.0, 2.0],
            "target": [0.0, 0.0],
        }
    )


def make_validation_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "date": pd.to_datetime(["2020-01-03", "2020-01-04"]),
            "asset_id": ["A", "B"],
            "x": [3.0, 4.0],
            "target": [1.0, 1.0],
        }
    )


def test_grid_search_explores_all_param_combinations() -> None:
    tuner = GridSearchTuner(
        param_grid={
            "alpha": [0.0, 1.0],
            "prediction_value": [0.5, 1.0],
        },
        scoring="rmse",
    )

    result = tuner.fit(
        model=DummyModel(),
        train_data=make_train_data(),
        validation_data=make_validation_data(),
        task=make_task(),
        feature_columns=["x"],
    )

    assert len(result.results_frame) == 4


def test_grid_search_selects_best_params_for_lower_is_better_metric() -> None:
    tuner = GridSearchTuner(
        param_grid={
            "prediction_value": [0.0, 1.0, 3.0],
        },
        scoring="rmse",
    )

    result = tuner.fit(
        model=DummyModel(),
        train_data=make_train_data(),
        validation_data=make_validation_data(),
        task=make_task(),
        feature_columns=["x"],
    )

    assert result.best_params == {
        "prediction_value": 1.0,
    }
    assert result.best_score == 0.0
    assert result.greater_is_better is False


def test_grid_search_selects_best_params_for_higher_is_better_metric() -> None:
    validation_data = pd.DataFrame(
        {
            "date": pd.to_datetime(["2020-01-03", "2020-01-04", "2020-01-05"]),
            "asset_id": ["A", "B", "C"],
            "x": [3.0, 4.0, 5.0],
            "target": [1.0, 2.0, 3.0],
        }
    )

    tuner = GridSearchTuner(
        param_grid={
            "prediction_value": [1.0],
        },
        scoring="ic",
    )

    result = tuner.fit(
        model=DummyModel(prediction_value=None),
        train_data=make_train_data(),
        validation_data=validation_data,
        task=make_task(),
        feature_columns=["x"],
    )

    assert result.best_params == {
        "prediction_value": 1.0,
    }
    assert result.greater_is_better is True


def test_grid_search_results_frame_contains_expected_columns() -> None:
    tuner = GridSearchTuner(
        param_grid={
            "prediction_value": [0.0, 1.0],
        },
        scoring="rmse",
    )

    result = tuner.fit(
        model=DummyModel(),
        train_data=make_train_data(),
        validation_data=make_validation_data(),
        task=make_task(),
        feature_columns=["x"],
    )

    assert set(result.results_frame.columns) == {
        "prediction_value",
        "score",
        "scoring",
        "greater_is_better",
    }


def test_grid_search_ignores_nan_scores() -> None:
    tuner = GridSearchTuner(
        param_grid={
            "prediction_value": [float("nan"), 1.0],
        },
        scoring="rmse",
    )

    result = tuner.fit(
        model=DummyModel(),
        train_data=make_train_data(),
        validation_data=make_validation_data(),
        task=make_task(),
        feature_columns=["x"],
    )

    assert result.best_params == {
        "prediction_value": 1.0,
    }


def test_grid_search_raises_when_all_scores_are_nan() -> None:
    tuner = GridSearchTuner(
        param_grid={
            "prediction_value": [float("nan")],
        },
        scoring="rmse",
    )

    with pytest.raises(TuningError):
        tuner.fit(
            model=DummyNaNModel(),
            train_data=make_train_data(),
            validation_data=make_validation_data(),
            task=make_task(),
            feature_columns=["x"],
        )


def test_grid_search_raises_when_prediction_column_is_missing() -> None:
    class BadFittedModel(FittedModelAdapter):
        def predict(
            self,
            data: pd.DataFrame,
            task: PredictionTask,
            feature_columns: list[str],
        ) -> pd.DataFrame:
            return pd.DataFrame(
                {
                    "bad_prediction": [0.0] * len(data),
                },
                index=data.index,
            )

    class BadModel(BaseModelAdapter):
        def fit(
            self,
            train_data: pd.DataFrame,
            task: PredictionTask,
            feature_columns: list[str],
            validation_data: pd.DataFrame | None = None,
        ) -> FittedModelAdapter:
            return BadFittedModel()

        def with_params(
            self,
            params: dict[str, Any],
        ) -> BaseModelAdapter:
            return self

    tuner = GridSearchTuner(
        param_grid={},
        scoring="rmse",
    )

    with pytest.raises(TuningError):
        tuner.fit(
            model=BadModel(),
            train_data=make_train_data(),
            validation_data=make_validation_data(),
            task=make_task(),
            feature_columns=["x"],
        )
    
def test_grid_search_selects_best_params_for_higher_is_better_metric() -> None:
    class FeatureBasedFittedModel(FittedModelAdapter):
        def predict(
            self,
            data: pd.DataFrame,
            task: PredictionTask,
            feature_columns: list[str],
        ) -> pd.DataFrame:
            return pd.DataFrame(
                {
                    "prediction": data["x"],
                },
                index=data.index,
            )

    class FeatureBasedModel(BaseModelAdapter):
        def fit(
            self,
            train_data: pd.DataFrame,
            task: PredictionTask,
            feature_columns: list[str],
            validation_data: pd.DataFrame | None = None,
        ) -> FittedModelAdapter:
            return FeatureBasedFittedModel()

        def with_params(
            self,
            params: dict[str, Any],
        ) -> BaseModelAdapter:
            return self

    validation_data = pd.DataFrame(
        {
            "date": pd.to_datetime(
                [
                    "2020-01-03",
                    "2020-01-04",
                    "2020-01-05",
                ]
            ),
            "asset_id": ["A", "B", "C"],
            "x": [1.0, 2.0, 3.0],
            "target": [1.0, 2.0, 3.0],
        }
    )

    tuner = GridSearchTuner(
        param_grid={},
        scoring="ic",
    )

    result = tuner.fit(
        model=FeatureBasedModel(),
        train_data=make_train_data(),
        validation_data=validation_data,
        task=make_task(),
        feature_columns=["x"],
    )

    assert result.best_params == {}
    assert result.best_score == pytest.approx(1.0)
    assert result.greater_is_better is True
    
import pandas as pd
from pydantic import BaseModel, ConfigDict

from ml_pipeline.core import PredictionTask
from ml_pipeline.features import FeatureSpec
from ml_pipeline.models import BaseModelAdapter, FittedModelAdapter
from ml_pipeline.preprocessing.pipeline import PreprocessingPipeline
from ml_pipeline.runner.context import RunnerContext
from ml_pipeline.runner.result import PredictionResult
from ml_pipeline.tuning import BaseTuner, TuningResult
from ml_pipeline.validation import BaseSplitter
from ml_pipeline.validation.splitters.split import Split


class Runner(BaseModel):
    model_config = ConfigDict(
        frozen=True,
        extra="forbid",
        arbitrary_types_allowed=True,
    )

    task: PredictionTask
    feature_spec: FeatureSpec

    splitter: BaseSplitter
    pipeline: PreprocessingPipeline
    model: BaseModelAdapter
    tuner: BaseTuner | None = None

    def predict_at(
        self,
        data: pd.DataFrame,
        prediction_date: pd.Timestamp,
    ) -> PredictionResult:
        split = self.splitter.get_split_for_date(
            data=data,
            task=self.task,
            prediction_date=prediction_date,
        )

        return self._predict_from_split(
            data=data,
            split=split,
        )

    def predict_range(
        self,
        data: pd.DataFrame,
    ) -> list[PredictionResult]:
        return [
            self._predict_from_split(
                data=data,
                split=split,
            )
            for split in self.splitter.split(
                data=data,
                task=self.task,
            )
        ]

    def _predict_from_split(
        self,
        data: pd.DataFrame,
        split: Split,
    ) -> PredictionResult:
        train_data = data.loc[split.train_indices].copy()

        validation_data: pd.DataFrame | None
        if split.validation_indices is not None:
            validation_data = data.loc[split.validation_indices].copy()
        else:
            validation_data = None

        prediction_data = data.loc[split.prediction_indices].copy()

        if self.tuner is None:
            fitted_pipeline = self.pipeline.fit(
                data=train_data,
                task=self.task,
            )

            train_processed = fitted_pipeline.transform(
                data=train_data,
                task=self.task,
            )

            if validation_data is not None:
                validation_processed = fitted_pipeline.transform(
                    data=validation_data,
                    task=self.task,
                )
            else:
                validation_processed = None

            prediction_processed = fitted_pipeline.transform(
                data=prediction_data,
                task=self.task,
            )

            model_feature_columns = self._model_feature_columns(
                output_columns=fitted_pipeline.output_columns,
            )

            fitted_model = self.model.fit(
                train_data=train_processed,
                validation_data=validation_processed,
                task=self.task,
                feature_columns=model_feature_columns,
            )

            tuning_result = None

        else:
            if validation_data is None:
                raise ValueError(
                    "Validation data is required when hyperparameter tuning is enabled."
                )

            fitted_pipeline_for_tuning = self.pipeline.fit(
                data=train_data,
                task=self.task,
            )

            train_processed_for_tuning = fitted_pipeline_for_tuning.transform(
                data=train_data,
                task=self.task,
            )

            validation_processed_for_tuning = fitted_pipeline_for_tuning.transform(
                data=validation_data,
                task=self.task,
            )

            model_feature_columns_for_tuning = self._model_feature_columns(
                output_columns=fitted_pipeline_for_tuning.output_columns,
            )

            tuning_result = self.tuner.fit(
                model=self.model,
                train_data=train_processed_for_tuning,
                validation_data=validation_processed_for_tuning,
                task=self.task,
                feature_columns=model_feature_columns_for_tuning,
            )

            refit_data = pd.concat(
                [
                    train_data,
                    validation_data,
                ],
                axis=0,
            )

            fitted_pipeline = self.pipeline.fit(
                data=refit_data,
                task=self.task,
            )

            refit_processed = fitted_pipeline.transform(
                data=refit_data,
                task=self.task,
            )

            prediction_processed = fitted_pipeline.transform(
                data=prediction_data,
                task=self.task,
            )

            model_feature_columns = self._model_feature_columns(
                output_columns=fitted_pipeline.output_columns,
            )

            best_model = self.model.with_params(
                params=tuning_result.best_params,
            )

            fitted_model = best_model.fit(
                train_data=refit_processed,
                validation_data=None,
                task=self.task,
                feature_columns=model_feature_columns,
            )

            train_processed = refit_processed.loc[train_data.index].copy()
            validation_processed = refit_processed.loc[validation_data.index].copy()

        predictions = fitted_model.predict(
            data=prediction_processed,
            task=self.task,
            feature_columns=model_feature_columns,
        )

        _ = RunnerContext(
            split=split,
            train_data=train_data,
            validation_data=validation_data,
            prediction_data=prediction_data,
            train_processed=train_processed,
            validation_processed=validation_processed,
            prediction_processed=prediction_processed,
        )

        return PredictionResult(
            predictions=predictions,
            actuals=prediction_data[self.task.target_col].copy(),
            prediction_data=prediction_data.copy(),
            prediction_date=split.prediction_date,
            train_size=len(train_data),
            validation_size=(
                len(validation_data)
                if validation_data is not None
                else 0
            ),
            prediction_size=len(prediction_data),
            train_start_date=split.train_start_date,
            train_end_date=split.train_end_date,
            validation_start_date=split.validation_start_date,
            validation_end_date=split.validation_end_date,
            prediction_start_date=split.prediction_start_date,
            prediction_end_date=split.prediction_end_date,
            features_used=self.feature_spec.active_feature_columns,
            output_columns=model_feature_columns,
            tuning_result=tuning_result,
        )

    def _model_feature_columns(
        self,
        output_columns: list[str],
    ) -> list[str]:
        reserved_columns = {
            self.task.date_col,
            self.task.target_col,
        }

        if self.task.entity_col is not None:
            reserved_columns.add(self.task.entity_col)

        return [
            column
            for column in output_columns
            if column not in reserved_columns
        ]
        
from typing import Any

import pandas as pd
import pytest

from ml_pipeline.core import PredictionTask, PredictionType, TaskType
from ml_pipeline.features import FeatureSpec
from ml_pipeline.models import BaseModelAdapter, FittedModelAdapter
from ml_pipeline.preprocessing.pipeline import PreprocessingPipeline
from ml_pipeline.runner import Runner
from ml_pipeline.tuning import GridSearchTuner
from ml_pipeline.validation import BaseSplitter
from ml_pipeline.validation.splitters.split import Split


class TunableFittedModel(FittedModelAdapter):
    def __init__(self, prediction_value: float) -> None:
        self.prediction_value = prediction_value

    def predict(
        self,
        data: pd.DataFrame,
        task: PredictionTask,
        feature_columns: list[str],
    ) -> pd.DataFrame:
        return pd.DataFrame(
            {"prediction": [self.prediction_value] * len(data)},
            index=data.index,
        )


class TunableDummyModel(BaseModelAdapter):
    def __init__(self, prediction_value: float = 0.0) -> None:
        self.prediction_value = prediction_value

    def fit(
        self,
        train_data: pd.DataFrame,
        task: PredictionTask,
        feature_columns: list[str],
        validation_data: pd.DataFrame | None = None,
    ) -> FittedModelAdapter:
        if validation_data is not None:
            return TunableFittedModel(
                prediction_value=self.prediction_value,
            )

        return TunableFittedModel(
            prediction_value=self.prediction_value + 10.0 * len(train_data),
        )

    def with_params(
        self,
        params: dict[str, Any],
    ) -> BaseModelAdapter:
        return TunableDummyModel(
            prediction_value=params.get(
                "prediction_value",
                self.prediction_value,
            )
        )


class ValidationSplitter(BaseSplitter):
    def get_split_for_date(
        self,
        data: pd.DataFrame,
        task: PredictionTask,
        prediction_date: str | pd.Timestamp,
    ) -> Split:
        return Split(
            prediction_date=pd.Timestamp(prediction_date),
            train_indices=pd.Index([0, 1]),
            validation_indices=pd.Index([2, 3]),
            prediction_indices=pd.Index([4]),
            train_start_date=pd.Timestamp("2020-01-01"),
            train_end_date=pd.Timestamp("2020-01-02"),
            validation_start_date=pd.Timestamp("2020-01-03"),
            validation_end_date=pd.Timestamp("2020-01-04"),
            prediction_start_date=pd.Timestamp("2020-01-05"),
            prediction_end_date=pd.Timestamp("2020-01-05"),
        )

    def split(
        self,
        data: pd.DataFrame,
        task: PredictionTask,
    ):
        yield self.get_split_for_date(
            data=data,
            task=task,
            prediction_date=pd.Timestamp("2020-01-05"),
        )


class NoValidationSplitter(ValidationSplitter):
    def get_split_for_date(
        self,
        data: pd.DataFrame,
        task: PredictionTask,
        prediction_date: str | pd.Timestamp,
    ) -> Split:
        split = super().get_split_for_date(
            data=data,
            task=task,
            prediction_date=prediction_date,
        )

        return Split(
            prediction_date=split.prediction_date,
            train_indices=split.train_indices,
            validation_indices=None,
            prediction_indices=split.prediction_indices,
            train_start_date=split.train_start_date,
            train_end_date=split.train_end_date,
            validation_start_date=None,
            validation_end_date=None,
            prediction_start_date=split.prediction_start_date,
            prediction_end_date=split.prediction_end_date,
        )


def make_task() -> PredictionTask:
    return PredictionTask(
        target_col="target",
        date_col="date",
        entity_col="asset_id",
        task_type=TaskType.REGRESSION,
        prediction_type=PredictionType.SCORE,
    )


def make_feature_spec() -> FeatureSpec:
    return FeatureSpec.from_groups(
        numeric=["x"],
    )


def make_data() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "date": pd.to_datetime(
                [
                    "2020-01-01",
                    "2020-01-02",
                    "2020-01-03",
                    "2020-01-04",
                    "2020-01-05",
                ]
            ),
            "asset_id": ["A"] * 5,
            "x": [1.0, 2.0, 3.0, 4.0, 5.0],
            "target": [0.0, 0.0, 1.0, 1.0, 99.0],
        }
    )


def make_tuner() -> GridSearchTuner:
    return GridSearchTuner(
        param_grid={
            "prediction_value": [0.0, 1.0, 3.0],
        },
        scoring="rmse",
    )


def make_runner(
    splitter: BaseSplitter | None = None,
) -> Runner:
    return Runner(
        task=make_task(),
        feature_spec=make_feature_spec(),
        splitter=splitter or ValidationSplitter(),
        pipeline=PreprocessingPipeline(),
        model=TunableDummyModel(),
        tuner=make_tuner(),
    )


def test_runner_returns_tuning_result() -> None:
    result = make_runner().predict_at(
        data=make_data(),
        prediction_date=pd.Timestamp("2020-01-05"),
    )

    assert result.tuning_result is not None
    assert result.tuning_result.best_params == {
        "prediction_value": 1.0,
    }
    assert result.tuning_result.best_score == 0.0


def test_runner_refits_best_model_on_train_plus_validation() -> None:
    result = make_runner().predict_at(
        data=make_data(),
        prediction_date=pd.Timestamp("2020-01-05"),
    )

    assert result.predictions["prediction"].iloc[0] == 41.0


def test_runner_requires_validation_data_when_tuning_is_enabled() -> None:
    runner = make_runner(
        splitter=NoValidationSplitter(),
    )

    with pytest.raises(ValueError):
        runner.predict_at(
            data=make_data(),
            prediction_date=pd.Timestamp("2020-01-05"),
        )