import pytest
from unittest.mock import MagicMock

from logic.Calendar import Calendar
from logic.ConflictException import ConflictsException
from logic.Room import Room


# test invalid add meeting to raise conflict exception
def test_invalid__add_meeting():
    room = Room("J204")

    fake_meeting = MagicMock()

    # mock calendar.add_meeting to raise exception
    room.calendar = MagicMock()
    room.calendar.add_meeting.side_effect = ConflictsException("Time conflict")

    # verify exception
    with pytest.raises(ConflictsException) as exc_info:
        room.add_meeting(fake_meeting)

    assert "Conflict for room J204" in str(exc_info.value)
    assert "Time conflict" in str(exc_info.value)

    room.calendar.add_meeting.assert_called_once_with(fake_meeting)

# Test print agenda return self.calandar.print_agenda(month, day)
def test_day_print_agenda():
    room = Room("J204")

    # Mock calendar.print_agenda to return value
    room.calendar = MagicMock()
    room.calendar.print_agenda.return_value = "Agenda Output"

    result = room.print_agenda(5, 12)
    assert result == "Agenda Output"

    room.calendar.print_agenda.assert_called_once(5, 12)

# test full only path of init, add, get id, print agenda, is busy, get meeting, remove meeting
def test_room():
    room = Room("J204")

    # replace calendar with mock
    room.calendar = MagicMock()

    fake_meeting = MagicMock()

    #  return values
    room.calendar.print_agenda.return_value = "Agenda Output"
    room.calendar.is_busy.return_value = True
    room.calendar.get_meeting.return_value = fake_meeting

    # get_id
    assert room.get_id() == "J204"

    # add meeting
    room.add_meeting(fake_meeting)
    room.calendar.add_meeting.assert_called_once_with(fake_meeting)

    # print_agenda
    agenda = room.print_agenda(5)
    assert agenda == "Agenda Output"
    room.calendar.print_agenda.assert_called_with(5)

    # is busy
    busy = room.is_busy(5, 10, 9, 11)
    assert busy is True
    room.calendar.is_busy.assert_called_once_with(5, 10, 9, 11)

    # get meeting
    meeting = room.get_meeting(5, 10, 0)
    assert meeting == fake_meeting
    room.calendar.print_agenda.assert_called_once_with(5, 10, 0)

    # remove meeting
    room.remove_meeting(5, 10, 0)
    room.calendar.print_agenda.assert_called_once_with(5, 10, 0)