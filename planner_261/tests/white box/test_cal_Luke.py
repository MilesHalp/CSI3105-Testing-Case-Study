import pytest
from unittest.mock import MagicMock

from logic.Calendar import Calendar
from logic.ConflictException import ConflictsException
from logic.Meeting import Meeting


#4.1
def test_add_meeting_success():
    #replace calendar with mock
    cal = Calendar()
    meeting = MagicMock()
    meeting.calendar = MagicMock()

    meeting.get_month.return_value = 1
    meeting.get_day.return_value = 1
    meeting.get_start_time.return_value = 8
    meeting.get_end_time.return_value = 12

    cal.add_meeting(meeting)
    assert meeting in cal.occupied[1][1]


def test_add_meeting_failure_day():
    #replace calendar with mock
    cal = Calendar()
    meeting = MagicMock()
    meeting.calendar = MagicMock()

    meeting.get_month.return_value = 2
    meeting.get_day.return_value = 42
    meeting.get_start_time.return_value = 8
    meeting.get_end_time.return_value = 12

    with pytest.raises(ConflictsException) as exc_info:
        cal.add_meeting(meeting)
    assert "Day does not exist." in str(exc_info.value)


def test_add_meeting_failure_month():
    #replace calendar with mock
    cal = Calendar()
    meeting = MagicMock()
    meeting.calendar = MagicMock()

    meeting.get_month.return_value = 42
    meeting.get_day.return_value = 2
    meeting.get_start_time.return_value = 8
    meeting.get_end_time.return_value = 12

    with pytest.raises(ConflictsException) as exc_info:
        cal.add_meeting(meeting)
    assert "Month does not exist." in str(exc_info.value)

def test_add_meeting_failure_times():
    #replace calendar with mock
    cal = Calendar()
    meeting = MagicMock()
    meeting.calendar = MagicMock()

    meeting.get_month.return_value = 2
    meeting.get_day.return_value = 2
    meeting.get_start_time.side_effect = [12, 13, 13]
    meeting.get_end_time.side_effect = [14, 15, 15]


    with pytest.raises(ConflictsException) as exc_info:
        cal.add_meeting(meeting)
    #assert "Overlap with another item" in str(exc_info.value)