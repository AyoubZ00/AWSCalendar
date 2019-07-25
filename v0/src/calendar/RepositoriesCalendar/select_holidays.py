import psycopg2
from v0.src.calendar.RepositoriesCalendar.configDB import config
from v0.src.calendar.RepositoriesCalendar.connect import connect
def get_holidays(conn):
    """ query data from the holidays table """
    # conn = None
    try:
        # invoke connection to bd method(stays open)
        # conn = connect()
        cur = conn.cursor()
        cur.execute("""SELECT holiday_id, recurrence, name, description
            FROM holidays""")
        print("The number of parts: ", cur.rowcount)
        rows = cur.fetchall()
 
       
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    return rows

if __name__ == '__main__':
        get_holidays()
