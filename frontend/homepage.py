from tkinter import*
from ttkbootstrap.constants import*
import ttkbootstrap as ttkb
from ttkbootstrap.toast import ToastNotification
from backend.loginbackend import*
from middleware.userLibs import *
from frontend.customer import*
from frontend.admin import*
from frontend.employee import*
from backend.signupbackend import*



def homeframe(root):


    def loginbtn(user):
        home_frame.pack_forget()
        login_pg_frame(root,user)

    def adminloginbtn():
        loginbtn('admin')
    
    def memberloginbtn():
        loginbtn('member')

    def employeeloginbtn():
        loginbtn('employee')



    global home_frame
    home_frame=ttkb.Frame(root,bootstyle='dark')
    home_frame.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)

    header_frame=ttkb.Labelframe(home_frame,text='Welcome to FUTE libs',bootstyle='secondary')
    header_frame.pack(padx=10,pady=40,fill=X)

    

    login_label=ttkb.Label(header_frame,text='LOGIN TO FUTElibs ',font=('Helvetica',36),bootstyle='primary')
    login_label.pack(pady=10)

    element_frame=ttkb.Labelframe(home_frame,text='LOGIN AS',bootstyle='secondary')
    element_frame.pack(padx=10,pady=5,expand=TRUE,fill=X)


    admin_b=ttkb.Button(element_frame,text='ADMIN LOGIN',bootstyle='secondary-outline',command=adminloginbtn)
    admin_b.pack(side=LEFT,padx=150,pady=10)

    member_b=ttkb.Button(element_frame,text='MEMBER LOGIN',bootstyle='secondary-outline',command=memberloginbtn)
    member_b.pack(side=LEFT,padx=100,pady=10)

    employee_b=ttkb.Button(element_frame,text='EMPLOYEE LOGIN',bootstyle='secondary-outline',command=employeeloginbtn)
    employee_b.pack(side=LEFT,padx=150,pady=10)








def login_pg_frame(root,user):

    

    User_login_frame_page=ttkb.Frame(root,bootstyle='dark')
    User_login_frame_page.pack(padx=10,pady=10,expand=TRUE,fill=BOTH)

    def signupframe_bt():
        User_login_frame_page.pack_forget()
        signup_frame(root,user)

    def loginlogic():

        userdata=UserLibs(email=email_ent.get(), password=pass_ent.get())
        result=login(userdata,user)

        if result!=None:

            userdata=UserLibs(result[0],result[1],result[2],result[3],result[4])
            
            User_login_frame_page.pack_forget()

            if user=='member':
                toast = ToastNotification(title="FUTElibs toast message",message="login successful",duration=3000,bootstyle='success')
                toast.show_toast()
                customer_frame(root,userdata)
            elif user=='admin':
                toast = ToastNotification(title="FUTElibs toast message",message="login successful",duration=3000,bootstyle='success')
                toast.show_toast()
                admin_frame(root,userdata)

            elif user=='employee':
                toast = ToastNotification(title="FUTElibs toast message",message="login successful",duration=3000,bootstyle='success')
                toast.show_toast()
                employee_frame(root,userdata)
                
        else:
            element_frame.configure(bootstyle='danger')
            toast = ToastNotification(title="FUTElibs toast message",message="wrong email/password",duration=3000,bootstyle='danger')
            toast.show_toast()



            
    def return_btn():
        User_login_frame_page.pack_forget()
        homeframe(root)




    if user=='member':
        lb_text='MEMBER LOGIN PAGE'
    elif user=='admin':
        lb_text='ADMIN LOGIN PAGE'
    elif user=='employee':
        lb_text='EMPLOYEE LOGIN PAGE'


    header_frame=ttkb.Labelframe(User_login_frame_page,text='WELCOME',bootstyle='secondary')
    header_frame.pack(padx=10,pady=10,fill=X)

    back_bt=ttkb.Button(header_frame,text='BACK',bootstyle='secondary outline',command=return_btn)
    back_bt.pack(padx=5,pady=5,side=LEFT)

    User_lin_lb=ttkb.Label(header_frame,text=lb_text,font=('Helvetica',32),bootstyle='primary')
    User_lin_lb.pack(pady=10)

    #global element_frame
    element_frame=ttkb.Labelframe(User_login_frame_page,text='Login',bootstyle='secondary')
    element_frame.pack(pady=30)

    email_frame=ttkb.Frame(element_frame)
    email_frame.pack(pady=30,padx=10,fill=BOTH)
    pass_frame=ttkb.Frame(element_frame)
    pass_frame.pack(pady=30,padx=10,fill=BOTH)


    email_lb=ttkb.Label(email_frame,text='Enter  Email ID',font=('Helvetica',10),bootstyle='secondary')
    email_lb.pack(side=LEFT,pady=30,padx=20)

    email_ent=ttkb.Entry(email_frame,font=('Helvetica',10),bootstyle='secondary')
    email_ent.pack(pady=5,padx=10,side=RIGHT)


    pass_lb=ttkb.Label(pass_frame,text='Enter Password',font=('Helvetica',10),bootstyle='secondary')
    pass_lb.pack(side=LEFT,pady=30,padx=20)

    pass_ent=ttkb.Entry(pass_frame,font=('Helvetica',10),bootstyle='secondary',show='*')
    pass_ent.pack(pady=5,padx=10,side=RIGHT)


    button_frame=ttkb.Frame(element_frame)
    button_frame.pack(pady=15,padx=10,fill=Y)

    login_b=ttkb.Button(button_frame,text='LOGIN',bootstyle='success-outline',command=loginlogic)
    login_b.pack(side=LEFT,pady=5,padx=5)

    signup_b=ttkb.Button(button_frame,text='SIGNUP',bootstyle='info-outline',command=signupframe_bt)
    signup_b.pack(side=LEFT,pady=5,padx=5)



