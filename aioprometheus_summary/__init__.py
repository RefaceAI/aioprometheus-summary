from typing import Optional, Sequence, Tuple

import aioprometheus
from aioprometheus.mypy_types import LabelsType
from quantile_estimator import TimeWindowEstimator


class Summary(aioprometheus.Summary):
    # pairs of (quantile, allowed error)
    DEFAULT_INVARIANTS = ((0.50, 0.05), (0.90, 0.01), (0.99, 0.001))

    def __init__(
        self,
        name: str,
        doc: str,
        const_labels: Optional[LabelsType] = None,
        registry: Optional[aioprometheus.Registry] = None,
        invariants: Sequence[Tuple[float, float]] = DEFAULT_INVARIANTS,
        max_age_seconds: int = 10 * 60,
        age_buckets: int = 5,
    ) -> None:
        super().__init__(name, doc, const_labels=const_labels, registry=registry)
        self.invariants = invariants
        self.max_age_seconds = max_age_seconds
        self.age_buckets = age_buckets

    def add(self, labels, value):
        if not isinstance(value, (float, int)):
            raise TypeError("Summary only works with int or float")

        try:
            e = self.get_value(labels)
        except KeyError:
            e = TimeWindowEstimator(*self.invariants)
            self.set_value(labels, e)  # type: ignore

        e.observe(float(value))

    observe = add
