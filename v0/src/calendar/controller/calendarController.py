from v0.src.calendar.ServiceCalendar.parsetojson import * 

def createCalendar(event, context):
    return {
        'body': getOneCalendarAPI('20')
    }