def signup_frame(root,user):
    signup_frame=ttkb.Frame(root,bootstyle='dark')
    signup_frame.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)

    def return_btn():
        signup_frame.pack_forget()
        login_pg_frame(root,user)


    def confirm_input_fx(cname,email,passw):

        confirm_frame=ttkb.Labelframe(tcl_frame,text='CONFIRM USER CREATION QUERY',bootstyle='secondary')
        confirm_frame.pack(padx=10,pady=30,expand=TRUE,fill=BOTH)


        def submit_input_fx():
            add_user(cname,email,passw,user)
            toast=ToastNotification(title="FUTElibs toast message",message="USER CREATED SUCCESSFULLY",duration=3000,bootstyle='success')
            toast.show_toast()

            return_btn()

        m1=ttkb.Label(confirm_frame,text='THE FOLLOWING USER IS TO BE CREATED',font=('Helvetica',14),bootstyle='primary')
        m1.pack(padx=10,pady=10)

        cname_lb=ttkb.Label(confirm_frame,text='  NAME: %s'%cname,font=('Helvetica',10),bootstyle='secondary')
        cname_lb.pack(padx=10,pady=10)

        email_lb=ttkb.Label(confirm_frame,text='  EMAIL: %s'%email,font=('Helvetica',10),bootstyle='secondary')
        email_lb.pack(padx=10,pady=10)

        passw_lb=ttkb.Label(confirm_frame,text='  PASSWORD: %s'%passw,font=('Helvetica',10),bootstyle='secondary')
        passw_lb.pack(padx=10,pady=10)
        



    def cinfo_input_fx():
        

        def confirm_btn():
            result=check_email(email_ent.get())


            if var_cname.get()=='':
                toast = ToastNotification(title="FUTElibs toast message",message="USER NAME CANNOT BE EMPTY",duration=3000,bootstyle='danger')
                toast.show_toast()
            elif var_email.get()=='':
                toast = ToastNotification(title="FUTElibs toast message",message="USER EMAIL CANNOT BE EMPTY",duration=3000,bootstyle='danger')
                toast.show_toast()
            elif var_pass.get()=='':
                toast = ToastNotification(title="FUTElibs toast message",message="USER PASSWORD CANNOT BE EMPTY",duration=3000,bootstyle='danger')
                toast.show_toast()
            elif result:
                toast = ToastNotification(title="FUTElibs toast message",message="USER ALREADY EXISTS",duration=3000,bootstyle='danger')
                toast.show_toast()
            else:
                do()

        cinfo_input_frame=ttkb.Labelframe(tcl_frame,text='USER INFO',bootstyle='secondary')
        cinfo_input_frame.pack(padx=10,pady=20,expand=TRUE,fill=BOTH)

        cname_input_frame=ttkb.Labelframe(cinfo_input_frame,text='NAME',bootstyle='secondary')
        cname_input_frame.pack(padx=10,pady=10,fill=X)

        cname_lb=ttkb.Label(cname_input_frame,text='Enter Name',font=('Helvetica',10),bootstyle='secondary')
        cname_lb.pack(side=LEFT,padx=10,pady=10)

        #limiting the input for name
        var_cname=StringVar()
        max_len_cname=20

        def on_enter_name(*args):
            s=var_cname.get()
            if len(s)>max_len_cname:
                var_cname.set(s[:max_len_cname])

        var_cname.trace('w',on_enter_name)


        name_ent=ttkb.Entry(cname_input_frame,textvariable=var_cname,font=('Helvetica',10),bootstyle='secondary')
        name_ent.pack(padx=10,pady=10,side=LEFT)

        email_input_frame=ttkb.Labelframe(cinfo_input_frame,text='EMAIL',bootstyle='secondary')
        email_input_frame.pack(padx=10,pady=10,fill=X)

        email_lb=ttkb.Label(email_input_frame,text='Enter Email',font=('Helvetica',10),bootstyle='secondary')
        email_lb.pack(side=LEFT,padx=10,pady=10)

        #limiting the input for email
        var_email=StringVar()

        max_len_email=25
        def on_enter_email(*args):
            s=var_email.get()
            if len(s)>max_len_email:
                var_email.set(s[:max_len_email])

        var_email.trace('w',on_enter_email)

        email_ent=ttkb.Entry(email_input_frame,textvariable=var_email,font=('Helvetica',10),bootstyle='secondary')
        email_ent.pack(padx=10,pady=10,side=LEFT)

        pass_input_frame=ttkb.Labelframe(cinfo_input_frame,text='PASSWORD',bootstyle='secondary')
        pass_input_frame.pack(padx=10,pady=10,fill=X)

        pass_lb=ttkb.Label(pass_input_frame,text='Enter Password',font=('Helvetica',10),bootstyle='secondary')
        pass_lb.pack(side=LEFT,padx=10,pady=10)

        #limiting the input for password
        var_pass=StringVar()

        max_len_pass=20
        def on_enter_pass(*args):
            s=var_pass.get()
            if len(s)>max_len_pass:
                var_pass.set(s[:max_len_pass])

        var_pass.trace('w',on_enter_pass)

        pass_ent=ttkb.Entry(pass_input_frame,textvariable=var_pass,font=('Helvetica',10),bootstyle='secondary',show='*')
        pass_ent.pack(padx=10,pady=10,side=LEFT)

        cinfo_cn_bt=ttkb.Button(cinfo_input_frame,text='CONFIRM',bootstyle='success-outline',command=confirm_btn)
        cinfo_cn_bt.pack(padx=10,pady=10,side=BOTTOM)

        def do():
            pass










    if user=='admin':
        lb_text='ADMIN SIGNUP'
    elif user=='member':
        lb_text='MEMBER SIGNUP'

    
    header_frame=ttkb.Labelframe(signup_frame,text=lb_text,bootstyle='secondary')
    header_frame.pack(padx=10,pady=10,fill=X)

    back_btn=ttkb.Button(header_frame,text='BACK',bootstyle='secondary-outline',command=return_btn)
    back_btn.pack(side=LEFT,padx=10,pady=10)

    signup_label=ttkb.Label(header_frame,text=lb_text,font=('Helvetica',32),bootstyle='primary')
    signup_label.pack(pady=10)

    element_frame=ttkb.Labelframe(signup_frame,text='SIGNUP',bootstyle='secondary')
    element_frame.pack(padx=10,pady=5,expand=TRUE,fill=BOTH)


    tcl_frame=ScrolledFrame(element_frame,autohide=True,bootstyle='dark')
    tcl_frame.pack(padx=5,pady=5,fill=BOTH,expand=True)


    cinfo_input_fx()
