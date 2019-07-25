from croniter import croniter
from datetime import datetime, timedelta


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
    print(convertCronDate(duration = 7200))
    # convertCronDateNoDuration()
    # compareTwoDates()
