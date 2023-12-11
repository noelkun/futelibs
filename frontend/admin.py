import datetime
from tkinter import*
from ttkbootstrap.constants import*
import ttkbootstrap as ttkb
from backend.customerbackend import*
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.scrolled import *
from ttkbootstrap.tableview import Tableview
from backend.adminbackend import*







def admin_frame(root,user):

    
    admin_pg_frame=ttkb.Frame(root,bootstyle='dark')
    admin_pg_frame.pack(padx=10,pady=10,expand=True,fil=BOTH)

    def add_e_btn():
        admin_pg_frame.pack_forget()
        add_e_frame(root,user)

    def add_b_btn():
        admin_pg_frame.pack_forget()
        add_b_frame(root,user)

    def remove_b_btn():
        admin_pg_frame.pack_forget()
        remove_b_frame(root,user)

    def remove_e_btn():
        admin_pg_frame.pack_forget()
        remove_e_frame(root,user)



        
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

    

    greeting_frame=ttkb.Frame(admin_pg_frame,bootstyle='dark')
    greeting_frame.pack(padx=5,pady=5,fill=X)

    
    admin_info_frame=ttkb.Labelframe(greeting_frame,bootstyle='success',text=greetings)
    admin_info_frame.pack(padx=20,fill=X)

    #id name doj
    admin_name_frame=ttkb.Frame(admin_info_frame)
    admin_name_frame.pack(side=LEFT,padx=80,pady=5)

    name_lb=ttkb.Label(admin_name_frame,text=user.getName(),font=('Helvetica',24),bootstyle='primary')
    name_lb.pack(padx=10,pady=5)

    admin_eid_doj_frame=ttkb.Frame(admin_info_frame)
    admin_eid_doj_frame.pack(padx=20,pady=5,side=RIGHT)

    eid_lb=ttkb.Label(admin_eid_doj_frame,text='AID   :%s'%user.getId(),font=('Helvetica',18),bootstyle='primary')
    eid_lb.pack(padx=10,pady=5)

    doj_lb=ttkb.Label(admin_eid_doj_frame,text='DOJ:%s'%user.getDoj(),font=('Helvetica',18),bootstyle='primary')
    doj_lb.pack(padx=10,pady=5)


    def c():
        pass


    #seperator
    div_sep=ttkb.Separator(admin_pg_frame,bootstyle='secondary')
    div_sep.pack(fill=X,padx=25,pady=50)

    options_frame =ttkb.Labelframe(admin_pg_frame,text='MENU',bootstyle='success')
    options_frame.pack(fill=X,padx=15,pady=100)

    add_b_bt=ttkb.Button(options_frame,text='ADD BOOK',bootstyle='secondary outline',command=add_b_btn)
    add_b_bt.pack(padx=90,pady=20,side=LEFT)

    

    remove_b_bt=ttkb.Button(options_frame,text='REMOVE BOOK',bootstyle='secondary outline',command=remove_b_btn)
    remove_b_bt.pack(padx=90,pady=20,side=LEFT)

    add_e_bt=ttkb.Button(options_frame,text='ADD EMPLOYEE',bootstyle='secondary outline',command=add_e_btn)
    add_e_bt.pack(padx=90,pady=20,side=LEFT)

    remove_e_bt=ttkb.Button(options_frame,text='REMOVE EMPLOYEE',bootstyle='secondary outline',command=remove_e_btn)
    remove_e_bt.pack(padx=90,pady=20,side=LEFT)






















