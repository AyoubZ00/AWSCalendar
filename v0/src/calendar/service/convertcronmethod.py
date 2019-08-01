from package.croniter import croniter
from datetime import datetime, timedelta
from repository.select_holidays import *

def convertCronDate(recurrence='0 8 * * mon-fri 2019', duration = 3600):
  year = recurrence[-4:]
  recurrence = recurrence[:-4]
  #basedate: year month day heure minute

  base = datetime(int(year), 1, 1, 0, 0)

  #recurrence cron : min hour day month day_of_week
  iter = croniter(recurrence, base, day_or = False)
  my_list = []
  while(True):
      date = iter.get_next(datetime)
      if(date.year == 2020):
          break
      # print("Date Debut : ", date)
      datef = date + timedelta(seconds=duration)
      # print("Date Fin   : ", datef)
      tmp = (date,datef)
      my_list.append(tmp)

  return my_list


def convertCronDateNext(recurrence='0 8 * * mon-fri 2019', duration=3600, basedate=None):
  year = recurrence[-4:]
  recurrence = recurrence[:-4]
  #basedate: year month day heure minute
  if(basedate is None):
    return None 

  #recurrence cron : min hour day month day_of_week
  iter = croniter(recurrence, basedate, day_or=False)


  date = iter.get_next(datetime)
  

    


  # print("Date Debut : ", date)
  datef = date + timedelta(seconds=duration)
      # print("Date Fin   : ", datef)
  my_list = []
  tmp = (date, datef)
  my_list.append(tmp)

  return my_list 

def help(date,Holidaydates):
  for adate in Holidaydates:
    if(compareTwoDates(date,adate)):
      return True
   
  return False 


def convertCronDateADay(recurrence='0 8 * * mon-fri 2019', duration=3600, basedate=None):
  # year = recurrence[-4:]
  recurrence = recurrence[:-4]
  #basedate: year month day heure minute

  # base = datetime(int(year), 1, 1, 0, 0)
  base = basedate.replace(hour=0, minute=0, second=0)
  #recurrence cron : min hour day month day_of_week
  iter = croniter(recurrence, base, day_or=False)
  my_list = []

  date = iter.get_next(datetime)
  if(not compareTwoDates(date,base)):
      return None 
  # print("Date Debut : ", date)
  datef = date + timedelta(seconds=duration)
  # print("Date Fin   : ", datef)
  # s = "%Y-%m-%dT%H:%M:%SZ"
  # tmp = (date.strftime(s),
  #        datef.strftime(s))
  tmp = (date, datef)

  my_list.append(tmp)
  return my_list


def convertCronDateToday(recurrence='0 8 * * mon-fri 2019', duration=3600):
  # year = recurrence[-4:]
  recurrence = recurrence[:-4]
  #basedate: year month day heure minute

  # base = datetime(int(year), 1, 1, 0, 0)
  base = datetime.today().replace(
      hour=0, minute=0, second=0)
  #recurrence cron : min hour day month day_of_week
  iter = croniter(recurrence, base, day_or=False)
  my_list = []

  date = iter.get_next(datetime)
  if(not compareTwoDates(date,base)):
    return None 
  # print("Date Debut : ", date)
  datef = date + timedelta(seconds=duration)

  # print("Date Fin   : ", datef)
  # s = "%Y-%m-%dT%H:%M:%SZ"
  # tmp = (date.strftime(s),
  # #        datef.strftime(s))
  tmp = (date,datef)
  my_list.append(tmp)

  return my_list


def convertCronDateByPeriod(recurrence='0 8 * * mon-fri 2019', duration=3600, basedate=None, enddate= None):
  # year = recurrence[-4:]
  recurrence = recurrence[:-4]
  #basedate: year month day heure minute

  # base = datetime(int(year), 1, 1, 0, 0)
  base = basedate.replace(hour=0, minute=0, second=0)
  #recurrence cron : min hour day month day_of_week
  iter = croniter(recurrence, base, day_or=False)
  my_list = []
  while(True):
    date = iter.get_next(datetime)
  # if(not compareTwoDates(date, base)):
  #     return None
    datef = date + timedelta(seconds=duration)
    tmp = (date, datef)
    if(date > enddate):
      break
    my_list.append(tmp)
  # while(date <= enddate):
  #   date = iter.get_next(datetime)
  #   datef = date + timedelta(seconds=duration)
  #   tmp = (date, datef)
  #   my_list.append(tmp)
  return my_list


def convertCronDateAWeek(recurrence='0 8 * * mon-fri 2019', duration=3600, basedate=None):
  year = recurrence[-4:]
  recurrence = recurrence[:-4]
  #basedate: year month day heure minute

  # base = datetime(int(year), 1, 1, 0, 0)
  base = basedate - timedelta(days=basedate.weekday())
  base = base.replace(hours=0, minute=0, second=0)
  #recurrence cron : min hour day month day_of_week
  iter = croniter(recurrence, base, day_or=False)

  end = base + timedelta(days=6)
  end = end.replace(hour=23, minute=59, second=59)

  my_list = []
  date = iter.get_next(datetime)
  datef = date + timedelta(seconds=duration)
  # print("Date Fin   : ", datef)
  tmp = (date, datef)
  my_list.append(tmp)
  while(date <= end):
   date = iter.get_next(datetime)
   # print("Date Debut : ", date)
   datef = date + timedelta(seconds=duration)
   # print("Date Fin   : ", datef)
   tmp = (date, datef)
   my_list.append(tmp)

  return my_list


def convertCronDateNextHolidayAware(recurrence='0 8 * * mon-fri 2019', duration=3600, basedate=None,dateHolidays = None):
  year = recurrence[-4:]
  recurrence = recurrence[:-4]
  #basedate: year month day heure minute
  if(basedate is None):
    return None

  #recurrence cron : min hour day month day_of_week
  iter = croniter(recurrence, basedate, day_or=False)

  date = iter.get_next(datetime)
  while(help(date, dateHolidays)):
    date = iter.get_next(datetime)
  # print("Date Debut : ", date)
  datef = date + timedelta(seconds=duration)
  # print("Date Fin   : ", datef)
  my_list = []
  tmp = (date, datef)
  my_list.append(tmp)

  return my_list


def convertCronDateNoDuration(recurrence='0 8 * * mon-fri 2019'):
  year = recurrence[-4:]
  recurrence = recurrence[:-4]
  base = datetime(int(year), 1, 1, 0, 0)
  #min hour day month day_of_week
  iter = croniter(recurrence, base, day_or=False)
  my_list = []
  date = iter.get_next(datetime)
  return date


def compareTwoDates(firstdate: datetime, seconddate: datetime):
      if((firstdate.year == seconddate.year)
         and (firstdate.month == seconddate.month)
         and (firstdate.day == seconddate.day)):
        return True
      else:
        return False


if __name__ == "__main__":
    print(convertCronDateToday())
    # convertCronDate(duration = 7200)
    # convertCronDateNoDuration()
    # print(convertCronDateADay(recurrence='0 8 * * mon-fri 2019' , basedate=datetime(2019, 2, 4, 11, 30, 59)))
    # print(convertCronDateByPeriod(basedate=datetime(2019,7,26),enddate=datetime(2019,8,31)))
    # i = 0
    # for k in convertCronDateByPeriod(basedate=datetime(2019, 7, 26), enddate=datetime(2019, 8, 31)):
    #   print(k[0])
    #   i = i + 1
    # print(i)

