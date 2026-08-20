\section{Exact vs.\ Economic Decomposition of the Beta-Neutral Pure Alpha}

We consider a Pure Alpha portfolio with weights
\[
\mathbf{w}_t
=
\mathbf{w}_t^L
+
\mathbf{w}_t^S,
\]
where $\mathbf{w}_t^L$ and $\mathbf{w}_t^S$ denote the long and short
components, respectively.

\subsection{Exact beta-neutralization}

Let
\[
\boldsymbol{\beta}_t
=
\begin{pmatrix}
\beta_{1,t} \\
\vdots \\
\beta_{N,t}
\end{pmatrix}
\]
denote the vector of individual stock market betas.

The beta-neutralization procedure used in the portfolio construction is
\[
\boxed{
\mathbf{w}_t^{BN}
=
\mathbf{w}_t
-
\lambda_t \boldsymbol{\beta}_t
}
\]
where
\[
\boxed{
\lambda_t
=
\frac{
\boldsymbol{\beta}_t^\top \mathbf{w}_t
}{
\boldsymbol{\beta}_t^\top \boldsymbol{\beta}_t
}.
}
\]

Indeed,
\[
\begin{aligned}
\boldsymbol{\beta}_t^\top \mathbf{w}_t^{BN}
&=
\boldsymbol{\beta}_t^\top
\left(
\mathbf{w}_t
-
\lambda_t \boldsymbol{\beta}_t
\right)
\\
&=
\boldsymbol{\beta}_t^\top \mathbf{w}_t
-
\lambda_t
\boldsymbol{\beta}_t^\top \boldsymbol{\beta}_t
\\
&=0.
\end{aligned}
\]

Hence, the resulting portfolio is beta-neutral by construction.

\subsection{Exact long--short decomposition}

Since
\[
\mathbf{w}_t
=
\mathbf{w}_t^L
+
\mathbf{w}_t^S,
\]
we can define
\[
\lambda_t^L
=
\frac{
\boldsymbol{\beta}_t^\top \mathbf{w}_t^L
}{
\boldsymbol{\beta}_t^\top \boldsymbol{\beta}_t
}
\]
and
\[
\lambda_t^S
=
\frac{
\boldsymbol{\beta}_t^\top \mathbf{w}_t^S
}{
\boldsymbol{\beta}_t^\top \boldsymbol{\beta}_t
}.
\]

By linearity,
\[
\lambda_t
=
\lambda_t^L
+
\lambda_t^S.
\]

Therefore,
\[
\begin{aligned}
\mathbf{w}_t^{BN}
&=
\mathbf{w}_t^L
+
\mathbf{w}_t^S
-
(\lambda_t^L+\lambda_t^S)\boldsymbol{\beta}_t
\\
&=
\left(
\mathbf{w}_t^L-\lambda_t^L\boldsymbol{\beta}_t
\right)
+
\left(
\mathbf{w}_t^S-\lambda_t^S\boldsymbol{\beta}_t
\right).
\end{aligned}
\]

We may consequently define
\[
\boxed{
\mathbf{w}_t^{L,BN}
=
\mathbf{w}_t^L
-
\lambda_t^L\boldsymbol{\beta}_t
}
\]
and
\[
\boxed{
\mathbf{w}_t^{S,BN}
=
\mathbf{w}_t^S
-
\lambda_t^S\boldsymbol{\beta}_t.
}
\]

Thus,
\[
\boxed{
\mathbf{w}_t^{BN}
=
\mathbf{w}_t^{L,BN}
+
\mathbf{w}_t^{S,BN}.
}
\]

Let $\mathbf{r}_{t+1}$ denote the vector of individual stock returns over
period $t$ to $t+1$. The raw long-leg return is
\[
R_{t+1}^L
=
(\mathbf{w}_t^L)^\top\mathbf{r}_{t+1},
\]
while the raw short-leg return is
\[
R_{t+1}^S
=
(\mathbf{w}_t^S)^\top\mathbf{r}_{t+1}.
\]

Define the return of the beta-weighted portfolio as
\[
\boxed{
R_{t+1}^{\beta}
=
\boldsymbol{\beta}_t^\top\mathbf{r}_{t+1}
=
\sum_{i=1}^{N}\beta_{i,t}r_{i,t+1}.
}
\]

