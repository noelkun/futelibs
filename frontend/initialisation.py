#gui to initialise app on first use and use @utiliies.initialise_db.py to initialise data base
from tkinter import*
from ttkbootstrap.constants import*
import ttkbootstrap as ttkb
from utilities.initialise_db import*
from frontend.homepage import*


def initialise_frame(root):
    initialise_frame=ttkb.Frame(root,bootstyle='dark')
    initialise_frame.pack(padx=10,pady=10,fill=BOTH,expand=TRUE)

    def initialise():
        initialise_frame.pack_forget()
        create_db()
        homeframe(root)

        

    initialise()
