from RepositoriesCalendar.select_holidays import *
from ServiceCalendar.convertcronmethod import convertCronDateNoDuration
from ServiceCalendar.CalendarEventsService import *
from ServiceCalendar.convertcronmethod import *
from ServiceCalendar.holidayclass import *


def toggleHolidayAware(holidayList, calendarList):
    newcalendarlist = []
    for acalendar in calendarList: 
      newcalendar = CalendarClass(acalendar.id,acalendar.name,acalendar.description)
      neweventsList = []
      for aevent in acalendar.events:
        for aholiday in holidayList:
            if(not compareTwoDates(aevent.date_start,aholiday.holiday_date)):
                neweventsList.append(aevent)
            else: 
                continue 
      newcalendar.events = neweventsList
      newcalendarlist.append(newcalendar)
    return newcalendarlist

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

def instantiateOneAwareEvent(row,lines):
    instancesList = []
    dateTuples = convertCronDate(row[1], row[5])
    allHolidayDates = []
    for line in lines : 
        dateHolidays = convertCronDateNoDuration(line[1])
        allHolidayDates.append(dateHolidays)
    for adate in dateTuples:
        for aholidaydate in allHolidayDates:
         if(not compareTwoDates(adate[0],aholidaydate)):
           aevent = EventClass(row[0])
           aevent.name = row[2]
           aevent.description = row[3]
           aevent.date_start = adate[0]
           aevent.date_end = adate[1]
           instancesList.append(aevent)
           continue
        continue

    return instancesList