The exact return decomposition is therefore
\[
\boxed{
R_{t+1}^{L,BN}
=
R_{t+1}^L
-
\lambda_t^L R_{t+1}^{\beta}
}
\]
and
\[
\boxed{
R_{t+1}^{S,BN}
=
R_{t+1}^S
-
\lambda_t^S R_{t+1}^{\beta}.
}
\]

Hence,
\[
\boxed{
R_{t+1}^{PA,BN}
=
R_{t+1}^{L,BN}
+
R_{t+1}^{S,BN}.
}
\]

\subsection{Rewriting the exact decomposition using portfolio betas}

Define the beta contributions of the long and short legs as
\[
\beta_t^L
=
\boldsymbol{\beta}_t^\top\mathbf{w}_t^L
\]
and
\[
\beta_t^S
=
\boldsymbol{\beta}_t^\top\mathbf{w}_t^S.
\]

Since
\[
\lambda_t^L
=
\frac{
\beta_t^L
}{
\boldsymbol{\beta}_t^\top\boldsymbol{\beta}_t
},
\]
we have
\[
\lambda_t^L R_{t+1}^{\beta}
=
\beta_t^L
\frac{
\boldsymbol{\beta}_t^\top\mathbf{r}_{t+1}
}{
\boldsymbol{\beta}_t^\top\boldsymbol{\beta}_t
}.
\]

Define
\[
\boxed{
R_{t+1}^{\beta,*}
=
\frac{
\boldsymbol{\beta}_t^\top\mathbf{r}_{t+1}
}{
\boldsymbol{\beta}_t^\top\boldsymbol{\beta}_t
}.
}
\]

The exact long-leg decomposition can then be written as
\[
\boxed{
R_{t+1}^{L,BN}
=
R_{t+1}^L
-
\beta_t^L R_{t+1}^{\beta,*}.
}
\]

Similarly,
\[
\boxed{
R_{t+1}^{S,BN}
=
R_{t+1}^S
-
\beta_t^S R_{t+1}^{\beta,*}.
}
\]

\subsection{Economic decomposition}

A more intuitive economic decomposition consists of replacing the
beta-mimicking portfolio return $R_{t+1}^{\beta,*}$ by the actual market
benchmark return $R_{M,t+1}$.

The long leg is then approximated by
\[
\boxed{
R_{t+1}^{L,BN,\mathrm{econ}}
=
R_{t+1}^L
-
\beta_t^L R_{M,t+1}
}
\]
and the short leg by
\[
\boxed{
R_{t+1}^{S,BN,\mathrm{econ}}
=
R_{t+1}^S
-
\beta_t^S R_{M,t+1}.
}
\]

This decomposition is exact only if
\[
\boxed{
R_{t+1}^{\beta,*}
=
R_{M,t+1}.
}
\]

Otherwise, it constitutes an approximation of the beta-neutralization
actually implemented in the portfolio construction.

\subsection{Why the beta-mimicking portfolio approximates the market}

Consider the single-factor market model
\[
\mathbf{r}_{t+1}
=
\boldsymbol{\alpha}_t
+
\boldsymbol{\beta}_t R_{M,t+1}
+
\boldsymbol{\varepsilon}_{t+1}.
\]

Premultiplying by $\boldsymbol{\beta}_t^\top$ gives
\[
\boldsymbol{\beta}_t^\top\mathbf{r}_{t+1}
=
\boldsymbol{\beta}_t^\top\boldsymbol{\alpha}_t
+
\boldsymbol{\beta}_t^\top\boldsymbol{\beta}_t R_{M,t+1}
+
\boldsymbol{\beta}_t^\top\boldsymbol{\varepsilon}_{t+1}.
\]

Dividing by
$\boldsymbol{\beta}_t^\top\boldsymbol{\beta}_t$ yields
\[
\boxed{
R_{t+1}^{\beta,*}
=
R_{M,t+1}
+
\frac{
\boldsymbol{\beta}_t^\top\boldsymbol{\alpha}_t
}{
\boldsymbol{\beta}_t^\top\boldsymbol{\beta}_t
}
+
\frac{
\boldsymbol{\beta}_t^\top\boldsymbol{\varepsilon}_{t+1}
}{
\boldsymbol{\beta}_t^\top\boldsymbol{\beta}_t
}.
}
\]

