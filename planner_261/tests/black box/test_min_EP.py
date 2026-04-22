import pytest
from frontend.Planner import Planner  # Import your Planner class

@pytest.fixture
def planner():
    """Fixture to create a fresh instance of Planner for each test."""
    return Planner()

@pytest.mark.parametrize("inputs, expected",
    [
        (["-1", "0"], "Please enter a number from 0 - 6"),        # < 0
        (["7", "0"], "Please enter a number from 0 - 6"),         # > 6
        (["abc", "0"], "Please enter a valid number from 0 - 6"), # non-integer
    ],
    ids=["EP-01", "EP-02", "EP-03"]
)
def test_menu_input_invalid(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize("inputs, expected",
    [
        (["3", "0", "5", "10", "12", "0"], "Month does not exist."),
        (["3", "13", "5", "10", "12", "0"], "Month does not exist."),
        (["3", "abc", "0"], "Please enter a valid number from 1 - 12"),
    ],
    ids=["EP-04", "EP-05", "EP-06"]
)
def test_month_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize("inputs, expected",
    [
        (["1", "Justin Gardener", "5", "0", "0"], "Day does not exist."),
        (["1", "Justin Gardener", "5", "32", "0"], "Day does not exist."),
        (["1", "Justin Gardener", "5", "abc", "0"], "Please enter a valid number from 1 - 31"),
    ],
    ids=["EP-07", "EP-08", "EP-09"]
)
def test_day_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize("inputs, expected",
    [
        # start invalid
        (["3", "5", "5", "-1", "12", "0"], "Illegal hour."),
        (["3", "5", "5", "24", "12", "0"], "Illegal hour."),
        (["3", "5", "5", "abc", "0"], "Please enter a valid number from 1 - 24"),

        # end invalid
        (["3", "5", "5", "10", "-1", "0"], "Illegal hour."),
        (["3", "5", "5", "10", "24", "0"], "Illegal hour."),
        (["3", "5", "5", "10", "abc", "0"], "Please enter a valid number from 1 - 24"),

        # logic
        (["3", "5", "5", "15", "10", "0"], "Meeting ends before it starts."),
    ],
    ids=[
        "EP-10",
        "EP-11",
        "EP-12",
        "EP-13",
        "EP-14",
        "EP-15",
        "EP-16",
    ]
)
def test_time_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize("inputs, expected",
    [
        (["6", "5", "5", "10", "12", "WrongRoom", "cancel", "0"], "Requested room does not exist"),
        (["6", "5", "5", "10", "12", "", "cancel", "0"], "Requested room does not exist"),
    ],
    ids=["EP-17", "EP-18"]
)
def test_room_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize("inputs, expected",
    [
        (["6", "5", "5", "10", "12", "JO18.330", "WrongName", "done", "description", "0"], "Requested employee does not exist"),

        (["6", "5", "5", "10", "12", "JO18.330", "", "done", "description", "0"], "Requested employee does not exist"),
    ],
    ids=["EP-19", "EP-20"]
)
def test_attendee_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out