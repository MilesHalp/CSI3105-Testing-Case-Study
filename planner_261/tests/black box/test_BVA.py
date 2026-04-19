import pytest
from frontend.Planner import Planner  # Import your Planner class

@pytest.fixture
def planner():
    """Fixture to create a fresh instance of Planner for each test."""
    return Planner()

@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3", "0", "10", "10", "0"], ) # invalid, the 4 valid, then invalid
    ]
)

def test_day_bva(monkeypatch, capsys, planner, inputs, expected):
    pass