If the beta-weighted alpha component is small,
\[
\frac{
\boldsymbol{\beta}_t^\top\boldsymbol{\alpha}_t
}{
\boldsymbol{\beta}_t^\top\boldsymbol{\beta}_t
}
\approx 0,
\]
and idiosyncratic risks are sufficiently diversified,
\[
\frac{
\boldsymbol{\beta}_t^\top\boldsymbol{\varepsilon}_{t+1}
}{
\boldsymbol{\beta}_t^\top\boldsymbol{\beta}_t
}
\approx 0,
\]
then
\[
\boxed{
R_{t+1}^{\beta,*}
\approx
R_{M,t+1}.
}
\]

Consequently,
\[
\boxed{
R_{t+1}^{L,BN}
\approx
R_{t+1}^L
-
\beta_t^L R_{M,t+1},
}
\]
and similarly,
\[
\boxed{
R_{t+1}^{S,BN}
\approx
R_{t+1}^S
-
\beta_t^S R_{M,t+1}.
}
\]

\subsection{Approximation error}

The difference between the exact and economic long-leg decompositions is
\[
\begin{aligned}
R_{t+1}^{L,BN}
-
R_{t+1}^{L,BN,\mathrm{econ}}
&=
-\beta_t^L
\left(
R_{t+1}^{\beta,*}
-
R_{M,t+1}
\right).
\end{aligned}
\]

Using the market model above,
\[
\boxed{
R_{t+1}^{L,BN}
-
R_{t+1}^{L,BN,\mathrm{econ}}
=
-\beta_t^L
\frac{
\boldsymbol{\beta}_t^\top
\left(
\boldsymbol{\alpha}_t
+
\boldsymbol{\varepsilon}_{t+1}
\right)
}{
\boldsymbol{\beta}_t^\top\boldsymbol{\beta}_t
}.
}
\]

Similarly, for the short leg,
\[
\boxed{
R_{t+1}^{S,BN}
-
R_{t+1}^{S,BN,\mathrm{econ}}
=
-\beta_t^S
\frac{
\boldsymbol{\beta}_t^\top
\left(
\boldsymbol{\alpha}_t
+
\boldsymbol{\varepsilon}_{t+1}
\right)
}{
\boldsymbol{\beta}_t^\top\boldsymbol{\beta}_t
}.
}
\]

Finally, defining
\[
\beta_t^{PA}
=
\beta_t^L+\beta_t^S,
\]
the total approximation error is
\[
\boxed{
R_{t+1}^{PA,BN}
-
R_{t+1}^{PA,BN,\mathrm{econ}}
=
-\beta_t^{PA}
\left(
R_{t+1}^{\beta,*}-R_{M,t+1}
\right).
}
\]

Equivalently,
\[
\boxed{
R_{t+1}^{PA,BN}
-
R_{t+1}^{PA,BN,\mathrm{econ}}
=
-\beta_t^{PA}
\frac{
\boldsymbol{\beta}_t^\top
\left(
\boldsymbol{\alpha}_t
+
\boldsymbol{\varepsilon}_{t+1}
\right)
}{
\boldsymbol{\beta}_t^\top\boldsymbol{\beta}_t
}.
}
\]

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
        
        
from pathlib import Path

import pandas as pd

from ml_pipeline.core import PredictionTask, PredictionType, TaskType
from ml_pipeline.evaluation import EvaluationEngine
from ml_pipeline.features import FeatureSpec
from ml_pipeline.models.sklearn import SklearnElasticNet
from ml_pipeline.preprocessing.missing import MissingValueEngine, MissingValueSpec
from ml_pipeline.preprocessing.pipeline import PreprocessingPipeline
from ml_pipeline.preprocessing.scaling import ScalingEngine, ScalingSpec
from ml_pipeline.runner import Runner
from ml_pipeline.tuning import GridSearchTuner
from ml_pipeline.validation import ExpandingWindowSplitter


DATA_PATH = Path("data/2026-05-MO.csv")


