from backend.database import*
import sys


#function to check weteher the employee email already exists
def check_email(email,user):
    conn=None

    sql='select * from %s where email=%s'
    values=(user,email)
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



def add_user(name,email,passw,user):
    conn=None

    uid=None

    if user=='member':
        uid=maxi()[1]+1
        uid=str(uid)
        sql='insert into members values(%s,%s,CURDATE(),%s,%s)'
    elif user=='admin':
        uid=maxi()[0]+1
        uid=str(uid)
        sql='insert into admin values(%s,%s,CURDATE(),%s,%s)'


    values=(uid,name,email,passw)

    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

    except:
        print('Error',sys.exc_info())
    
    finally:
        del values, sql, conn
