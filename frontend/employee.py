import datetime
from tkinter import*
from ttkbootstrap.constants import*
import ttkbootstrap as ttkb
from backend.employeebackend import*
from ttkbootstrap.tableview import Tableview
from ttkbootstrap.scrolled import *
from ttkbootstrap.toast import ToastNotification




def employee_frame(root,user):
    employee_pg_frame=ttkb.Frame(root,bootstyle='dark')
    employee_pg_frame.pack(padx=10,pady=10,expand=True,fil=BOTH)

    def issue_btn():
        employee_pg_frame.pack_forget()
        issue_frame(root,user)


    def return_issue_btn():
        employee_pg_frame.pack_forget()
        return_issue_frame(root,user)


    
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

    

    greeting_frame=ttkb.Frame(employee_pg_frame,bootstyle='dark')
    greeting_frame.pack(padx=5,pady=5,fill=X)

    
    employee_info_frame=ttkb.Labelframe(greeting_frame,bootstyle='success',text=greetings)
    employee_info_frame.pack(padx=20,fill=X)

    #id name doj
    employee_name_frame=ttkb.Frame(employee_info_frame)
    employee_name_frame.pack(side=LEFT,padx=80,pady=5)

    name_lb=ttkb.Label(employee_name_frame,text=user.getName(),font=('Helvetica',24),bootstyle='primary')
    name_lb.pack(padx=10,pady=5)

    employee_eid_doj_frame=ttkb.Frame(employee_info_frame)
    employee_eid_doj_frame.pack(padx=20,pady=5,side=RIGHT)

    eid_lb=ttkb.Label(employee_eid_doj_frame,text='EID   :%s'%user.getId(),font=('Helvetica',18),bootstyle='primary')
    eid_lb.pack(padx=10,pady=5)

    doj_lb=ttkb.Label(employee_eid_doj_frame,text='DOJ:%s'%user.getDoj(),font=('Helvetica',18),bootstyle='primary')
    doj_lb.pack(padx=10,pady=5)

    #seperator
    div_sep=ttkb.Separator(employee_pg_frame,bootstyle='secondary')
    div_sep.pack(fill=X,padx=25,pady=50)

    options_frame =ttkb.Labelframe(employee_pg_frame,text='MENU',bootstyle='success')
    options_frame.pack(fill=X,padx=15,pady=100)

    issue_bt=ttkb.Button(options_frame,text='ISSUE BOOK',bootstyle='secondary outline',command=issue_btn)
    issue_bt.pack(padx=150,pady=20,side=LEFT)

    return_issue_bt=ttkb.Button(options_frame,text='RETURN ISSUED BOOK',bootstyle='secondary outline',command=return_issue_btn)
    return_issue_bt.pack(padx=150,pady=20,side=RIGHT)










