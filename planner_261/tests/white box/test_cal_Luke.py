import pytest
from unittest.mock import MagicMock

from logic.Calendar import Calendar
from logic.ConflictException import ConflictsException

#4.1
def test_add_meeting():
    #replace calendar with mock
    cal = Calendar()

    fake_meeting = MagicMock()

    cal.add_meeting(fake_meeting)
