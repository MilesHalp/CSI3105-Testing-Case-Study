import pytest
from frontend.Planner import Planner

@pytest.fixture
def planner():
    return Planner()

@pytest.mark.parametrize("inputs, expected",
    [
        (["1", "WrongName", "0"], "Requested employee does not exist"), # valid menu
        (["-1", "0"], "Please enter a number from 0 - 6"),              # < 0
        (["7", "0"], "Please enter a number from 0 - 6"),               # > 6
        (["abc", "0"], "Please enter a valid number from 0 - 6"),       # non-integer
    ],
    ids=[
        "EP-01",
        "EP-02",
        "EP-04",
        "EP-05",
    ]
)
def test_menu_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3", "10", "5", "10", "12", "0"], "Justin Gardener"),         # valid input
        (["3", "0", "5", "10", "12", "0"], "Month does not exist."),   # month < 1
        (["3", "13", "5", "10", "12", "0"], "Month does not exist."),  # month > 12
        (["3", "abc", "0"], "Please enter a valid number from 1 - 12"), # non-integer
    ],
    ids=[
        "EP-05",
        "EP-06",
        "EP-07",
        "EP-08",
    ]
)
def test_month_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["1", "Justin Gardener", "5", "all", "0"], "No Meetings booked on this date."),        # valid "all"
        (["1", "Justin Gardener", "5", "0", "0"], "Day does not exist."),                       # < 1
        (["1", "Justin Gardener", "5", "32", "0"], "Day does not exist."),                      # > 31
        (["1", "Justin Gardener", "5", "abc", "0"], "Please enter a valid number from 1 - 31"), # non-integer
    ],
    ids=[
        "EP-09",
        "EP-10",
        "EP-11",
        "EP-12",
    ]
)
def test_day_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3", "5", "5", "10", "12", "0"], "The people available"),  # valid

        (["3", "5", "5", "-1", "12", "0"], "Illegal hour."),   # start < 0
        (["3", "5", "5", "24", "12", "0"], "Illegal hour."),   # start > 23
        (["3", "5", "5", "abc", "0"], "Please enter a valid number from 1 - 24"), # start non-int

        (["3", "5", "5", "10", "-1", "0"], "Illegal hour."),   # end < 0
        (["3", "5", "5", "10", "24", "0"], "Illegal hour."),   # end > 23
        (["3", "5", "5", "10", "abc", "0"], "Please enter a valid number from 1 - 24"), # end non-int

        (["3", "5", "5", "10", "10", "0"], "Meeting end and start time are the same."),   # equal
        (["3", "5", "5", "15", "10", "0"], "Meeting ends before it starts."),   # start > end
    ],
    ids=[
        "EP-13",
        "EP-14",
        "EP-15",
        "EP-16",
        "EP-17",
        "EP-18",
        "EP-19",
        "EP-20",
        "EP-21",
    ]
)
def test_time_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize(
    "inputs, expected, exists",
    [
        (["6", "5", "5", "10", "12", "JO18.330", "Justin Gardener", "done", "description", "0"], "Meeting is now booked!", True),  # valid room
        (["6", "5", "5", "10", "12", "cancel", "0"], "Requested room does not exist", False),  # cancel
        (["6", "5", "5", "10", "12", "WrongRoom", "cancel", "0"], "Requested room does not exist", True), # invalid room
        (["6", "5", "5", "10", "12", "", "cancel", "0"], "Requested room does not exist", True),  # empty input
    ],
    ids=[
        "EP-22",
        "EP-23",
        "EP-24",
        "EP-25",
    ]
)
def test_room_selection(monkeypatch, capsys, planner, inputs, expected, exists):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()

    if exists:
        assert expected in captured.out
    else:
        assert expected not in captured.out


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["6", "5", "5", "10", "12", "JO18.330", "Justin Gardener", "done", "description", "0"], "Meeting is now booked!"),  # valid
        (["6", "5", "5", "10", "12", "JO18.330", "done", "description", "0"], "Meeting is now booked!"),  # invalid done figure out how to test
        (["6", "5", "5", "10", "12", "JO18.330", "WrongName", "done", "description", "0"], "Requested employee does not exist"),
        (["6", "5", "5", "10", "12", "JO18.330", "", "done", "description", "0"], "Requested employee does not exist"),
    ],
    ids=[
        "EP-26",
        "EP-27",
        "EP-28",
        "EP-29",
    ]
)
def test_attendee_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["6", "5", "10", "12", "Room1", "done", "Description", "0"], ""),  # valid
        (["6", "5", "10", "12", "Room1", "done", "", "0"], ""),         # empty
    ],
    ids=[
        "EP-30",
        "EP-31",
    ]
)
def test_description(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out