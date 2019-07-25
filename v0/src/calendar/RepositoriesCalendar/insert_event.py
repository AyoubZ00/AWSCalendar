import psycopg2
from v0.src.calendar.RepositoriesCalendar.configDB import config
from v0.src.calendar.RepositoriesCalendar.connect import connect
 
def insert_event(
                 calendar_id, 
                 recurrence,
                 name = '' ,
                 description = '',
                 duration = 3600 
                 ):
    """ insert a new event into the event table """
    sql = """INSERT INTO event(calendar_id,recurrence,name,description,duration)
             VALUES(%s,%s,%s,%s,%s) RETURNING event_id;"""
    conn = None
    event_id = None
    try:
        conn = connect()
        cur = conn.cursor()
        cur.execute(sql, (calendar_id,recurrence,name,description,duration))
        # get the generated id back
        event_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return event_id


if __name__ == '__main__':
    print(insert_event(19, '0 8 22 * mon-fri 2019',"Trip 2", "Morning trip for bus 0004", 7200))
