import pytest
from unittest.mock import MagicMock

from logic.ConflictException import ConflictsException
from logic.Room import Room


# test invalid add meeting to raise conflict exception
def test_add_meeting_RP1():
    room = Room("J204")

    # Create mock meeting
    meeting = MagicMock()

    # mock calendar.add_meeting to raise exception
    room.calendar = MagicMock()
    room.calendar.add_meeting.side_effect = ConflictsException("Time conflict")

    # verify exception and add meeting
    with pytest.raises(ConflictsException) as exc_info:
        room.add_meeting(meeting)

    # Catches exception and test it has correct exception
    assert "Conflict for room J204" in str(exc_info.value)
    assert "Time conflict" in str(exc_info.value)
    # Confirm add meeting is called with correct variables
    room.calendar.add_meeting.assert_called_once_with(meeting)

# Test print agenda return self.calendar.print_agenda(month, day)
def test_print_agenda_RP2():
    room = Room("J204")

    # Mock calendar.print_agenda to return value
    room.calendar = MagicMock()
    room.calendar.print_agenda.return_value = "print agenda Output"

    result = room.print_agenda(5, 12)
    assert result == "print agenda Output"

    room.calendar.print_agenda.assert_called_once(5, 12)

# Test full only path of init, add, get id, print agenda, is busy, get meeting, remove meeting
def test_room_RP3():
    room = Room("J204")

    # Replace calendar with mock
    room.calendar = MagicMock()

    meeting = MagicMock()

    #  Return values
    room.calendar.print_agenda.return_value = "print agenda Output"
    room.calendar.is_busy.return_value = True
    room.calendar.get_meeting.return_value = meeting

    # get_id
    assert room.get_id() == "J204"

    # add_meeting
    room.add_meeting(meeting)
    room.calendar.add_meeting.assert_called_once_with(meeting)

    # print_agenda
    agenda = room.print_agenda(5)
    assert agenda == "print agenda Output"
    room.calendar.print_agenda.assert_called_with(5)

    # is busy
    busy = room.is_busy(5, 10, 9, 11)
    assert busy is True
    room.calendar.is_busy.assert_called_once_with(5, 10, 9, 11)

    # get_meeting
    meeting = room.get_meeting(5, 10, 0)
    assert meeting == meeting
    room.calendar.print_agenda.assert_called_once_with(5, 10, 0)

    # remove_meeting
    room.remove_meeting(5, 10, 0)
    room.calendar.print_agenda.assert_called_once_with(5, 10, 0)