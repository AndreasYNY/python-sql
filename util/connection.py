import pymysql.cursors

def conn():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="fXRc478R",
        database="testdb",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True
    )
    return connection