import package.psycopg2
import datetime 
from repository.configDB import config
from repository.connect import connect


def get_calendar(conn):
    """ query data from the calendar table """
    try:
        # invoke connection to bd method(stays open)
        # conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT calendar_id, name, description FROM calendar")
        rows = cur.fetchall()
  


    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    return rows

def get_acalendar(calendar_id: int, conn):
    """ query data from the calendar table """

    try:
        # invoke connection to bd method(stays open)
        # conn = connect()
        cur = conn.cursor()
        cur.execute("SELECT calendar_id, name, description FROM calendar WHERE calendar_id = %s"
                    , (calendar_id,))
        # print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    return row

if __name__ == '__main__':
        get_calendar()
