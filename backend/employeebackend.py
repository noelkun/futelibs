from backend.database import*
import sys



'''make new issues functions'''

def Get_customer_table_data(): 
    conn=None

    sql='select mid, name from members'
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


    
def check_mid(mid):
    conn=None

    sql='select mid,name from members where mid=%s'
    values=(mid,)
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



def make_new_issue(mid,bid,eid):
    conn=None

    sql1='update book set holder=%s where bid=%s'
    values1=(mid,bid)

    tid=maxi()
    tid=tid[3]
    tid=tid+1
    tid=str(tid)

    

    sql2="insert into raw_tr values(%s,%s,%s,%s,CURDATE(),'pending',NULL,NULL)"
    values2=(tid,mid,bid,eid)


    
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql1, values1)
        cursor.execute(sql2, values2)
        conn.commit()
        cursor.close()
        conn.close()

    except:
        print('Error',sys.exc_info())

    finally:
        del values1,values2, sql1,sql2, conn


'''return issue functions'''


def Get_issue_table_data(mid):
    conn=None

    sql='select raw_tr.tid,raw_tr.bid,pending_v.name,pending_v.fine_payable from raw_tr,pending_v where raw_tr.mid=%s and raw_tr.tid=pending_v.tid '
    values=(mid,)

    result=None
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql,values)
        result=cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print('Error',sys.exc_info())

    finally:
        del sql, conn,values
        return result



def check_tid(tid):
    conn=None

    sql='select raw_tr.bid,pending_v.fine_payable from raw_tr,pending_v where raw_tr.tid=pending_v.tid and raw_tr.tid=%s'
    values=(tid,)
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




def make_return_issue(bid,tid,fine):
    conn=None

    sql1='update book set holder=0 where bid=%s'
    values1=(bid,)

    sql2="update raw_tr set status='returned' where tid=%s"
    values2=(tid,)

    sql3="update raw_tr set re_date=CURDATE() where tid=%s"
    values3=(tid,)

    sql4="update raw_tr set fine_paid=%s where tid=%s"
    values4=(fine,tid)

    
    try:
        conn=Connect()
        cursor=conn.cursor()
        cursor.execute(sql1, values1)
        cursor.execute(sql2, values2)
        cursor.execute(sql3, values3)
        cursor.execute(sql4, values4)
        conn.commit()
        cursor.close()
        conn.close()

    except:
        print('Error',sys.exc_info())

    finally:
        del values1,values2,values3,values4, sql1,sql2,sql3,sql4, conn