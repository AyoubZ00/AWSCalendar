from configparser import ConfigParser
import os
 
def config(filename='RepositoriesCalendar/database.ini'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    # db = {}
    # if parser.has_section(section):
    #     params = parser.items(section)
    #     for param in params:
    #         db[param[0]] = param[1]
    db = {}
    params = parser.items('db')
    for param in params:
        db[param[0]] = param[1]
        # print(db)
    params = {}
    # print(os.getenv(db['db_host'], 'localhost'))
    # print(db['db_name'])
    # print(os.getenv(db['db_username'], 'postgres'))
    # print(os.getenv(db['db_password'], 'root'))
    params['host'] = os.getenv(db['db_host'], 'localhost')
    params['database'] = db['db_name']
    params['user'] = os.getenv(db['db_username'], 'postgres')
    params['password']=os.getenv(db['db_password'], 'root')
    # print(db)
    # else:
    #     raise Exception('Section {0} not found in the {1} file'.format(section, filename))
 
    return params

if __name__ == "__main__":
    config()
