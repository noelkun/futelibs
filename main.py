from tkinter import*
from ttkbootstrap.constants import*
import ttkbootstrap as ttkb
from frontend.homepage import*
from frontend.initialisation import*
from backend.database import *






root=ttkb.Window(themename='vapor')

global logo
logo=PhotoImage(file="frontend/imgs/logo.png")

root.title('library management')
root.geometry('1200x600+40+20')
root.resizable(False,False)

root.iconphoto(False,logo)

if Connect()==None:
    initialise_frame(root)
else:
    homeframe(root)
    


root.mainloop()