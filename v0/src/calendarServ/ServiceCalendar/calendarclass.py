from datetime import datetime, timedelta


class CalendarClass:
    #properties
    id = int
    name = str 
    description = str
    events = list 
    holidayAware = bool 
   
    def __init__(self, id, name = '', description = '', events = None,
     holidayAware = None):
        self.id  = id
        self.name = name 
        self.description = description 
        self.events = events 
        self.holidayAware = holidayAware
    

    # def get_id(self):
    #     return self._id

    # # setter method
    # def set_id(self, x):
    #     self._id = x
    
    # def del_id(self):
    #     del self._id 

    # id = property(get_id, set_id, del_id)


