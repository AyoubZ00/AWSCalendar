import psycopg2
from calendarServ.RepositoriesCalendar.configDB import config
from calendarServ.RepositoriesCalendar.connect import connect

def delete_calendar(calendar_id):
    """ delete calendar by calendar id """
    conn = None
    rows_deleted = 0
    try:
        conn = connect()
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM calendar WHERE calendar_id = %s", (calendar_id,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        print(rows_deleted)
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return rows_deleted


def remove_allcalendars():
    """ delete all calendars """
    conn = None
    rows_deleted = 0
    try:
        # invoke connection to bd method(stays open)
        conn = connect()
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM calendar")
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
        print(rows_deleted)
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted


if __name__ == "__main__":
    remove_allcalendars()
