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
