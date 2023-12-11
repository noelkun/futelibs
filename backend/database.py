import mysql.connector
import sys

"""
Host: sql12.freesqldatabase.com
Database name: sql12669532
Database user: sql12669532
Database password: wlIArNGzxs
Port number: 3306
"""

def Connect():
    conn=None
    try:
        conn=mysql.connector.Connect(
            host='sql12.freesqldatabase.com',
            username='sql12669532',
            password='wlIArNGzxs',
            database='sql12669532'
        )


    except:
        print('Error', sys.exc_info())

    finally:
        return conn
    

def maxi():
    conn=None

    sql='select * from maxi'
    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchone()
        cursor.close()
        conn.close()

    except:
        print('Error',sys.exc_info())

    finally:
        del sql, conn
        return result