def issue_frame(root,user):
    issue_pg_frame =ttkb.Frame(root,bootstyle='dark')
    issue_pg_frame.pack(padx=5,pady=5,expand=TRUE,fill=BOTH)

    def return_btn():
        issue_pg_frame.pack_forget()
        employee_frame(root,user)


    

    def confirm_input_fx(mid,bid,eid):

        confirm_frame=ttkb.Labelframe(tcl_frame,text='CONFIRM NEW ISSUE',bootstyle='secondary')
        confirm_frame.pack(padx=10,pady=30,expand=TRUE,fill=BOTH)


        def submit_input_fx():
            
            make_new_issue(mid,bid,eid)

            toast = ToastNotification(title="FUTElibs toast message",message="THE ISSUE WAS SUCCESSFUL",duration=3000,bootstyle='success')
            toast.show_toast()

            return_btn()


        m1=ttkb.Label(confirm_frame,text='THE FOLLOWING ISSUE IS TO BE PLACED',font=('Helvetica',14),bootstyle='primary')
        m1.pack(padx=10,pady=10)

        eid_lb=ttkb.Label(confirm_frame,text='  EID: %s'%eid,font=('Helvetica',10),bootstyle='secondary')
        eid_lb.pack(padx=10,pady=5)

        mid_lb=ttkb.Label(confirm_frame,text='  MID: %s'%mid,font=('Helvetica',10),bootstyle='secondary')
        mid_lb.pack(padx=10,pady=5)

        bid_lb=ttkb.Label(confirm_frame,text='  BID: %s'%bid,font=('Helvetica',10),bootstyle='secondary')
        bid_lb.pack(padx=10,pady=5)

        submit_bt=ttkb.Button(confirm_frame,text='SUBMIT',bootstyle='secondary outline',command=submit_input_fx)
        submit_bt.pack(padx=10,pady=15)



    def bid_input_fx(mid,eid):
        

        def bid_ck_btn():
            do()


        bid_input_frame=ttkb.Labelframe(tcl_frame,text='BOOK INFO',bootstyle='secondary')
        bid_input_frame.pack(padx=10,pady=20,fill=X)

        bid_label=ttkb.Label(bid_input_frame,text='ENTER    BOOK BID',font=('Helvetica',10),bootstyle='secondary')
        bid_label.pack(padx=50,pady=5,side=LEFT)

        bid_ent=ttkb.Entry(bid_input_frame,font=('Helvetica',10),bootstyle='secondary')
        bid_ent.pack(side=LEFT,padx=10,pady=5)

        #customer data table
        b_coldata=['BID','BOOK','AUTHOR']
        b_rowdata=Get_book_table_data()
        
        b_table=Tableview(
            tcl_frame,
            coldata=b_coldata,
            rowdata=b_rowdata,
            paginated=True,
            searchable=True,
            autoalign=False,
            bootstyle='primary'
            )
        
        b_table.pack(padx=10,pady=10)


        bid_ck_bt =ttkb.Button(bid_input_frame,text='Check',bootstyle='info outline',command=bid_ck_btn)
        bid_ck_bt.pack(side=LEFT,padx=10,pady=5)






        def do():
            customer=check_bid(bid_ent.get())
            if customer!=None:
                b_table.pack_forget()
                bid_ck_bt.pack_forget()
                c_name_label=ttkb.Label(bid_input_frame,text='BOOOK : %s'%customer[1],font=('Helvetica',10),bootstyle='secondary')
                c_name_label.pack(padx=5,pady=5)
                
                confirm_input_fx(mid,bid_ent.get(),eid)

            else:
                toast = ToastNotification(title="FUTElibs toast message",message="THE BOOK IS UNAVAILABLE",duration=3000,bootstyle='danger')
                toast.show_toast()





    
    def mid_input_fx():


        
        def mid_ck_btn():
            do()



        mid_input_frame=ttkb.Labelframe(tcl_frame,text='CUSTOMER INFO',bootstyle='secondary')
        mid_input_frame.pack(padx=10,pady=20,fill=X)

        mid_label=ttkb.Label(mid_input_frame,text='ENTER CUSTOMER MID',font=('Helvetica',10),bootstyle='secondary')
        mid_label.pack(padx=50,pady=5,side=LEFT)

        mid_ent=ttkb.Entry(mid_input_frame,font=('Helvetica',10),bootstyle='secondary')
        mid_ent.pack(side=LEFT,padx=10,pady=5)

        #customer data table
        c_coldata=['MID','NAME']
        c_rowdata=Get_customer_table_data()
        
        c_table=Tableview(
            tcl_frame,
            coldata=c_coldata,
            rowdata=c_rowdata,
            paginated=True,
            searchable=True,
            autoalign=False,
            bootstyle='primary'
            )
        
        c_table.pack(padx=10,pady=10)


        mid_ck_bt =ttkb.Button(mid_input_frame,text='Check',bootstyle='info outline',command=mid_ck_btn)
        mid_ck_bt.pack(side=LEFT,padx=10,pady=5)




        def do():
            customer=check_mid(mid_ent.get())
            if customer!=None:
                c_table.pack_forget()
                mid_ck_bt.pack_forget()
                c_name_label=ttkb.Label(mid_input_frame,text='CUSTOMER NAME: %s'%customer[1],font=('Helvetica',10),bootstyle='secondary')
                c_name_label.pack(padx=5,pady=5)
                
                bid_input_fx(mid_ent.get(),user.getId())

            else:
                toast = ToastNotification(title="FUTElibs toast message",message="NO SUCH USER FOUND",duration=3000,bootstyle='danger')
                toast.show_toast()




    
    back_bt_container = ttkb.Labelframe(issue_pg_frame,text='RETURN',bootstyle='secondary')
    back_bt_container.pack(padx=1,pady=1,fill=X)

    back_bt=ttkb.Button(back_bt_container,text='<<<',bootstyle='secondary outline',command=return_btn)
    back_bt.pack(padx=5,pady=3,side=LEFT)


    tcl_frame=ScrolledFrame(issue_pg_frame,autohide=True,bootstyle='dark')
    tcl_frame.pack(padx=5,pady=5,fill=BOTH,expand=True)

    mid_input_fx()




    
        









