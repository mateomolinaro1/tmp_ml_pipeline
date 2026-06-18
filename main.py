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