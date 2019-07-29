import json
# from ServiceCalendar.CalendarEventsService import *
from calendarServ.RepositoriesCalendar.select_calendar import * 
from calendarServ.ServiceCalendar.holidayEventsService import *
from calendarServ.ServiceCalendar.CalendarEventsService import *
from calendarServ.ServiceCalendar.toggleHolidayAware import *

def getOneCalendarAPI(calendar_id):
    api = to_dict(instantiateACalendarEvents(calendar_id))
    return api

def getOneTodayCalendarAPI(calendar_id):
    api = to_dict(instantiateACalendarEventsForToday(calendar_id))
    return api


def getOneADayCalendarAPI(calendar_id, basedate):
    api = to_dict(instantiateACalendarEventsForADay(calendar_id, basedate))
    return api

def getOneAwareCalendarAPI(calendar_id):
    api = to_dict(invokeAHolidayAwareCalendar(calendar_id))
    return api 

# def to_dict(calendar_id):
#     return json.loads(json.dumps(instantiateACalendarEvents(calendar_id), default=myconverter))

def to_dict(obj):
    return json.dumps(obj, default=myconverter,
     indent=4,)
#sort_keys=True



# def myconverter(o):
#     if isinstance(o, datetime.datetime):
#         return o.__str__()
#     else:
#         return o.__dict__


def myconverter(o):
    if isinstance(o, datetime):
        return o.__str__()
    else:
        return o.__dict__



def getAllCalendarsAPI():
    allCalendars = instantiateAllCalendarEvents()
    apis = []
    for acalendar in allCalendars: 
        api = to_dict(acalendar)
        print(api)
        apis.append(api)
    return apis

def getAllHolidaysAPI():
    apis = []
    allholidays = allHolidays()
    for aHoliday in allholidays:
        api = to_dict(aHoliday)
        print(api)
        apis.append(api)
    return apis


def getAllCalendarsAPI2():
    allCalendars = toggleHolidayAware(
        allHolidays(), instantiateAllCalendarEvents())
    apis = []
    for acalendar in allCalendars:
        api = to_dict(acalendar)
        print(api)
        apis.append(api)
    return apis