#function to add employee
def add_e_frame(root,user):
    add_e_pg_frame =ttkb.Frame(root,bootstyle='dark')
    add_e_pg_frame.pack(padx=5,pady=5,expand=TRUE,fill=BOTH)




    def return_btn():
        add_e_pg_frame.pack_forget()
        admin_frame(root,user)




    def confirm_input_fx(ename,email,password):

        confirm_frame=ttkb.Labelframe(tcl_frame,text='CONFIRM EMPLOYEE ADDITION QUERY',bootstyle='secondary')
        confirm_frame.pack(padx=10,pady=30,expand=TRUE,fill=BOTH)


        def submit_input_fx():
            add_employee(ename,email,password)
            toast = ToastNotification(title="FUTElibs toast message",message="THE QUERY WAS SUCCESSFUL",duration=3000,bootstyle='primary')
            toast.show_toast()

            return_btn()

        m1=ttkb.Label(confirm_frame,text='THE FOLLOWING EMPLOYEE IS TO BE ADDED',font=('Helvetica',14),bootstyle='primary')
        m1.pack(padx=10,pady=10)

        ename_lb=ttkb.Label(confirm_frame,text='  NAME: %s'%ename,font=('Helvetica',10),bootstyle='secondary')
        ename_lb.pack(padx=10,pady=10)

        email_lb=ttkb.Label(confirm_frame,text='  EMAIL: %s'%email,font=('Helvetica',10),bootstyle='secondary')
        email_lb.pack(padx=10,pady=10)

        submit_bt=ttkb.Button(confirm_frame,text='SUBMIT',bootstyle='secondary outline',command=submit_input_fx)
        submit_bt.pack(padx=10,pady=10)



    

    def einfo_input_fx():

        def confirm_btn():

            result=check_email(email_ent.get())


            if var_ename.get()=='':
                toast = ToastNotification(title="FUTElibs toast message",message="EMPLOYEE NAME CANNOT BE EMPTY",duration=3000,bootstyle='danger')
                toast.show_toast()
            elif var_email.get()=='':
                toast = ToastNotification(title="FUTElibs toast message",message="EMPLOYEE EMAIL CANNOT BE EMPTY",duration=3000,bootstyle='danger')
                toast.show_toast()
            elif var_password.get()=='':
                toast = ToastNotification(title="FUTElibs toast message",message="EMPLOYEE PASSWORD CANNOT BE EMPTY",duration=3000,bootstyle='danger')
                toast.show_toast()
            elif result:
                toast = ToastNotification(title="FUTElibs toast message",message="EMPLOYEE ALREADY EXISTS",duration=3000,bootstyle='danger')
                toast.show_toast()
            else:
                do()




        einfo_input_frame=ttkb.Labelframe(tcl_frame,text='EMPLOYEE INFO',bootstyle='secondary')
        einfo_input_frame.pack(padx=10,pady=20,fill=X)

        ename_input_frame=ttkb.Labelframe(einfo_input_frame,text='EMPLOYEE NAME',bootstyle='secondary')
        ename_input_frame.pack(padx=10,pady=20,fill=X)






        ename_label=ttkb.Label(ename_input_frame,text='NAME:',font=('Helvetica',10),bootstyle='secondary')
        ename_label.pack(padx=10,pady=5,side=LEFT)

        #limiting the input field for employee name
        var_ename=ttk.StringVar()

        max_len_ename = 25
        def on_write_ename(*args):
            s = var_ename.get()
            if len(s) > max_len_ename:
                var_ename.set(s[:max_len_ename])

        var_ename.trace('w', on_write_ename)

        ename_ent=ttkb.Entry(ename_input_frame,textvariable=var_ename,font=('Helvetica',10),bootstyle='secondary')
        ename_ent.pack(padx=10,pady=5,side=LEFT)




        email_input_frame=ttkb.Labelframe(einfo_input_frame,text='EMPLOYEE EMAIL',bootstyle='secondary')
        email_input_frame.pack(padx=10,pady=20,fill=X)

        email_label=ttkb.Label(email_input_frame,text='EMAIL:',font=('Helvetica',10),bootstyle='secondary')
        email_label.pack(padx=10,pady=5,side=LEFT)

        #limiting the input field for employee email
        var_email=ttk.StringVar()

        max_len_email = 25
        def on_write_email(*args):
            s = var_email.get()
            if len(s) > max_len_email:
                var_email.set(s[:max_len_email])

        var_email.trace('w', on_write_email)

        email_ent=ttkb.Entry(email_input_frame,textvariable=var_email,font=('Helvetica',10),bootstyle='secondary')
        email_ent.pack(padx=10,pady=5,side=LEFT)

        pass_input_frame=ttkb.Labelframe(einfo_input_frame,text='EMPLOYEE PASSWORD',bootstyle='secondary')
        pass_input_frame.pack(padx=10,pady=20,fill=X)

        pass_label=ttkb.Label(pass_input_frame,text='PASSWORD:',font=('Helvetica',10),bootstyle='secondary')
        pass_label.pack(padx=10,pady=5,side=LEFT)

        #limiting the input field for employee password
        var_password=ttk.StringVar()

        max_len_pass = 20
        def on_write_pass(*args):
            s = var_password.get()
            if len(s) > max_len_pass:
                var_password.set(s[:max_len_pass])

        var_password.trace('w', on_write_pass)

        pass_ent=ttkb.Entry(pass_input_frame,textvariable=var_password,font=('Helvetica',10),bootstyle='secondary')
        pass_ent.pack(padx=10,pady=5,side=LEFT)

        enifo_cn_bt=ttkb.Button(einfo_input_frame,text='CONFIRM',bootstyle='success',command=confirm_btn)
        enifo_cn_bt.pack(padx=10,pady=20,side=BOTTOM)

        def do():
            confirm_input_fx(ename_ent.get(),email_ent.get(),pass_ent.get())



    

    back_bt_container = ttkb.Labelframe(add_e_pg_frame,text='RETURN',bootstyle='secondary')
    back_bt_container.pack(padx=1,pady=1,fill=X)

    back_bt=ttkb.Button(back_bt_container,text='<<<',bootstyle='secondary outline',command=return_btn)
    back_bt.pack(padx=5,pady=3,side=LEFT)

    tcl_frame=ScrolledFrame(add_e_pg_frame,autohide=True,bootstyle='dark')
    tcl_frame.pack(padx=5,pady=5,fill=BOTH,expand=True)


    einfo_input_fx()