def load_macro_data() -> pd.DataFrame:
    raw = pd.read_csv(DATA_PATH)

    transform = raw.iloc[0, 1:].to_dict()
    transform = {key: value for key, value in transform.items()}

    data = raw.iloc[1:, :].copy()
    data.index = pd.to_datetime(data["sasdate"])
    data.index.name = "date"
    data = data.drop(columns=["sasdate"])

    for column in data.columns:
        data[column] = pd.to_numeric(data[column], errors="coerce")

    data["target"] = data["RPI"].shift(-1)
    data = data.dropna(subset=["target"])

    data = data.reset_index()

    return data


def test_macro_dataset_end_to_end() -> None:
    data = load_macro_data()

    feature_columns = [
        column
        for column in data.columns
        if column not in {"date", "target"}
    ]

    task = PredictionTask(
        target_col="target",
        date_col="date",
        entity_col=None,
        task_type=TaskType.REGRESSION,
        prediction_type=PredictionType.SCORE,
    )

    feature_spec = FeatureSpec.from_groups(
        numeric=feature_columns,
    )

    pipeline = PreprocessingPipeline(
        steps=[
            MissingValueEngine(
                spec=MissingValueSpec(
                    strategies={
                        column: "mean"
                        for column in feature_columns
                    }
                )
            ),
            ScalingEngine(
                spec=ScalingSpec(
                    strategies={
                        column: "standard"
                        for column in feature_columns
                    }
                )
            ),
        ]
    )

    runner = Runner(
        task=task,
        feature_spec=feature_spec,
        splitter=ExpandingWindowSplitter(
            min_train_window="20Y",
            validation_window="5Y",
            prediction_window="1M",
            step="12M",
        ),
        pipeline=pipeline,
        model=SklearnElasticNet(
            max_iter=5000,
        ),
        tuner=GridSearchTuner(
            param_grid={
                "alpha": [0.001, 0.01, 0.1],
                "l1_ratio": [0.2, 0.5, 0.8],
            },
            scoring="rmse",
        ),
    )

    results = runner.predict_range(data=data)

    assert len(results) > 0
    assert all(result.tuning_result is not None for result in results)
    assert all(len(result.predictions) > 0 for result in results)
    assert all(result.predictions["prediction"].notna().all() for result in results)

    evaluation = EvaluationEngine().evaluate(
        results=results,
        task=task,
    )

    assert not evaluation.evaluation_frame.empty
    assert not evaluation.date_metrics.empty

    assert "rmse" in evaluation.global_metrics
    assert "mae" in evaluation.global_metrics
    assert "ic_mean" in evaluation.global_metrics
    assert "rank_ic_mean" in evaluation.global_metrics
    
    from typing import Any

import pandas as pd
from pydantic import BaseModel, ConfigDict, Field

from ml_pipeline.preprocessing.base import FittablePreprocessor
from ml_pipeline.preprocessing.missing.standard.base import MissingValueImputer
from ml_pipeline.preprocessing.missing.standard.registry import (
    default_missing_value_registry,
)
from ml_pipeline.preprocessing.missing.standard.spec import MissingValueSpec


class FittedMissingValueEngine(BaseModel):
    model_config = ConfigDict(frozen=True, extra="forbid", arbitrary_types_allowed=True)

    spec: MissingValueSpec
    fitted_values: dict[str, Any]
    dropped_columns: list[str] = Field(default_factory=list)

    def fit(self, data: pd.DataFrame) -> "FittedMissingValueEngine":
        return self

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        output = data.copy()

        output = output.drop(
            columns=self.dropped_columns,
            errors="ignore",
        )

        for column, strategy in self.spec.strategies.items():
            if column in self.dropped_columns:
                continue

            if column not in output.columns:
                raise ValueError(f"Column '{column}' not found in data.")

            imputer = _resolve_imputer(strategy)
            fitted_value = self.fitted_values[column]

            output[column] = imputer.transform(output[column], fitted_value)

        return output


