from backend.database import Connect
import sys


def login(user_ent_dat,user):
    conn=None

    if user=='admin':
        sql="""SELECT * FROM admin WHERE email=%s AND pass=%s"""
    elif user=='employee':
        sql="""SELECT * FROM employee WHERE email=%s AND pass=%s"""
    elif user=='member':
        sql="""SELECT * FROM members WHERE email=%s AND pass=%s"""
        
    values=(user_ent_dat.getEmail(), user_ent_dat.getPassword())
    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        result=cursor.fetchone()
        cursor.close()
        conn.close()

    except:
        print('Error',sys.exc_info())

    finally:
        del values, sql, conn
        return result