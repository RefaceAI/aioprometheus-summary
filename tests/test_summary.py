import random

import pytest
from aioprometheus import Registry

from aioprometheus_summary import Summary


@pytest.fixture()
def registry():
    return Registry()


@pytest.fixture()
def summary(registry):
    return Summary("test", "test", registry=registry)


@pytest.mark.parametrize("num_observations", [1, 10, 100, 1000, 10000, 100000])
def test_random_observations(num_observations, summary):
    labels = {"key": "value"}
    sum_observations = 0
    for _ in range(num_observations):
        value = random.randint(1, 1000) / 100
        summary.observe(labels, value)
        sum_observations += value

    metric_value = summary.get(labels)
    assert metric_value["count"] == num_observations
    assert metric_value["sum"] == sum_observations
    assert metric_value[0.5] <= metric_value[0.9] <= metric_value[0.99]
