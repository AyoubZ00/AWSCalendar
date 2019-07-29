from datetime import datetime, timedelta


class HolidayClass:
    #properties
    holiday_id = int
    name = str
    description = str
    holiday_date = datetime

    def __init__(self, id, holiday_date = None, name='', description='' ):
        self.holiday_id = id
        self.holiday_date = holiday_date
        self.name = name
        self.description = description

