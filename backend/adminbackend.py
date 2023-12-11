from backend.database import*
import sys


def Get_book_table_data():
    conn=None

    sql='select bid, name,author from book where holder=0'
    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print('Error',sys.exc_info())

    finally:
        del sql, conn
        return result

def check_bid(bid):
    conn=None

    sql='select bid,name,author from book where bid=%s and holder=0'
    values=(bid,)
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
    

def remove_book(bid):
    conn=None

    sql='update book set holder=-1 where bid=%s'
    values=(bid,)
    
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
        


def add_book(bname,auth):
    conn=None

    sql='insert into book values(%s,%s,%s,0)'

    bid=maxi()[4]+1
    bid=str(bid)

    values=(bid,bname,auth)
    
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



"""employee dats"""


#function to give imployee table data
def Get_employee_table_data():
    conn=None

    sql='select eid,name,email from employee'

    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print('Error',sys.exc_info())
    
    finally:
        del sql, conn
        return result
 


def check_eid(eid):
    conn=None

    sql='select eid,name,email from employee where eid=%s'
    values=(eid)
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





def remove_employee(eid):
    conn=None

    sql='delete from employee where eid=%s'
    values=(eid,)
    
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




#function to check weteher the employee email already exists
def check_email(email):
    conn=None

    sql='select * from employee where email=%s'
    values=(email,)
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
 


#function to add employee to the database
def add_employee(name,email,passw):
    conn=None

    eid=maxi()[2]+1
    eid=str(eid)
    sql='insert into employee values(%s,%s,CURDATE(),%s,%s)'
    values=(eid,name,email,passw)

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
