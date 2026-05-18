import pytest
from unittest.mock import MagicMock
from logic.ConflictException import ConflictsException
from logic.Person import Person

# Test that person's name is correctly returned
def test_get_name():
    person = Person("Miles")

    # Confirm that person's name was returned
    assert person.get_name() == "Miles"

# Test that meetings are added successfully
def test_add_meeting_success():
    person = Person("Miles")
    meeting = MagicMock() # Create mock meeting and calender
    person.calendar = MagicMock()

    person.add_meeting(meeting) # Add the meeting to that person's calender and ensure the method was called once
    person.calendar.add_meeting.assert_called_once_with(meeting)

# Test that failing to add meetings correctly raises an exception
def test_add_meeting_failure():
    person = Person("Miles")
    meeting = MagicMock() # Create mock meeting and calender
    person.calendar = MagicMock()

    person.calendar.add_meeting.side_effect = ConflictsException("Attendee conflict")  # Assign an exception to the method

    # Verify the exception and add the meeting to that person's calender
    with pytest.raises(ConflictsException) as exc_info:
        person.add_meeting(meeting)

    # Catch the exception and ensure the method was called once
    assert "Conflict for attendee Miles" in str(exc_info.value)
    person.calendar.add_meeting.assert_called_once_with(meeting)

# Test that print agenda returns only month if only a month is provided as a parameter
def test_print_agenda_month():
    person = Person("Miles")
    person.calendar = MagicMock() # Create calender and assign a return value for the method
    person.calendar.print_agenda.return_value = "Print agenda month output"

    result = person.calendar.print_agenda(5) # Insert only a month as a parameter

    # Ensure that month is outputted and the method was called
    assert result == "Print agenda month output"
    person.calendar.print_agenda.assert_called_once_with(5)

# Test that print agenda returns month and day if both are provided as a parameter
def test_print_agenda_day():
    person = Person("Miles")
    person.calendar = MagicMock() # Create calender and assign a return value for the method
    person.calendar.print_agenda.return_value = "Print agenda day output"

    result = person.calendar.print_agenda(5, 12) # Insert a month and day as parameters

    # Ensure that month+day is outputted and the method was called
    assert result == "Print agenda day output"
    person.calendar.print_agenda.assert_called_once_with(5, 12)

# Test is busy correctly returns the right boolean
def test_is_busy():
    person = Person("Miles")
    person.calendar = MagicMock() # Create calender and assign a return value for the method
    person.calendar.is_busy.return_value = True

    result = person.is_busy(5, 10, 9 ,11) # Insert month, day, start time and end time as parameters

    # Ensure that the method was called and the correct boolean state was returned too
    person.calendar.is_busy.assert_called_once_with(5, 10, 9, 11)
    assert result is True

# Test get meeting returns the correct meeting
def test_get_meeting():
    person = Person("Miles")
    meeting = MagicMock()  # Create mock meeting and calender
    person.calendar = MagicMock()
    person.calendar.get_meeting.return_value = meeting # Assign a return value for the method

    result = person.get_meeting(5, 10, 0) # Insert month, day and index as parameters

    # Ensure the correct meeting is returned
    assert result == meeting

# Test remove meeting removes the correct meeting
def test_remove_meeting():
    person = Person("Miles")
    person.calendar = MagicMock() # Create mock calender

    person.calendar.remove_meeting(5, 10, 0) # Insert month, day and index as parameters

    # Ensure the method was called using the right parameters
    person.calendar.remove_meeting.assert_called_once_with(5, 10, 0)