class MissingValueEngine(BaseModel, FittablePreprocessor[FittedMissingValueEngine]):
    model_config = ConfigDict(frozen=True, extra="forbid", arbitrary_types_allowed=True)

    spec: MissingValueSpec
    registry: dict[str, MissingValueImputer] = Field(
        default_factory=default_missing_value_registry
    )

    def fit(self, data: pd.DataFrame) -> FittedMissingValueEngine:
        fitted_values: dict[str, Any] = {}
        dropped_columns: list[str] = []

        for column, strategy in self.spec.strategies.items():
            if column not in data.columns:
                raise ValueError(f"Column '{column}' not found in data.")

            if data[column].isna().all():
                dropped_columns.append(column)
                continue

            imputer = self._resolve_imputer(strategy)
            fitted_values[column] = imputer.fit(data[column])

        return FittedMissingValueEngine(
            spec=self.spec,
            fitted_values=fitted_values,
            dropped_columns=dropped_columns,
        )

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        raise RuntimeError(
            "MissingValueEngine must be fitted before transform. "
            "Call fitted = engine.fit(train_data), then fitted.transform(data)."
        )

    def _resolve_imputer(
        self,
        strategy: str | MissingValueImputer,
    ) -> MissingValueImputer:
        if isinstance(strategy, str):
            return self.registry[strategy]

        return strategy


def _resolve_imputer(strategy: str | MissingValueImputer) -> MissingValueImputer:
    if isinstance(strategy, str):
        return default_missing_value_registry()[strategy]

    return strategy
    
    
import pandas as pd

from ml_pipeline.preprocessing.missing import MissingValueEngine, MissingValueSpec


def test_all_nan_column_is_dropped_after_fit_transform() -> None:
    data = pd.DataFrame(
        {
            "x1": [1.0, 2.0, 3.0],
            "x2": [None, None, None],
        }
    )

    engine = MissingValueEngine(
        spec=MissingValueSpec(
            strategies={
                "x1": "mean",
                "x2": "mean",
            }
        )
    )

    fitted = engine.fit(data)
    transformed = fitted.transform(data)

    assert fitted.dropped_columns == ["x2"]
    assert list(transformed.columns) == ["x1"]


def test_column_all_nan_in_train_is_dropped_even_if_present_in_prediction() -> None:
    train_data = pd.DataFrame(
        {
            "x1": [1.0, 2.0, 3.0],
            "x2": [None, None, None],
        }
    )

    prediction_data = pd.DataFrame(
        {
            "x1": [4.0, None],
            "x2": [10.0, 20.0],
        }
    )

    engine = MissingValueEngine(
        spec=MissingValueSpec(
            strategies={
                "x1": "mean",
                "x2": "mean",
            }
        )
    )

    fitted = engine.fit(train_data)
    transformed = fitted.transform(prediction_data)

    assert list(transformed.columns) == ["x1"]
    assert transformed["x1"].tolist() == [4.0, 2.0]


def test_non_all_nan_column_is_mean_imputed() -> None:
    data = pd.DataFrame(
        {
            "x1": [1.0, None, 3.0],
        }
    )

    engine = MissingValueEngine(
        spec=MissingValueSpec(
            strategies={
                "x1": "mean",
            }
        )
    )

    fitted = engine.fit(data)
    transformed = fitted.transform(data)

    assert fitted.dropped_columns == []
    assert transformed["x1"].tolist() == [1.0, 2.0, 3.0]
    
    import numpy as np
import pandas as pd

# ============================================================
# Inputs assumed available
# ============================================================
# w_before_bn : DataFrame [dates x assets]
#     Pure Alpha weights BEFORE beta-neutralization and BEFORE isovol
#
# rets : DataFrame [dates x assets]
#     Asset returns over period (t-1, t]
#
# betas : DataFrame [dates x assets]
#     Individual stock betas used by BetaNeutralization
#
# vol : DataFrame or Series [dates]
#     Ex-ante volatility used for isovol
#
# pa_bn_isovol : Series/DataFrame [dates]
#     Original strategy returns after BN + isovol, only for comparison
#
# vol_target = 0.05


# ============================================================
# 1. Align dates and assets
# ============================================================

common_dates = (
    w_before_bn.index
    .intersection(rets.index)
    .intersection(betas.index)
)

common_assets = (
    w_before_bn.columns
    .intersection(rets.columns)
    .intersection(betas.columns)
)

