import pytest
from unittest.mock import MagicMock
from logic.Meeting import Meeting

def test_add_attendee_MP1():
    meet = Meeting(1, 1, 6, 12, attendees= None, room = None, description = "None")
    person = MagicMock()

    meet.add_attendee(person)
    assert meet.attendees[0] == person

def test_remove_attendee_MP2():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    person = MagicMock()

    meet.add_attendee(person)
    assert meet.attendees[0] == person
    meet.remove_attendee(person)
    assert meet.attendees == []

def test_str_MP3():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    result = meet.__str__()
    assert result == 'Month: 1, Day: 1, Time slot: 6 - 12, Room No: N/A: None\nAttending: No attendees'

def test_str_MP4():
    person = MagicMock()
    meet = Meeting(1, 1, 6, 12, attendees=person, room=None, description="None")

    result = meet.__str__()
    assert result == 'Month: 1, Day: 1, Time slot: 6 - 12, Room No: N/A: None\nAttending: '


def test_get_month_MP5():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    result = meet.get_month()
    assert result == 1

def test_set_month_MP6():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    meet.set_month(2)
    assert meet.month == 2

def test_get_day_MP7():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    result = meet.get_day()
    assert result == 1

def test_set_day_MP8():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    meet.set_day(2)
    assert meet.day == 2

def test_get_start_time_MP9():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    result = meet.get_start_time()
    assert result == 6

def test_set_start_time_MP10():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    meet.set_start_time(8)
    assert meet.start == 8

def test_get_end_time_MP11():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    result = meet.get_end_time()
    assert result == 12

def test_set_end_time_MP12():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    meet.set_end_time(14)
    assert meet.end == 14

def test_get_attendees_MP13():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")


    meet.get_attendees()
    assert meet.attendees == []

def test_get_room_MP14():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")

    meet.get_room()
    assert meet.room == None

def test_set_room_MP15():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")
    room = MagicMock()

    meet.set_room(room)
    assert meet.room == room

def test_get_description_MP16():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")

    meet.get_description()
    assert meet.description == "None"

def test_set_description_MP17():
    meet = Meeting(1, 1, 6, 12, attendees=None, room=None, description="None")

    meet.set_description("New Description")
    assert meet.description == "New Description"