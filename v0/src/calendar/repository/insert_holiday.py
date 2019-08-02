import package.psycopg2
from repository.configDB import config
from repository.connect import connect
def insert_holiday(
                 recurrence,
                 name = '' ,
                 description = '',
                 ):
    """ insert a new holiday into the holidays table """
    sql = """INSERT INTO holidays(recurrence,name,description)
             VALUES(%s,%s,%s) RETURNING holiday_id;"""
    conn = None
    holiday_id = None  
    try:
        
        conn = connect()
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (recurrence,name,description))
        # get the generated id back
        holiday_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, package.psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return holiday_id

  #min hour day month day_of_week
if __name__ == '__main__':
    # print(insert_holiday('0 0 * * sat-sun 2019',"Weekend", "You know, Weekends"))
    # print(insert_holiday('0 0 30 7 * 2019', "Throne Day",
    #                      "Celebrate Ascension of Moroccan KingTo the Throne"))
    print(insert_holiday('0 0 30 7 * 2019', "Throne Day", "A Holiday"))
