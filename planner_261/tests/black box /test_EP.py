import pytest
from frontend.Planner import Planner  # Import your Planner class

@pytest.fixture
def planner():
    """Fixture to create a fresh instance of Planner for each test."""
    return Planner()


## Should test valid and invalid, weak robust
@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["1", "WrongName", "0"], "Requested employee does not exist"), # wrong name is to end menu function
        (["abc", "0"], "Please enter a valid number from 0 - 6"),
    ],
    ids=[
        "1", # valid
        "2", # not valid num
        "3", # not valid input
    ]
)
def test_menu_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)

    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    planner = Planner()  # Create an instance of Planner
    with pytest.raises(SystemExit):  # Expect the exit call to prevent test failure
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out

@pytest.mark.parametrize(
    "inputs, expected",
    [],
    ids=[]
)

def test_employee_name_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)


## test each menu function fully with weak robust. Don't think it would be strong as BVA will test that.



