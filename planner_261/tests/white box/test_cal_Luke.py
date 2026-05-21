import pytest
from unittest.mock import MagicMock

from logic.Calendar import Calendar
from logic.ConflictException import ConflictsException


#4.1
def test_add_meeting_success_CP15():
    #replace calendar with mock
    cal = Calendar()
    meeting = MagicMock()
    meeting.calendar = MagicMock()

    meeting.get_month.return_value = 1
    meeting.get_day.return_value = 1
    meeting.get_start_time.return_value = 8
    meeting.get_end_time.return_value = 12
    meeting.get_description.return_value = "test meeting"

    cal.add_meeting(meeting)
    assert meeting in cal.occupied[1][1]

def test_add_meeting_success_CP16():
    #replace calendar with mock
    cal = Calendar()
    meeting = MagicMock()
    meeting.calendar = MagicMock()

    meeting.get_month.return_value = 1
    meeting.get_day.return_value = 1
    meeting.get_start_time.return_value = 8
    meeting.get_end_time.return_value = 12
    meeting.get_description.return_value = "Day does not exist"

    cal.add_meeting(meeting)
    assert meeting in cal.occupied[1][1]

def test_add_meeting_success_CP17():
    #replace calendar with mock
    cal = Calendar()
    meeting = MagicMock()
    meeting.calendar = MagicMock()

    meeting.get_month.return_value = 2
    meeting.get_day.return_value = 29
    meeting.get_start_time.return_value = 8
    meeting.get_end_time.return_value = 12
    meeting.get_description.return_value = "Day does not exist"

    cal.add_meeting(meeting)
    assert meeting in cal.occupied[2][29]

def test_add_meeting_success_CP18():
    #replace calendar with mock
    cal = Calendar()
    meeting = MagicMock()
    meeting.calendar = MagicMock()

    meeting.get_month.return_value = 2
    meeting.get_day.return_value = 2
    meeting.get_start_time.return_value = 8
    meeting.get_end_time.return_value = 12
    meeting.get_description.return_value = "Day does not exist"

    cal.add_meeting(meeting)
    assert meeting in cal.occupied[2][2]

def test_add_meeting_failure_times_CP19():
    #replace calendar with mock
    cal = Calendar()
    meeting = MagicMock()
    meeting.calendar = MagicMock()

    meeting.get_month.return_value = 2
    meeting.get_day.return_value = 2
    meeting.get_start_time.return_value = 12
    meeting.get_end_time.return_value = 14
    meeting.to_check.get_description.return_value = "Exists"

    cal.add_meeting(meeting)


    with pytest.raises(ConflictsException) as exc_info:
        cal.add_meeting(meeting)
    assert "Overlap with another item" in str(exc_info.value)

def test_add_meeting_failure_times_CP20():
    #replace calendar with mock
    cal = Calendar()
    meeting = MagicMock()
    meeting.calendar = MagicMock()

    meeting.get_month.return_value = 2
    meeting.get_day.return_value = 2
    meeting.get_start_time.return_value = 12
    meeting.get_end_time.return_value = 14
    meeting.to_check.get_description.return_value = "Exists"

    cal.add_meeting(meeting)

    meeting.get_start_time.return_value = 8

    with pytest.raises(ConflictsException) as exc_info:
        cal.add_meeting(meeting)
    assert "Overlap with another item" in str(exc_info.value)

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