w = w_before_bn.reindex(
    index=common_dates,
    columns=common_assets
)

rets_aligned = rets.reindex(
    index=common_dates,
    columns=common_assets
)

betas_aligned = betas.reindex(
    index=common_dates,
    columns=common_assets
)

# Keep the same dates for vol
if isinstance(vol, pd.DataFrame):
    vol_aligned = vol.reindex(common_dates).iloc[:, 0]
else:
    vol_aligned = vol.reindex(common_dates)


# ============================================================
# 2. Split pre-BN portfolio into long and short legs
# ============================================================

w_lo = w.where(w > 0, 0.0)

w_so = w.where(w < 0, 0.0)


# ============================================================
# 3. Realized raw long / short returns
#
# R_t^L = w_{t-1}^{L,T} r_t
# R_t^S = w_{t-1}^{S,T} r_t
# ============================================================

w_lo_lag = w_lo.shift(1)
w_so_lag = w_so.shift(1)

ret_lo = (
    w_lo_lag
    .mul(rets_aligned)
    .sum(axis=1)
    .rename("ret_lo")
)

ret_so = (
    w_so_lag
    .mul(rets_aligned)
    .sum(axis=1)
    .rename("ret_so")
)


# ============================================================
# 4. Lag the beta vector
#
# beta_{t-1} is the vector used to construct the portfolio
# whose return is realized at t.
# ============================================================

betas_lag = betas_aligned.shift(1)


# ============================================================
# 5. Long / short beta contributions
#
# beta_{t-1}^L = beta_{t-1}' w_{t-1}^L
# beta_{t-1}^S = beta_{t-1}' w_{t-1}^S
# ============================================================

beta_lo = (
    w_lo_lag
    .mul(betas_lag)
    .sum(axis=1)
    .rename("beta_lo")
)

beta_so = (
    w_so_lag
    .mul(betas_lag)
    .sum(axis=1)
    .rename("beta_so")
)


# ============================================================
# 6. Exact beta-mimicking return
#
# R_t^{beta,*}
# =
# (beta_{t-1}' r_t)
# /
# (beta_{t-1}' beta_{t-1})
# ============================================================

beta_port_ret = (
    betas_lag
    .mul(rets_aligned)
    .sum(axis=1)
    .rename("beta_port_ret")
)

beta_norm_sq = (
    betas_lag
    .pow(2)
    .sum(axis=1)
    .rename("beta_norm_sq")
)

beta_mimicking_ret = (
    beta_port_ret / beta_norm_sq
).rename("beta_mimicking_ret")


# ============================================================
# 7. Exact beta-neutral long / short decomposition
#
# R_t^{L,BN}
# =
# R_t^{L,NBN}
# -
# beta_{t-1}^L * R_t^{beta,*}
#
# R_t^{S,BN}
# =
# R_t^{S,NBN}
# -
# beta_{t-1}^S * R_t^{beta,*}
# ============================================================

ret_lo_bn = (
    ret_lo
    - beta_lo * beta_mimicking_ret
).rename("ret_lo_bn")

ret_so_bn = (
    ret_so
    - beta_so * beta_mimicking_ret
).rename("ret_so_bn")


# ============================================================
# 8. Rebuild beta-neutral Pure Alpha before isovol
# ============================================================

pa_bn_rebuilt_pre_isovol = (
    ret_lo_bn + ret_so_bn
).rename("pa_bn_rebuilt_pre_isovol")


# ============================================================
# 9. Isovol scaler
#
# k_{t-1} = vol_target / vol_{t-1}
#
# IMPORTANT:
# If "vol" is already stored at date t as the scaler applicable
# to return t, remove the shift below.
# ============================================================

vol_target = 0.05

k = (
    vol_target / vol_aligned.shift(1)
).rename("k")


# ============================================================
# 10. Apply the SAME global isovol scaler to both legs
# ============================================================

lo_part = (
    k * ret_lo_bn
).rename("lo_part")

so_part = (
    k * ret_so_bn
).rename("so_part")

pa_bn_isovol_rebuilt = (
    lo_part + so_part
).rename("pa_bn_isovol_rebuilt")


# ============================================================
# 11. Collect everything
# ============================================================

