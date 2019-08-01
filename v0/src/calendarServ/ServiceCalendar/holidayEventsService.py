from src.calendarServ.RepositoriesCalendar.select_holidays import * 
from src.calendarServ.ServiceCalendar.convertcronmethod import convertCronDateNoDuration
from src.calendarServ.ServiceCalendar.CalendarEventsService import *
from src.calendarServ.ServiceCalendar.convertcronmethod import *
from src.calendarServ.ServiceCalendar.holidayclass import *


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


