import psycopg2
from src.calendarServ.RepositoriesCalendar.configDB import config
from src.calendarServ.RepositoriesCalendar.connect import connect
def delete_holiday(holiday_id):
    """ delete holiday by holiday id """
    conn = None
    rows_deleted = 0
    try:
        # invoke connection to bd method(stays open)
        conn = connect()
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM holidays WHERE holiday_id = %s", (holiday_id,))
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
    return rows_deleted


def remove_allholidays():
    """ delete all holidays """
    conn = None
    rows_deleted = 0
    try:
        # read database configuration
        params = config()
        # connect to the PostgreSQL database
        conn = psycopg2.connect(**params)
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute("DELETE FROM holidays")
        # get the number of updated rows
        rows_deleted = cur.rowcount
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return rows_deleted


if __name__ == "__main__":
    remove_allholidays()
