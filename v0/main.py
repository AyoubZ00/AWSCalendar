from src.calendarServ.ServiceCalendar.parsetojson import *
import json
import dateutil.parser
from src.calendarServ.RepositoriesCalendar.insert_holiday import * 
from psycopg2 import pool

def GetCalendar(event, context):
        # yourdate = dateutil.parser.parse(adate)
    return {
        'body': json.loads(getOneTodayCalendarAPI(1))
    }
    

def GetSomeDayCalendar(event, context):
        yourdate = dateutil.parser.parse(event['date'])
        return {
        'body': json.loads(getOneADayCalendarAPI(20,yourdate))
    }


def GetNextCalendar(event, context):
        yourdate = dateutil.parser.parse(event['date'])
        return {
            'body': json.loads(getNextCalendarAPI(20, yourdate))
        }

def GetPeriodCalendar(event,context):
    yourdate = dateutil.parser.parse(event['startdate'])
    anotherdate = dateutil.parser.parse(event['enddate'])

    return {
        'body': json.loads(getPeriodCalendarAPI(20, yourdate,anotherdate))
    }

def GetHolidayAwareTodayCalendar(event,context):
    return {
        'body': json.loads(getOneAwareTodayCalendarAPI(20))
    }

def GetHolidayAwareADayCalendar(event,context):
    adate = dateutil.parser.parse(event['startdate'])
    return {
        'body': json.loads(getOneAwareForADayCalendarAPI(20,adate))
    }

def GetHolidayAwareNextCalendar(event,context):
    adate = dateutil.parser.parse(event['startdate'])
    return {
        'body': json.loads(getOneAwareNextCalendarAPI(20, adate))
    }

if __name__ == '__main__':
    # adate = '2019-07-30T08:00:00Z'
    # yourdate = dateutil.parser.parse(adate)
    # event = {}
    # event['startdate'] = '2019-08-11T08:00:00Z'
    # event['enddate'] = '2019-08-2T15:00:00Z'
    # # # print(createCalendar(event,'hey'))
    # # print(GetSomeDayCalendar(event,'hey'))
    # # print(getOneTodayCalendarAPI(20))
    # # getAllHolidaysAPI()
    # print(GetPeriodCalendar(event,'hey'))
    # print(GetHolidayAwareTodayCalendar(20,'hey'))
    # getAllHolidaysAPI()
    # print(insert_holiday('0 0 12 8 * 2019', "Eid Adha", "First Day of Eid Adha"))
    # print(insert_holiday('0 0 13 8 * 2019', "Eid Adha", "Second Day of Eid Adha"))
    # print(insert_holiday('0 0 14 7 * 2019', """Oued Ed-Dahab Day
    #                      """, """Oued Ed-Dahab Day
    #                      """))
    # print(GetHolidayAwareTodayCalendar(1, 'hey'))
    # params = config()
    # user = params['user']
    # password = params['password']
    # host = params['host']
    # database = params['database']
    # ddd = 'ddd'
    # print(f'hi {ddd}')
    # print(GetHolidayAwareNextCalendar(event, 'hey'))
    # for aholiday in getAllHolidaysAPI():
    #     print(aholiday)
    # conn = connect()
    # print(get_allevent(conn))
    # conn.close()
    print(GetCalendar(1,'hey'))