df_decomp = pd.concat(
    [
        ret_lo,
        ret_so,
        beta_lo,
        beta_so,
        beta_port_ret,
        beta_norm_sq,
        beta_mimicking_ret,
        ret_lo_bn,
        ret_so_bn,
        pa_bn_rebuilt_pre_isovol,
        k,
        lo_part,
        so_part,
        pa_bn_isovol_rebuilt,
    ],
    axis=1
)

df_decomp = df_decomp.dropna()


# ============================================================
# 12. Optional comparison with original BN + isovol strategy
# ============================================================

if "pa_bn_isovol" in globals():

    original = pa_bn_isovol.squeeze().reindex(df_decomp.index)

    comparison = pd.concat(
        [
            original.rename("pa_bn_isovol_original"),
            df_decomp["pa_bn_isovol_rebuilt"],
        ],
        axis=1
    ).dropna()

    comparison["error"] = (
        comparison["pa_bn_isovol_original"]
        - comparison["pa_bn_isovol_rebuilt"]
    )

    print("Mean error:")
    print(comparison["error"].mean())

    print("\nMean absolute error:")
    print(comparison["error"].abs().mean())

    print("\nRMSE:")
    print(
        np.sqrt(
            np.mean(
                comparison["error"] ** 2
            )
        )
    )

    print("\nCorrelation original vs rebuilt:")
    print(
        comparison[
            [
                "pa_bn_isovol_original",
                "pa_bn_isovol_rebuilt"
            ]
        ].corr().iloc[0, 1]
    )


# ============================================================
# 13. Optional exact identity checks
# ============================================================

# beta of total pre-BN portfolio
beta_total = (
    w.shift(1)
    .mul(betas_lag)
    .sum(axis=1)
)

# Must equal beta_lo + beta_so
check_beta_split = (
    beta_total
    - (beta_lo + beta_so)
)

print("\nMax beta split error:")
print(check_beta_split.abs().max())


# Direct reconstruction from exact projection:
#
# w_BN,t-1
# =
# w_{t-1}
# -
# lambda_{t-1} beta_{t-1}
#
# lambda_{t-1}
# =
# (beta' w) / (beta' beta)

lambda_total = (
    beta_total / beta_norm_sq
)

w_bn_exact = (
    w.shift(1)
    - betas_lag.mul(lambda_total, axis=0)
)

ret_bn_direct = (
    w_bn_exact
    .mul(rets_aligned)
    .sum(axis=1)
    .rename("ret_bn_direct")
)

check_exact_reconstruction = (
    ret_bn_direct
    - pa_bn_rebuilt_pre_isovol
)

print("\nMax exact BN reconstruction error:")
print(check_exact_reconstruction.abs().max())

# Cumulative returns
cumprod = (1 + df_to_plot).cumprod()
cumprod = cumprod / cumprod.iloc[0, :]

fig, ax = plt.subplots(figsize=(9, 4))

# --------------------------------------------------
# Left axis: portfolio return series
# --------------------------------------------------
left_cols = [
    "pa_bn_isovol_rebuilt",
    "pa_bn_isovol",
    "lo_part",
    "so_part"
]

cumprod[left_cols].plot(ax=ax)

ax.set_xlabel("Date")
ax.set_ylabel("Cumulative growth")
ax.grid(alpha=0.3)

# --------------------------------------------------
# Right axis: LR_Sigma_Y_BN
# --------------------------------------------------
ax2 = ax.twinx()

cumprod["LR_Sigma_Y_BN"].plot(
    ax=ax2,
    linestyle="--",
    label="LR_Sigma_Y_BN"
)

ax2.set_ylabel("LR_Sigma_Y_BN cumulative growth")

# --------------------------------------------------
# Combined legend
# --------------------------------------------------
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()

ax.legend(
    lines1 + lines2,
    labels1 + labels2,
    loc="upper left"
)

# Remove the automatic legend from ax2
if ax2.get_legend() is not None:
    ax2.get_legend().remove()

ax.set_title(
    "Cumulative Performance of the decomposition of Pure Alpha BN"
)

cumprod_path = folder_path / Path("bn_merged_cumprod.png")
fig.savefig(cumprod_path, dpi=300, bbox_inches="tight")

plt.close(fig)