def remove_e_frame(root,user):
    remove_e_pg_frame =ttkb.Frame(root,bootstyle='dark')
    remove_e_pg_frame.pack(padx=5,pady=5,expand=TRUE,fill=BOTH)



    def return_btn():
        remove_e_pg_frame.pack_forget()
        admin_frame(root,user)




    def confirm_input_fx(eid,ename,email):

        confirm_frame=ttkb.Labelframe(tcl_frame,text='CONFIRM EMPLOYEE REMOVAL QUERY',bootstyle='secondary')
        confirm_frame.pack(padx=10,pady=30,expand=TRUE,fill=BOTH)



        def submit_input_fx():
            
            remove_employee(eid)

            toast = ToastNotification(title="FUTElibs toast message",message="THE QUERY WAS SUCCESSFUL",duration=3000,bootstyle='primary')
            toast.show_toast()

            return_btn()


        m1=ttkb.Label(confirm_frame,text='THE FOLLOWING EMPLOYEE IS TO BE REMOVED',font=('Helvetica',14),bootstyle='primary')
        m1.pack(padx=10,pady=5,side=TOP)

        eid_lb=ttkb.Label(confirm_frame,text='  EID: %s'%eid,font=('Helvetica',10),bootstyle='secondary')
        eid_lb.pack(padx=10,pady=5,side=TOP)

        ename_lb=ttkb.Label(confirm_frame,text='  NAME: %s'%ename,font=('Helvetica',10),bootstyle='secondary')
        ename_lb.pack(padx=10,pady=5,side=TOP)

        email_lb=ttkb.Label(confirm_frame,text='  EMAIL: %s'%email,font=('Helvetica',10),bootstyle='secondary')
        email_lb.pack(padx=10,pady=5,side=TOP)

        submit_bt=ttkb.Button(confirm_frame,text='SUBMIT',bootstyle='success',command=submit_input_fx)
        submit_bt.pack(padx=10,pady=5,side=TOP)





    def eid_input_fx():



        def bid_ck_btn():
            do()
        


        eid_input_frame=ttkb.Labelframe(tcl_frame,text='EMPLOYEE ID',bootstyle='secondary')
        eid_input_frame.pack(padx=10,pady=20,fill=X)

        eid_label=ttkb.Label(eid_input_frame,text='ENTER EMPLOYEE ID:',font=('Helvetica',10),bootstyle='secondary')
        eid_label.pack(padx=10,pady=5,side=LEFT)

        eid_ent=ttkb.Entry(eid_input_frame,font=('Helvetica',10),bootstyle='secondary')
        eid_ent.pack(padx=10,pady=5,side=LEFT)



        e_rowdata=Get_employee_table_data()
        e_coldata=['EID','NAME','EMAIL']

        e_table=Tableview(
            tcl_frame,
            rowdata=e_rowdata,
            coldata=e_coldata,
            paginated=True,
            searchable=True,
            autoalign=False,
            bootstyle='primary'
        )
    
        e_table.pack(padx=10,pady=10)
        
        eid_ck_bt=ttkb.Button(eid_input_frame,text='CHECK',bootstyle='info outline',command=bid_ck_btn)
        eid_ck_bt.pack(padx=10,pady=5,side=LEFT)


        def do():
            employee=check_eid(eid_ent.get())
            if employee!=None:
                e_table.pack_forget()
                eid_ck_bt.pack_forget()
                confirm_input_fx(employee[0],employee[1],employee[2])

            else:
                toast = ToastNotification(title="FUTElibs toast message",message="THE EMPLOYEE DOES NOT EXIST",duration=3000,bootstyle='danger')
                toast.show_toast()




    back_bt_container = ttkb.Labelframe(remove_e_pg_frame,text='RETURN',bootstyle='secondary')
    back_bt_container.pack(padx=1,pady=1,fill=X)

    back_bt=ttkb.Button(back_bt_container,text='<<<',bootstyle='secondary outline',command=return_btn)
    back_bt.pack(padx=5,pady=3,side=LEFT)

    tcl_frame=ScrolledFrame(remove_e_pg_frame,autohide=True,bootstyle='dark')
    tcl_frame.pack(padx=5,pady=5,fill=BOTH,expand=True)


    eid_input_fx()






















