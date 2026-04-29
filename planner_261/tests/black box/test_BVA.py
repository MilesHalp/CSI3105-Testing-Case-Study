import pytest
from frontend.Planner import Planner  # Import your Planner class

@pytest.fixture
def planner():
    return Planner()

# day
@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3", "5", "0", "10", "12", "0"], "Day does not exist."),  # month > 12
        (["3", "5", "1", "10", "12", "0"], "Justin Gardener"),  # month > 12
        (["3", "5", "2", "10", "12", "0"], "Justin Gardener"),  # month > 12

        (["3", "5", "30", "10", "12", "0"], "Justin Gardener"),  # month > 12
        (["3", "5", "31", "10", "12", "0"], "Justin Gardener"),  # month > 12
        (["3", "5", "32", "10", "12", "0"], "Day does not exist."),  # month > 12
    ],
    ids=[
        "BVA-01",
        "BVA-02",
        "BVA-03",

        "BVA-04",
        "BVA-05",
        "BVA-06",
    ]
)
def test_5_day_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3", "2", "0", "10", "12", "0"], "Day does not exist."),  # month > 12
        (["3", "2", "1", "10", "12", "0"], "Justin Gardener"),  # month > 12
        (["3", "2", "2", "10", "12", "0"], "Justin Gardener"),  # month > 12

        (["3", "2", "27", "10", "12", "0"], "Justin Gardener"),  # month > 12
        (["3", "2", "28", "10", "12", "0"], "Justin Gardener"),  # month > 12
        (["3", "2", "29", "10", "12", "0"], "Day does not exist."),  # month > 12
    ],
    ids=[
        "BVA-07",
        "BVA-08",
        "BVA-09",

        "BVA-10",
        "BVA-11",
        "BVA-12",
    ]
)
def test_2_day_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3", "4", "0", "10", "12", "0"], "Day does not exist."),  # month > 12
        (["3", "4", "1", "10", "12", "0"], "Justin Gardener"),  # month > 12
        (["3", "4", "2", "10", "12", "0"], "Justin Gardener"),  # month > 12

        (["3", "4", "29", "10", "12", "0"], "Justin Gardener"),  # month > 12
        (["3", "4", "30", "10", "12", "0"], "Justin Gardener"),  # month > 12
        (["3", "4", "31", "10", "12", "0"], "Day does not exist."),  # month > 12
    ],
    ids=[
        "BVA-13",
        "BVA-14",
        "BVA-15",

        "BVA-16",
        "BVA-17",
        "BVA-18",
    ]
)
def test_4_day_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


# month
@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3", "0", "5", "10", "12", "0"], "Month does not exist."),
        (["3", "1", "5", "10", "12", "0"], "Justin Gardener"),
        (["3", "2", "5", "10", "12", "0"], "Justin Gardener"),

        (["3", "11", "5", "10", "12", "0"], "Justin Gardener"),
        (["3", "12", "5", "10", "12", "0"], "Justin Gardener"),
        (["3", "13", "5", "10", "12", "0"], "Month does not exist."),
    ],
    ids=[
        "BVA-19",
        "BVA-20",
        "BVA-21",

        "BVA-22",
        "BVA-23",
        "BVA-24",
    ]
)
def test_month_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out

# Start time
@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3", "5", "5", "-1", "23", "0"], "Illegal hour."),
        (["3", "5", "5", "0", "23", "0"], "Justin Gardener"),
        (["3", "5", "5", "1", "23", "0"], "Justin Gardener"),

        (["3", "5", "5", "21", "23", "0"], "Justin Gardener"),
        (["3", "5", "5", "22", "23", "0"], "Justin Gardener"),
        (["3", "5", "5", "23", "23", "0"], "Illegal hour."),
    ],
    ids=[
        "BVA-25",
        "BVA-26",
        "BVA-27",

        "BVA-28",
        "BVA-29",
        "BVA-30",
    ]
)
def test_start_time_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out

# end time
@pytest.mark.parametrize(
    "inputs, expected",
    [
        (["3", "5", "5", "0", "-1", "0"], "Illegal hour."),
        (["3", "5", "5", "0", "0", "0"], "Justin Gardener"),
        (["3", "5", "5", "0", "1", "0"], "Justin Gardener"),

        (["3", "5", "5", "0", "22", "0"], "Justin Gardener"),
        (["3", "5", "5", "0", "23", "0"], "Justin Gardener"),
        (["3", "5", "5", "0", "24", "0"], "Illegal hour."),
    ],
    ids=[
        "BVA-31",
        "BVA-32",
        "BVA-33",

        "BVA-34",
        "BVA-35",
        "BVA-36",
    ]
)
def test_end_time_input(monkeypatch, capsys, planner, inputs, expected):
    input_iter = iter(inputs)
    monkeypatch.setattr('builtins.input', lambda _: next(input_iter))

    with pytest.raises(SystemExit):
        planner.main_menu()

    captured = capsys.readouterr()
    assert expected in captured.out


