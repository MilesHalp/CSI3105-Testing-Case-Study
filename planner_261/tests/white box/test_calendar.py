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
     (5, 10, 15, 10, "Meeting starts before it ends"),
     (5, 10, 9, 10, None)],
    ids=["CP1", "CP2", "CP3", "CP4", "CP5", "Y"],
)
def test_check_times(month, day, start, end, result):
    if result is None: # Tests to make sure it runs without error
        Calendar.check_times(month, day, start, end)
    else:
        with pytest.raises(ConflictsException, match=result):
            Calendar.check_times(month, day, start, end)

@pytest.mark.parametrize(
    "month, day, start, end, result",
    [(5, 1, 0, 23, False),
     (5, 10, 9, 10, True),
     (5, 10, 8, 9, True),
     (5, 10, 12, 14, False)
    ],
    ids = ["CP11", "CP12", "CP13", "CP14"],
)
def test_is_busy(month, day, start, end, result):
    cal = Calendar()

    meeting = MagicMock()
    meeting.get_start_time.return_value = 9
    meeting.get_end_time.return_value = 10

    if day != 0:
        cal.occupied[month][day].append(meeting)

    outcome = cal.is_busy(month, day, start, end)

    assert outcome == result

def test_clear_schedule_CP10():
    cal = Calendar()

    meeting1 = MagicMock()
    meeting2 = MagicMock()

    # Add two meetings to the same day
    cal.occupied[5][10].append(meeting1)
    cal.occupied[5][10].append(meeting2)

    # confirms meetings exist
    assert len(cal.occupied[5][10]) == 2

    # remove meeting
    cal.clear_schedule(5, 10)

    # asserts that schedule is empty
    assert cal.occupied[5][10] == []

# Test print agenda month & day with no meeting
def test_print_agenda_CP8():
    cal = Calendar()

    result = cal.print_agenda(5, 10)

    assert result == "No Meetings booked on this date.\n\n"

# Test print agenda month & day with a meeting
def test_print_agenda_CP9():
    cal = Calendar()

    meeting = MagicMock()
    meeting.__str__.return_value = "Meeting"

    cal.occupied[5][10].append(meeting)

    result = cal.print_agenda(5, 10)

    assert "Agenda for 5/10 are as follows:" in result
    assert "Meeting" in result

# Test print agenda with only month variable with no meeting
def test_print_agenda_CP6():
    cal = Calendar()

    result = cal.print_agenda(5)

    assert result == "No Meetings booked on this date.\n\n"

# Test print agenda with only month variable with a meeting
def test_print_agenda_CP7():
    cal = Calendar()

    meeting = MagicMock()
    meeting.__str__.return_value = "Meeting"

    cal.occupied[5].append(meeting)

    result = cal.print_agenda(5)

    assert "Agenda for 5:\n" in result
    assert "Meeting" in result

# Tests path CP21
def test_get_meeting_CP21():
    cal = Calendar()

    meeting = MagicMock()

    cal.occupied[5][10].append(meeting)

    result = cal.get_meeting(5, 10, 0)

    assert result == meeting

# Tests path CP22
def test_remove_meeting_CP22():
    cal = Calendar()

    meeting = MagicMock()

    cal.occupied[5][10].append(meeting)

    cal.remove_meeting(5, 10, 0)

    assert cal.occupied[5][10] == []


