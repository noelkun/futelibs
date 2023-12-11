from tkinter import*
from ttkbootstrap.constants import*
from ttkbootstrap.scrolled import *
from ttkbootstrap.tableview import Tableview
import ttkbootstrap as ttkb
from backend.customerbackend import*
import datetime






def customer_frame(root,user):
    customer_pg_frame=ttkb.Frame(root,bootstyle='dark')
    customer_pg_frame.pack(padx=10,pady=10,fill=BOTH,expand=True)

    def greet():
        now = datetime.datetime.now()
        hour = now.hour

        if hour < 12:
            return "Good morning  "
        elif hour < 17:
            return "Good afternoon  "
        else:
            return "Good evening  "

    greetings='%s %s'%(greet(),user.getName())
    greetings=greetings.upper()

    

    greeting_frame=ttkb.Frame(customer_pg_frame,bootstyle='dark')
    greeting_frame.pack(padx=5,pady=5,fill=X)


    

    customer_info_frame=ttkb.Labelframe(greeting_frame,bootstyle='success',text=greetings)
    customer_info_frame.pack(padx=20,fill=X)

    #id name doj
    customer_name_frame=ttkb.Frame(customer_info_frame)
    customer_name_frame.pack(side=LEFT,padx=80,pady=5)

    name_lb=ttkb.Label(customer_name_frame,text=user.getName(),font=('Helvetica',24),bootstyle='primary')
    name_lb.pack(padx=10,pady=5)

    customer_mid_doj_frame=ttkb.Frame(customer_info_frame)
    customer_mid_doj_frame.pack(padx=20,pady=5,side=RIGHT)

    mid_lb=ttkb.Label(customer_mid_doj_frame,text='MID   :%s'%user.getId(),font=('Helvetica',18),bootstyle='primary')
    mid_lb.pack(padx=10,pady=5)

    doj_lb=ttkb.Label(customer_mid_doj_frame,text='DOJ:%s'%user.getDoj(),font=('Helvetica',18),bootstyle='primary')
    doj_lb.pack(padx=10,pady=5)

    #seperator
    div_sep=ttkb.Separator(customer_pg_frame,bootstyle='success')
    div_sep.pack(fill=X,padx=15,pady=20)

    #scrolledframe
    transaction_frame=ScrolledFrame(customer_pg_frame,autohide=True,bootstyle='dark')
    transaction_frame.pack(padx=5,pady=10,expand=True,fill=BOTH)

    pending_issue_frame=ttkb.Labelframe(transaction_frame,bootstyle='info',text='PENDING ISSUES')
    pending_issue_frame.pack(padx=15,pady=5,expand=True,fill=BOTH)

    returned_issue_frame=ttkb.Labelframe(transaction_frame,bootstyle='info',text='RETURNED ISSUES')
    returned_issue_frame.pack(padx=15,pady=5,expand=True,fill=BOTH)

    pt_coldata=['TID','ISSUE DATE','BOOK','DAYS LEFT FOR RETURN','DELAY (IN DAYS)','FINE PAYABLE']
    pt_rowdata=pending(user.getId())

    pending_table=Tableview(
        pending_issue_frame,
        coldata=pt_coldata,
        rowdata=pt_rowdata,
        paginated=True,
        searchable=True,
        autoalign=False,
        bootstyle='primary'
        )
    
    pending_table.pack(padx=5,pady=1)

    rt_coldata=['TID','ISSUE DATE','BOOK','RETURN DATE','DELAY','FINE PAID']
    rt_rowdata=returned(user.getId())

    returned_table=Tableview(
        returned_issue_frame,
        coldata=rt_coldata,
        rowdata=rt_rowdata,
        paginated=True,
        searchable=True,
        autoalign=False,
        bootstyle='primary'
    )
    returned_table.pack(padx=5, pady=1)