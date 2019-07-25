import psycopg2

from v0.src.calendar.RepositoriesCalendar.select_event import *
from v0.src.calendar.ServiceCalendar.eventclass import *
from v0.src.calendar.ServiceCalendar.convertcronmethod import *
from v0.src.calendar.ServiceCalendar.calendarclass import *
from v0.src.calendar.RepositoriesCalendar.select_calendar import *
from v0.src.calendar.ServiceCalendar.CalendarEventsService import *
from v0.src.calendar.ServiceCalendar.holidayEventsService import *


def instantiateACalendarEvents(calendarid):
    conn = connect()
    calendarRow = get_acalendar(calendarid,conn)
    rows = get_event(calendarRow[0],conn)
    InstantiatedEventsList = []
    conn.close()
    for row in rows:
        anInstantiatedEvent = instantiateOneEvent(row)
        InstantiatedEventsList.extend(anInstantiatedEvent)
    acalendar = CalendarClass(
        calendarRow[0], calendarRow[1], calendarRow[2],
        None, False)
    acalendar.events = InstantiatedEventsList
    return acalendar


def instantiateAllCalendarEvents():
    conn = connect()
    calendarRows = get_calendar(conn)
    calendarList = []
    for calendarRow in calendarRows:
        rows = get_event(calendarRow[0],conn)
        InstantiatedEventsList = []
        for row in rows:
            anInstantiatedEvent = instantiateOneEvent(row)
            InstantiatedEventsList.extend(anInstantiatedEvent)
        acalendar = CalendarClass(
            calendarRow[0], calendarRow[1], calendarRow[2],
            None, False)
        acalendar.events = InstantiatedEventsList
        calendarList.append(acalendar)
    conn.close()
    return calendarList


def instantiateOneEvent(row):
    instancesList = []
    dateTuples = convertCronDate(row[1], row[5])
    for adate in dateTuples:
           aevent = EventClass(row[0])
           aevent.name = row[2]
           aevent.description = row[3]
           aevent.date_start = adate[0]
           aevent.date_end = adate[1]
           instancesList.append(aevent)

    return instancesList
