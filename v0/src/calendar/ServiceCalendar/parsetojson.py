import json
# from ServiceCalendar.CalendarEventsService import *
from v0.src.calendar.RepositoriesCalendar.select_calendar import * 
from v0.src.calendar.ServiceCalendar.holidayEventsService import *
from v0.src.calendar.ServiceCalendar.CalendarEventsService import *
from v0.src.calendar.ServiceCalendar.toggleHolidayAware import *

def getOneCalendarAPI(calendar_id):
    api = to_dict(instantiateACalendarEvents(calendar_id))
    return api

def getOneAwareCalendarAPI(calendar_id):
    api = to_dict(invokeAHolidayAwareCalendar(calendar_id))
    return api 

# def to_dict(calendar_id):
#     return json.loads(json.dumps(instantiateACalendarEvents(calendar_id), default=myconverter))

def to_dict(obj):
    return json.dumps(obj, default=myconverter,
     indent=4, sort_keys=True)




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
