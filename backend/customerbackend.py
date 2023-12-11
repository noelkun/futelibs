from backend.database import Connect
import sys

def pending(id):
    conn=None
    sql="""SELECT tid,issue_date,name,days_left,delay,fine_payable FROM pending_v WHERE mid=%s"""
    values=(id,)
    result=None

    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print('Error',sys.exc_info())

    finally:
        del values, sql, conn
        return result
    

def returned(id):
    conn=None
    sql="""SELECT tid,issue_date,name,re_date,delay,fine_paid FROM returned_v WHERE mid=%s"""
    values=(id,)
    result=None
    
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql, values)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print('Error',sys.exc_info())

    finally:
        del values, sql, conn
        return result