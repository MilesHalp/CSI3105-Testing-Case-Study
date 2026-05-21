import pytest
from unittest.mock import MagicMock
from logic.Meeting import Meeting

def test_add_attendee_MP1():
    # Adds a mock person to the list of attendees, asserts if person is in attendees
    meet = Meeting(1, 1, 6, 12, attendees= None, room = None, description = "None")
    person = MagicMock()

    meet.add_attendee(person)
    assert meet.attendees[0] == person

def test_remove_attendee_MP2():
    # Adds a mock person to the list of attendees, asserts if person is in attendees
    # Removes a mock person from the list of attendees, asserts if person is no longer in attendees
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    person = MagicMock()

    meet.add_attendee(person)
    assert meet.attendees[0] == person
    meet.remove_attendee(person)
    assert meet.attendees == []

def test_str_MP3():
    # Tests if the list "meet" is converted to a string correctly when attendees is NONE
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    result = meet.__str__()
    assert result == 'Month: 1, Day: 1, Time slot: 6 - 12, Room No: N/A: None\nAttending: No attendees'

def test_str_MP4():
    # Tests if the list "meet" is converted to a string correctly when attendees is a list of mock attendees
    person = MagicMock()
    meet = Meeting(1, 1, 6, 12, attendees=person, room=None, description="None")

    result = meet.__str__()
    assert result == 'Month: 1, Day: 1, Time slot: 6 - 12, Room No: N/A: None\nAttending: '


def test_get_month_MP5():
    # tests get month from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    result = meet.get_month()
    assert result == 1

def test_set_month_MP6():
    # tests set month from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    meet.set_month(2)
    assert meet.month == 2

def test_get_day_MP7():
    # tests get day from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    result = meet.get_day()
    assert result == 1

def test_set_day_MP8():
    # tests set month from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    meet.set_day(2)
    assert meet.day == 2

def test_get_start_time_MP9():
    # tests get start time from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    result = meet.get_start_time()
    assert result == 6

def test_set_start_time_MP10():
    # tests set start time from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    meet.set_start_time(8)
    assert meet.start == 8

def test_get_end_time_MP11():
    # tests get end time from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    result = meet.get_end_time()
    assert result == 12

def test_set_end_time_MP12():
    # tests set end time from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    meet.set_end_time(14)
    assert meet.end == 14

def test_get_attendees_MP13():
    # tests get attendees from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    meet.get_attendees()
    assert meet.attendees == []

def test_get_room_MP14():
    # tests get room from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    meet.get_room()
    assert meet.room == None

def test_set_room_MP15():
    # tests set room from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    room = MagicMock()
    meet.set_room(room)
    assert meet.room == room

def test_get_description_MP16():
    # tests get description from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    meet.get_description()
    assert meet.description == "None"

def test_set_description_MP17():
    # tests set description from string "meet"
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    meet.set_description("New Description")
    assert meet.description == "New Description"