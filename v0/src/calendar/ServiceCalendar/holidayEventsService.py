from v0.src.calendar.RepositoriesCalendar.select_holidays import * 
from v0.src.calendar.ServiceCalendar.convertcronmethod import convertCronDateNoDuration
from v0.src.calendar.ServiceCalendar.CalendarEventsService import *
from v0.src.calendar.ServiceCalendar.convertcronmethod import *
from v0.src.calendar.ServiceCalendar.holidayclass import *


def allHolidays():
    holidaysList = []
    conn = connect()
    rows = get_holidays(conn)
    conn.close()
    for row in rows : 
        aholiday = HolidayClass(row[0],
                                convertCronDateNoDuration(row[1]),
                                row[2],
                                row[3]
        )
        holidaysList.append(aholiday)
    return holidaysList


