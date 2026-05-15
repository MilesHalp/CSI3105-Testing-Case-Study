import pytest
from unittest.mock import MagicMock

from logic.Calendar import Calendar
from logic.ConflictException import ConflictsException
from logic.Meeting import Meeting


#4.1
def test_add_meeting(monkeypatch):
    #replace calendar with mock
    cal = Calendar()
    meeting = MagicMock()

    monkeypatch.setenv("m_month", 1)
    monkeypatch.setenv("m_day", 2)
    monkeypatch.setenv("m_start", 8)
    monkeypatch.setenv("m_end", 12)


    monkeypatch.setattr(cal, 'check_times', MagicMock(return_value=None))

    monkeypatch.setenv("to_check.get_description", "Exists")
    monkeypatch.setenv("to_check.get_start_time", "12")
    monkeypatch.setenv("to_check.get_end_time", "8")

    cal.add_meeting(meeting)