def add_b_frame(root,user):
    add_b_pg_frame =ttkb.Frame(root,bootstyle='dark')
    add_b_pg_frame.pack(padx=5,pady=5,expand=TRUE,fill=BOTH)

    def return_btn():
        add_b_pg_frame.pack_forget()
        admin_frame(root,user)




    

    def confirm_input_fx(bname,author):

        confirm_frame=ttkb.Labelframe(tcl_frame,text='CONFIRM BOOK  ADD QUERY',bootstyle='secondary')
        confirm_frame.pack(padx=10,pady=30,expand=TRUE,fill=BOTH)


        def submit_input_fx():
            
            add_book(bname,author)

            toast = ToastNotification(title="FUTElibs toast message",message="THE QUERY WAS SUCCESSFUL",duration=3000,bootstyle='success')
            toast.show_toast()

            return_btn()


        m1=ttkb.Label(confirm_frame,text='THE FOLLOWING BOOK IS TO BE ADDED',font=('Helvetica',14),bootstyle='primary')
        m1.pack(padx=10,pady=10)

        bname_lb=ttkb.Label(confirm_frame,text='  BOOK: %s'%bname,font=('Helvetica',10),bootstyle='secondary')
        bname_lb.pack(padx=10,pady=5)

        author_lb=ttkb.Label(confirm_frame,text='  AUTHOR: %s'%author,font=('Helvetica',10),bootstyle='secondary')
        author_lb.pack(padx=10,pady=5)

        submit_bt=ttkb.Button(confirm_frame,text='SUBMIT',bootstyle='secondary outline',command=submit_input_fx)
        submit_bt.pack(padx=10,pady=15)



    


    



    def binfo_input_fx():

        def confirm_btn():
            if var_book.get()=='' or var_author.get()=='':
                toast = ToastNotification(title="FUTElibs toast message",message="PLEASE ENTER BOOK NAME AND AUTHOR NAME",duration=3000,bootstyle='danger')
                toast.show_toast()
            else:
                do()

        
        binfo_input_frame=ttkb.Labelframe(tcl_frame,text='BOOK INFO',bootstyle='secondary')
        binfo_input_frame.pack(padx=10,pady=20,fill=X)

        bname_input_frame=ttkb.Labelframe(binfo_input_frame,text='BOOK NAME',bootstyle='secondary')
        bname_input_frame.pack(padx=10,pady=20,fill=X)



        



        bname_label=ttkb.Label(bname_input_frame,text='ENTER    BOOK  NAME',font=('Helvetica',10),bootstyle='secondary')
        bname_label.pack(padx=50,pady=5,side=LEFT)


        #liimiting the input field for book name
        var_book=ttk.StringVar()
        
        max_len = 50
        def on_write_book(*args):
            s = var_book.get()
            if len(s) > max_len:
                var_book.set(s[:max_len])

        var_book.trace('w', on_write_book)

        bname_ent=ttkb.Entry(bname_input_frame,font=('Helvetica',10),bootstyle='secondary',textvariable=var_book,width=50)
        bname_ent.pack(side=LEFT,padx=10,pady=5)





        author_input_frame=ttkb.Labelframe(binfo_input_frame,text='AUTHOR INFO',bootstyle='secondary')
        author_input_frame.pack(padx=10,pady=20,fill=X)

        author_label=ttkb.Label(author_input_frame,text='ENTER AUTHOR NAME',font=('Helvetica',10),bootstyle='secondary')
        author_label.pack(padx=50,pady=5,side=LEFT)

        #limiting the input field for author name
        var_author=ttk.StringVar()

        def on_write_author(*args):
            s = var_author.get()
            if len(s) > max_len:
                var_author.set(s[:max_len])

        var_author.trace('w', on_write_author)

        author_ent=ttkb.Entry(author_input_frame,font=('Helvetica',10),bootstyle='secondary',textvariable=var_author,width=50)
        author_ent.pack(side=LEFT,padx=10,pady=5)

        binfo_cn_bt =ttkb.Button(binfo_input_frame,text='CONFIRM',bootstyle='info outline',command=confirm_btn)
        binfo_cn_bt.pack(padx=10,pady=10)

        def do():
            confirm_input_fx(bname_ent.get(),author_ent.get())








    back_bt_container = ttkb.Labelframe(add_b_pg_frame,text='RETURN',bootstyle='secondary')
    back_bt_container.pack(padx=1,pady=1,fill=X)

    back_bt=ttkb.Button(back_bt_container,text='<<<',bootstyle='secondary outline',command=return_btn)
    back_bt.pack(padx=5,pady=3,side=LEFT)

       
    tcl_frame=ScrolledFrame(add_b_pg_frame,autohide=True,bootstyle='dark')
    tcl_frame.pack(padx=5,pady=5,fill=BOTH,expand=True)

    binfo_input_fx()










