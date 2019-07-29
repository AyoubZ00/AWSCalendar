from datetime import datetime, timedelta
import json
from dataclasses import dataclass, asdict

class EventClass:
    #properties
    event_id = int
    name = str 
    description = str
    startdate = datetime 
    enddate   = datetime
   
    def __init__(self, id, name = '', description = '', date_start = None, date_end = None):
        self.event_id = id 
    # getter method
