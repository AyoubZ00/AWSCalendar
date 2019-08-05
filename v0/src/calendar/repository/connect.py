import package.psycopg2
from repository.configDB import config

def connect():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = package.psycopg2.connect(**params)

        return conn
    except (Exception, package.psycopg2.DatabaseError) as error:
        print(error)

if __name__ == "__main__":
    connect()