def remove_b_frame(root,user):
    remove_b_pg_frame =ttkb.Frame(root,bootstyle='dark')
    remove_b_pg_frame.pack(padx=5,pady=5,expand=TRUE,fill=BOTH)



    def return_btn():
        remove_b_pg_frame.pack_forget()
        admin_frame(root,user)

    



    def confirm_input_fx(bid,bname,author):

        confirm_frame=ttkb.Labelframe(tcl_frame,text='CONFIRM BOOK REMOVAL QUERY',bootstyle='secondary')
        confirm_frame.pack(padx=10,pady=30,expand=TRUE,fill=BOTH)


        def submit_input_fx():
            
            remove_book(bid)

            toast = ToastNotification(title="FUTElibs toast message",message="THE QUERY WAS SUCCESSFUL",duration=3000,bootstyle='success')
            toast.show_toast()

            return_btn()


        m1=ttkb.Label(confirm_frame,text='THE FOLLOWING BOOK IS TO BE REMOVED',font=('Helvetica',14),bootstyle='primary')
        m1.pack(padx=10,pady=10)

        bid_lb=ttkb.Label(confirm_frame,text='  BID: %s'%bid,font=('Helvetica',10),bootstyle='secondary')
        bid_lb.pack(padx=10,pady=5)

        bname_lb=ttkb.Label(confirm_frame,text='  BOOK: %s'%bname,font=('Helvetica',10),bootstyle='secondary')
        bname_lb.pack(padx=10,pady=5)

        author_lb=ttkb.Label(confirm_frame,text='  AUTHOR: %s'%author,font=('Helvetica',10),bootstyle='secondary')
        author_lb.pack(padx=10,pady=5)

        submit_bt=ttkb.Button(confirm_frame,text='SUBMIT',bootstyle='secondary outline',command=submit_input_fx)
        submit_bt.pack(padx=10,pady=15)






    def bid_input_fx():
        

        def bid_ck_btn():
            do()


        bid_input_frame=ttkb.Labelframe(tcl_frame,text='BOOK INFO',bootstyle='secondary')
        bid_input_frame.pack(padx=10,pady=20,fill=X)

        bid_label=ttkb.Label(bid_input_frame,text='ENTER    BOOK BID',font=('Helvetica',10),bootstyle='secondary')
        bid_label.pack(padx=50,pady=5,side=LEFT)

        bid_ent=ttkb.Entry(bid_input_frame,font=('Helvetica',10),bootstyle='secondary')
        bid_ent.pack(side=LEFT,padx=10,pady=5)

        #book data table
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
            book=check_bid(bid_ent.get())
            if book!=None:
                b_table.pack_forget()
                bid_ck_bt.pack_forget()
                c_name_label=ttkb.Label(bid_input_frame,text='BOOOK : %s'%book[1],font=('Helvetica',10),bootstyle='secondary')
                c_name_label.pack(padx=5,pady=5)
                
                confirm_input_fx(book[0],book[1],book[2])

            else:
                toast = ToastNotification(title="FUTElibs toast message",message="THE BOOK IS UNAVAILABLE",duration=3000,bootstyle='danger')
                toast.show_toast()



    back_bt_container = ttkb.Labelframe(remove_b_pg_frame,text='RETURN',bootstyle='secondary')
    back_bt_container.pack(padx=1,pady=1,fill=X)

    back_bt=ttkb.Button(back_bt_container,text='<<<',bootstyle='secondary outline',command=return_btn)
    back_bt.pack(padx=5,pady=3,side=LEFT)


    
    tcl_frame=ScrolledFrame(remove_b_pg_frame,autohide=True,bootstyle='dark')
    tcl_frame.pack(padx=5,pady=5,fill=BOTH,expand=True)

    bid_input_fx()




