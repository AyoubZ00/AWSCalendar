import package.psycopg2
from repository.configDB import config
from repository.connect import connect

def get_event(calendar_id,conn):
    """ query data from the event table """

    # invoke connection to bd method(stays open)
    try:
        # conn = connect()
        cur = conn.cursor()
        queryline = """SELECT event_id, recurrence, name, description, calendar_id, duration
            FROM event WHERE calendar_id = %s"""
        cur.execute(queryline,(calendar_id,))
        rows = cur.fetchall()
        cur.close()
    except (Exception, package.psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    return rows

def get_allevent(conn):
    """ query data from the event table """

    try:
        cur = conn.cursor()
        queryline = """SELECT event_id, recurrence, name, description, calendar_id, duration
            FROM event """
        cur.execute(queryline)
        rows = cur.fetchall()

    except (Exception, package.psycopg2.DatabaseError) as error:
        print(error)
    # finally:
    #     if conn is not None:
    #         conn.close()
    return rows


if __name__ == '__main__':
       get_event(12)
