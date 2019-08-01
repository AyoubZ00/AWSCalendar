import json
# from ServiceCalendar.CalendarEventsService import *
from src.calendarServ.RepositoriesCalendar.select_calendar import * 
from src.calendarServ.ServiceCalendar.holidayEventsService import *
from src.calendarServ.ServiceCalendar.CalendarEventsService import *
from src.calendarServ.ServiceCalendar.toggleHolidayAware import *

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

def getNextCalendarAPI(calendar_id,basedate):
    api = to_dict(instantiateNextCalendarEvents(calendar_id,basedate))
    return api 

def getPeriodCalendarAPI(calendar_id,basedate,enddate):
    api = to_dict(instantiatePeriodCalendarEvents(calendar_id,basedate,enddate))
    return api 


def getOneAwareTodayCalendarAPI(calendar_id):
    api = to_dict(invokeAHolidayAwareCalendarToday(calendar_id))
    return api 

def getOneAwareForADayCalendarAPI(calendar_id,basedate):
    api = to_dict(invokeAHolidayAwareCalendarForADay(calendar_id,basedate))
    return api

def getOneAwareNextCalendarAPI(calendar_id,basedate):
    api = to_dict(invokeAHolidayAwareCalendarForNext(calendar_id,basedate))
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
        s = "%Y-%m-%dT%H:%M:%SZ"
        o = o.strftime(s)
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
