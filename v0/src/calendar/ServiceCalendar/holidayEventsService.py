from RepositoriesCalendar.select_holidays import * 
from ServiceCalendar.convertcronmethod import convertCronDateNoDuration
from ServiceCalendar.CalendarEventsService import *
from ServiceCalendar.convertcronmethod import *
from ServiceCalendar.holidayclass import *


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


