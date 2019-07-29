import psycopg2
from calendarServ.RepositoriesCalendar.configDB import config
from calendarServ.RepositoriesCalendar.connect import connect
 
def insert_calendar(name = '' , calendar_description = ''):
    """ insert a new calendar into the calendar table """
    sql = """INSERT INTO calendar(name,description)
             VALUES(%s,%s) RETURNING calendar_id;"""
    conn = None
    calendar_id = None
    try:
        conn = connect()
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (name,calendar_description))
        # get the generated id back
        calendar_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return calendar_id


if __name__ == '__main__':
   print(insert_calendar("Autumn calendar",
                      "Calendar for the Leaves to wither and fall. A somewhat malencholic season."))
   print(insert_calendar("Summer calendar",
                      "Calendar for the fun activities which you unfortunately won't be able to participate in because you're an adult now"))
   print(insert_calendar("Winter calendar",
                      "Calendar for the chilliest season of the year. Get your coat on"))
   print(insert_calendar("Spring calendar",
                      "Calendar for the best season of the year. S-P-R-I-N-G "))
