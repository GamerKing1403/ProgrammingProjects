import mysqlx

# Connect to server on localhost
session = mysqlx.get_session({
    'host': '127.0.0.1',
    'port': 33060,
    'user': 'root',
    'password': 'tushki2003'
})

schema = session.get_default_schema()

cursor = session  

