import pymysql
import pymysql.cursors

def get_db():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='1234',
        database='fid',
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection