import psycopg2

from repository.select_event import *
from service.eventclass import *
from service.convertcronmethod import *
from service.calendarclass import *
from repository.select_calendar import *
from service.CalendarEventsService import *
from service.holidayEventsService import *


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


def instantiateACalendarEventsForToday(calendarid):
    conn = connect()
    calendarRow = get_acalendar(calendarid, conn)
    rows = get_event(calendarRow[0], conn)
    InstantiatedEventsList = []
    conn.close()
    for row in rows:
        anInstantiatedEvent = instantiateOneEventForToday(row)
        InstantiatedEventsList.extend(anInstantiatedEvent)
    acalendar = CalendarClass(
        calendarRow[0], calendarRow[1], calendarRow[2],
        None, False)
    acalendar.events = InstantiatedEventsList
    return acalendar


def instantiateACalendarEventsForADay(calendarid,basedate):
    conn = connect()
    calendarRow = get_acalendar(calendarid, conn)
    rows = get_event(calendarRow[0], conn)
    InstantiatedEventsList = []
    conn.close()
    for row in rows:
        anInstantiatedEvent = instantiateOneEventForADay(row,basedate)
        InstantiatedEventsList.extend(anInstantiatedEvent)
    acalendar = CalendarClass(
        calendarRow[0], calendarRow[1], calendarRow[2],
        None, False)
    acalendar.events = InstantiatedEventsList
    return acalendar


def instantiateNextCalendarEvents(calendarid, basedate):
    conn = connect()
    calendarRow = get_acalendar(calendarid, conn)
    rows = get_event(calendarRow[0], conn)
    InstantiatedEventsList = []
    conn.close()
    for row in rows:
        anInstantiatedEvent = instantiateOneEventForNext(row, basedate)
        InstantiatedEventsList.extend(anInstantiatedEvent)
    acalendar = CalendarClass(
        calendarRow[0], calendarRow[1], calendarRow[2],
        None, False)
    acalendar.events = InstantiatedEventsList
    return acalendar


def instantiatePeriodCalendarEvents(calendarid, basedate,enddate):
    conn = connect()
    calendarRow = get_acalendar(calendarid, conn)
    rows = get_event(calendarRow[0], conn)
    InstantiatedEventsList = []
    conn.close()
    for row in rows:
        anInstantiatedEvent = instantiateOneEventPeriod(row, basedate,enddate)
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


def instantiateOneEventForToday(row):
    instancesList = []
    if(convertCronDateToday(row[1], row[5]) is not None):
      dateTuples = convertCronDateToday(row[1], row[5])
      for adate in dateTuples:
             aevent = EventClass(row[0])
             aevent.name = row[2]
             aevent.description = row[3]
             aevent.startdate = adate[0]
             aevent.enddate = adate[1]
             instancesList.append(aevent)

    return instancesList


def instantiateOneEventForADay(row,basedate):
    instancesList = []
    if(convertCronDateADay(row[1], row[5], basedate) is not None):
      dateTuples = convertCronDateADay(row[1], row[5], basedate)
      for adate in dateTuples:
             aevent = EventClass(row[0])
             aevent.name = row[2]
             aevent.description = row[3]
             aevent.startdate = adate[0]
             aevent.enddate = adate[1]
             instancesList.append(aevent)

    return instancesList


def instantiateOneEventForNext(row, basedate):
    instancesList = []
    if(convertCronDateADay(row[1], row[5], basedate) is not None):
      dateTuples = convertCronDateNext(row[1], row[5], basedate)
      for adate in dateTuples:
             aevent = EventClass(row[0])
             aevent.name = row[2]
             aevent.description = row[3]
             aevent.startdate = adate[0]
             aevent.enddate = adate[1]
             instancesList.append(aevent)

    return instancesList


def instantiateOneEventPeriod(row, basedate,enddate):
    instancesList = []
    if(convertCronDateByPeriod(row[1], row[5], basedate,enddate) is not None):
      dateTuples = convertCronDateByPeriod(row[1], row[5], basedate,enddate)
      for adate in dateTuples:
             aevent = EventClass(row[0])
             aevent.name = row[2]
             aevent.description = row[3]
             aevent.startdate = adate[0]
             aevent.enddate = adate[1]
             instancesList.append(aevent)

    return instancesList
