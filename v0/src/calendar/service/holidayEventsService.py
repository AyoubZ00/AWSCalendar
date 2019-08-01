from repository.select_holidays import *
from service.convertcronmethod import convertCronDateNoDuration
from service.CalendarEventsService import *
from service.convertcronmethod import *
from service.holidayclass import *


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