"""return issue frame"""




def return_issue_frame(root,user):
    return_issue_pg_frame =ttkb.Frame(root,bootstyle='dark')
    return_issue_pg_frame.pack(padx=5,pady=5,expand=TRUE,fill=BOTH)

    def return_btn():
        return_issue_pg_frame.pack_forget()
        employee_frame(root,user)


    

    def confirm_input_fx(mid,bid,tid,fine):

        confirm_frame=ttkb.Labelframe(tcl_frame,text='CONFIRM RETURN ISSUE',bootstyle='secondary')
        confirm_frame.pack(padx=10,pady=30,expand=TRUE,fill=BOTH)


        def submit_input_fx():
            pass
            make_return_issue(bid,tid,fine)

            toast = ToastNotification(title="FUTElibs toast message",message="THE ISSUE WAS SUCCESSFUL",duration=3000,bootstyle='success')
            toast.show_toast()

            return_btn()


        m1=ttkb.Label(confirm_frame,text='THE FOLLOWING RETURN ISSUE IS TO BE PLACED',font=('Helvetica',14),bootstyle='primary')
        m1.pack(padx=10,pady=10)

        tid_lb=ttkb.Label(confirm_frame,text='  TID: %s'%tid,font=('Helvetica',10),bootstyle='secondary')
        tid_lb.pack(padx=10,pady=5)

        mid_lb=ttkb.Label(confirm_frame,text='  MID: %s'%mid,font=('Helvetica',10),bootstyle='secondary')
        mid_lb.pack(padx=10,pady=5)

        bid_lb=ttkb.Label(confirm_frame,text='  BID: %s'%bid,font=('Helvetica',10),bootstyle='secondary')
        bid_lb.pack(padx=10,pady=5)

        fine_lb=ttkb.Label(confirm_frame,text='  BE SURE TO COLLECT A FINE OF: [RS.%s] '%fine,font=('Helvetica',12),bootstyle='danger')
        fine_lb.pack(padx=10,pady=5)

        submit_bt=ttkb.Button(confirm_frame,text='SUBMIT',bootstyle='secondary outline',command=submit_input_fx)
        submit_bt.pack(padx=10,pady=15)



    def tid_input_fx(mid):
        

        def tid_ck_btn():
            do()


        tid_input_frame=ttkb.Labelframe(tcl_frame,text='ISSUE INFO',bootstyle='secondary')
        tid_input_frame.pack(padx=10,pady=20,fill=X)

        tid_label=ttkb.Label(tid_input_frame,text='ENTER    ISSUE TID',font=('Helvetica',10),bootstyle='secondary')
        tid_label.pack(padx=50,pady=5,side=LEFT)

        tid_ent=ttkb.Entry(tid_input_frame,font=('Helvetica',10),bootstyle='secondary')
        tid_ent.pack(side=LEFT,padx=10,pady=5)

        #customer data table
        t_coldata=['TID','BOOK BID','BOOK','FINE']
        t_rowdata=Get_issue_table_data(mid)
        
        t_table=Tableview(
            tcl_frame,
            coldata=t_coldata,
            rowdata=t_rowdata,
            paginated=True,
            searchable=True,
            autoalign=False,
            bootstyle='primary'
            )
        
        t_table.pack(padx=10,pady=10)


        tid_ck_bt =ttkb.Button(tid_input_frame,text='Check',bootstyle='info outline',command=tid_ck_btn)
        tid_ck_bt.pack(side=LEFT,padx=10,pady=5)






        def do():
            result=check_tid(tid_ent.get())
            if result!=None:
                t_table.pack_forget()
                tid_ck_bt.pack_forget()
                c_name_label=ttkb.Label(tid_input_frame,text='TID : %s'%result[0],font=('Helvetica',10),bootstyle='secondary')
                c_name_label.pack(padx=5,pady=5)
                
                confirm_input_fx(mid,result[0],tid_ent.get(),result[1])

            else:
                toast = ToastNotification(title="FUTElibs toast message",message="NO SUCH ISSUE FOUND",duration=3000,bootstyle='danger')
                toast.show_toast()





    
    def mid_input_fx():


        
        def mid_ck_btn():
            do()



        mid_input_frame=ttkb.Labelframe(tcl_frame,text='CUSTOMER INFO',bootstyle='secondary')
        mid_input_frame.pack(padx=10,pady=20,fill=X)

        mid_label=ttkb.Label(mid_input_frame,text='ENTER CUSTOMER MID',font=('Helvetica',10),bootstyle='secondary')
        mid_label.pack(padx=50,pady=5,side=LEFT)

        mid_ent=ttkb.Entry(mid_input_frame,font=('Helvetica',10),bootstyle='secondary')
        mid_ent.pack(side=LEFT,padx=10,pady=5)

        #customer data table
        c_coldata=['MID','NAME']
        c_rowdata=Get_customer_table_data()
        
        c_table=Tableview(
            tcl_frame,
            coldata=c_coldata,
            rowdata=c_rowdata,
            paginated=True,
            searchable=True,
            autoalign=False,
            bootstyle='primary'
            )
        
        c_table.pack(padx=10,pady=10)


        mid_ck_bt =ttkb.Button(mid_input_frame,text='Check',bootstyle='info outline',command=mid_ck_btn)
        mid_ck_bt.pack(side=LEFT,padx=10,pady=5)




        def do():
            customer=check_mid(mid_ent.get())
            if customer!=None:
                c_table.pack_forget()
                mid_ck_bt.pack_forget()
                c_name_label=ttkb.Label(mid_input_frame,text='CUSTOMER NAME: %s'%customer[1],font=('Helvetica',10),bootstyle='secondary')
                c_name_label.pack(padx=5,pady=5)
                
                tid_input_fx(mid_ent.get())

            else:
                toast = ToastNotification(title="FUTElibs toast message",message="NO SUCH USER FOUND",duration=3000,bootstyle='danger')
                toast.show_toast()





    
    back_bt_container = ttkb.Labelframe(return_issue_pg_frame,text='RETURN',bootstyle='secondary')
    back_bt_container.pack(padx=1,pady=1,fill=X)

    back_bt=ttkb.Button(back_bt_container,text='<<<',bootstyle='secondary outline',command=return_btn)
    back_bt.pack(padx=5,pady=3,side=LEFT)


    tcl_frame=ScrolledFrame(return_issue_pg_frame,autohide=True,bootstyle='dark')
    tcl_frame.pack(padx=5,pady=5,fill=BOTH,expand=True)

    mid_input_fx()