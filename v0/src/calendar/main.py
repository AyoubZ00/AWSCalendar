from ServiceCalendar.parsetojson import *
import json
import dateutil.parser
def createCalendar(event, context):
        # yourdate = dateutil.parser.parse(adate)
    return {
        'body': json.loads(getOneTodayCalendarAPI(20))
    }
    
    


if __name__ == '__main__':
    # adate = '2019-07-30T08:00:00Z'
    # yourdate = dateutil.parser.parse(adate)
    # event = {}
    # event['date'] = '2019-07-30T08:00:00Z'
    # print(createCalendar(event,'hey'))
    print(createCalendar(1,'hey'))
