import pytest
from unittest.mock import MagicMock
from logic.Meeting import Meeting

def test_add_attendee():
    meet = Meeting(1, 1, 6, 12, attendees= None, room = None, description = "None")
    person = MagicMock()

    meet.add_attendee(person)
    assert meet.attendees[0] == person

def test_remove_attendee():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    person = MagicMock()

    meet.add_attendee(person)
    assert meet.attendees[0] == person
    meet.remove_attendee(person)
    assert meet.attendees == []

def test_str():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    result = meet.__str__()
    assert result == 'Month: 1, Day: 1, Time slot: 6 - 12, Room No: N/A: None\nAttending: No attendees'

def test_get_month():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    result = meet.get_month()
    assert result == 1

def test_set_month():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    meet.set_month(2)
    assert meet.month == 2

def test_get_day():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    result = meet.get_day()
    assert result == 1

def test_set_day():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    meet.set_day(2)
    assert meet.day == 2

def test_get_start_time():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    result = meet.get_start_time()
    assert result == 6

def test_set_start_time():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    meet.set_start_time(8)
    assert meet.start == 8

def test_get_end_time():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    result = meet.get_end_time()
    assert result == 12

def test_set_end_time():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    meet.set_end_time(14)
    assert meet.end == 14

def test_get_attendees():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    meet.get_attendees()
    assert meet.attendees == []

def test_get_room():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")

    meet.get_room()
    assert meet.room == None

def test_set_room():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    room = MagicMock()

    meet.set_room(room)
    assert meet.room == room

def test_get_description():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")

    meet.get_description()
    assert meet.description == "None"

def test_set_description():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")

    meet.set_description("New Description")
    assert meet.description == "New Description"