from unittest import result

import pytest
from unittest.mock import MagicMock

from logic.Calendar import Calendar
from logic.ConflictException import ConflictsException

@pytest.mark.parametrize(
    "month, day, start, end, result",
    [(5, 0, 9, 10, "Day does not exist"),
     (12, 10, 9, 10, "Month does not exist"),
     (5, 10, 23, 10, "Illegal hour"),
     (5, 10, 9, 24, "Illegal hour"),
     (5, 10, 15, 10, "Meeting starts before it ends")],
    ids=["1", "2", "3", "4", "5"],
)
def test_check_times(month, day, start, end, result):
    with pytest.raises(ConflictsException, match=result):
        Calendar.check_times(month, day, start, end)




def test_clear_schedule():
    cal = Calendar()

    meeting = MagicMock()

    cal.occupied[5][10].append(meeting)

    # verify meeting exist
    assert len(cal.occupied[5][10]) == 1

    # remove meeting
    cal.clear_schedule(5, 10)

    # assert
    assert cal.occupied[5][10] == []

# print agenda month / day
def test_print_agenda_day_empty():
    cal = Calendar()

    result = cal.print_agenda(5, 10)

    assert result == "No Meetings booked on this date.\n\n"

def test_print_agenda_day_filled():
    cal = Calendar()

    meeting = MagicMock()
    meeting.__str__.return_value = "Meeting"

    cal.occupied[5][10].append(meeting)

    result = cal.print_agenda(5, 10)

    assert "Agenda for 5/10 are as follows:" in result
    assert "Meeting" in result

# print agenda month
def test_print_agenda_month_empty():
    cal = Calendar()

    result = cal.print_agenda(5)

    assert result == "No Meetings booked on this date.\n\n"

def test_print_agenda_month_filled():
    cal = Calendar()

    meeting = MagicMock()
    meeting.__str__.return_value = "Meeting"

    cal.occupied[5].append(meeting)

    result = cal.print_agenda(5)

    assert "Agenda for 5:\n" in result
    assert "Meeting" in result

# get meeting
def test_get_meeting():
    cal = Calendar()

    meeting = MagicMock()

    cal.occupied[5][10].append(meeting)

    result = cal.get_meeting(5, 10, 0)

    assert result == meeting


