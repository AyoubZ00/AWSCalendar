from calendarServ.RepositoriesCalendar.select_holidays import *
from calendarServ.ServiceCalendar.convertcronmethod import convertCronDateNoDuration
from calendarServ.ServiceCalendar.CalendarEventsService import *
from calendarServ.ServiceCalendar.convertcronmethod import *
from calendarServ.ServiceCalendar.holidayclass import *

def toggleHolidayAware(holidayList, calendarList):
    newcalendarlist = []
    newcalendarlist = calendarList
    for acalendar in calendarList: 
      newcalendar = CalendarClass(acalendar.id,acalendar.name,acalendar.description)
      neweventsList = []
      for aevent in acalendar.events:
        if(handleEvent(aevent,holidayList)):
            x = newcalendarlist.events.index(aevent.date_start)
            del newcalendarlist.events[x]
    return newcalendarlist

def handleEvent(date,holidaylist):
        for aholiday in holidaylist:
            if(compareTwoDates(date, aholiday)):
                return True
        return False 
                
    

def invokeAHolidayAwareCalendar(calendarid):
    conn = connect()
    calendarRow = get_acalendar(calendarid, conn)
    rows = get_event(calendarRow[0], conn)
    lines = get_holidays(conn) 
    InstantiatedEventsList = []
    conn.close()
    for row in rows:
        anInstantiatedEvent = instantiateOneAwareEvent(row,lines)
        InstantiatedEventsList.extend(anInstantiatedEvent)
    acalendar = CalendarClass(
        calendarRow[0], calendarRow[1], calendarRow[2],
        None, True)
    acalendar.events = InstantiatedEventsList
    return acalendar


def invokeAHolidayAwareCalendarToday(calendarid):
    conn = connect()
    calendarRow = get_acalendar(calendarid, conn)
    rows = get_event(calendarRow[0], conn)
    lines = get_holidays(conn)
    InstantiatedEventsList = []
    conn.close()
    for row in rows:
        anInstantiatedEvent = instantiateOneAwareEventToday(row, lines)
        InstantiatedEventsList.extend(anInstantiatedEvent)
    acalendar = CalendarClass(
        calendarRow[0], calendarRow[1], calendarRow[2],
        None, True)
    acalendar.events = InstantiatedEventsList
    return acalendar


def invokeAHolidayAwareCalendarForADay(calendarid,basedate):
    conn = connect()
    calendarRow = get_acalendar(calendarid, conn)
    rows = get_event(calendarRow[0], conn)
    lines = get_holidays(conn)
    InstantiatedEventsList = []
    conn.close()
    for row in rows:
        anInstantiatedEvent = instantiateOneAwareEventForADay(
            row, lines, basedate)
        InstantiatedEventsList.extend(anInstantiatedEvent)
    acalendar = CalendarClass(
        calendarRow[0], calendarRow[1], calendarRow[2],
        None, True)
    acalendar.events = InstantiatedEventsList
    return acalendar


def invokeAHolidayAwareCalendarForNext(calendarid, basedate):
    conn = connect()
    calendarRow = get_acalendar(calendarid, conn)
    rows = get_event(calendarRow[0], conn)
    lines = get_holidays(conn)
    InstantiatedEventsList = []
    conn.close()
    for row in rows:
        anInstantiatedEvent = instantiateOneAwareEventForNext(
            row, lines, basedate)
        InstantiatedEventsList.extend(anInstantiatedEvent)
    acalendar = CalendarClass(
        calendarRow[0], calendarRow[1], calendarRow[2],
        None, True)
    acalendar.events = InstantiatedEventsList
    return acalendar

def instantiateOneAwareEvent(row,lines):
    instancesList = []
    dateTuples = convertCronDate(row[1], row[5])
    allHolidayDates = []
    for line in lines : 
        dateHolidays = convertCronDateNoDuration(line[1])
        allHolidayDates.append(dateHolidays)
    for adate in dateTuples:
        if(not handleEvent(adate[0],allHolidayDates)):
           aevent = EventClass(row[0])
           aevent.name = row[2]
           aevent.description = row[3]
           aevent.date_start = adate[0]
           aevent.date_end = adate[1]
           instancesList.append(aevent)
    return instancesList


def instantiateOneAwareEventToday(row, lines):
    instancesList = []
    dateTuples = []
    if(convertCronDateToday(row[1], row[5]) is not None):
        dateTuples = convertCronDateToday(row[1], row[5])
    allHolidayDates = []
    for line in lines:
        dateHolidays = convertCronDateNoDuration(line[1])
        allHolidayDates.append(dateHolidays)
    for adate in dateTuples:
        if(not handleEvent(adate[0], allHolidayDates)):
           aevent = EventClass(row[0])
           aevent.name = row[2]
           aevent.description = row[3]
           aevent.startdate = adate[0]
           aevent.enddate = adate[1]
           instancesList.append(aevent)
    return instancesList


def instantiateOneAwareEventForADay(row, lines,basedate):
    instancesList = []
    dateTuples = []
    if(convertCronDateADay(row[1], row[5],basedate) is not None):
        dateTuples = convertCronDateADay(row[1], row[5],basedate)
    allHolidayDates = []
    for line in lines:
        dateHolidays = convertCronDateNoDuration(line[1])
        allHolidayDates.append(dateHolidays)
    for adate in dateTuples:
        if(not handleEvent(adate[0], allHolidayDates)):
           aevent = EventClass(row[0])
           aevent.name = row[2]
           aevent.description = row[3]
           aevent.startdate = adate[0]
           aevent.enddate = adate[1]
           instancesList.append(aevent)
    return instancesList


def instantiateOneAwareEventForNext(row, lines, basedate):
    instancesList = []
    dateTuples = []
    # if(convertCronDateNext(row[1], row[5], basedate) is not None):
    #     dateTuples = convertCronDateNext(row[1], row[5], basedate)
    allHolidayDates = []
    for line in lines:
        dateHolidays = convertCronDateNoDuration(line[1])
        allHolidayDates.append(dateHolidays)
    dateTuples = convertCronDateNextHolidayAware(row[1], row[5], basedate,allHolidayDates)
    for adate in dateTuples:
        
           aevent = EventClass(row[0])
           aevent.name = row[2]
           aevent.description = row[3]
           aevent.startdate = adate[0]
           aevent.enddate = adate[1]
           instancesList.append(aevent)


    return instancesList
