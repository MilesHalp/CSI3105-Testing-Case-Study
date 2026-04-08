import pytest
from frontend.Planner import Planner  # Import your Planner class

@pytest.fixture
def planner():
    """Fixture to create a fresh instance of Planner for each test."""
    return Planner()

