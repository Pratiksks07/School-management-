import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from sql import login

_location = os.path.dirname(__file__)

class loginpage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,height=1020,width=1960)
        self.configure(background="#d9d9d9")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        self.top = self

        global id_var,passw_var
        id_var=tk.StringVar()
        passw_var=tk.StringVar()
        
        self.Canvas1 = tk.Canvas(self.top)
        self.Canvas1.place(relx=0.605, rely=0.0, relheight=1.068, relwidth=0.395)

        self.Canvas1.configure(background="#dbe6ff")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="#000000")
        self.Canvas1.configure(insertbackground="#000000")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#d9d9d9")
        self.Canvas1.configure(selectforeground="black")

        self.Enterpsword = tk.Entry(self.Canvas1, textvariable= passw_var, font=(20),show="*")
        self.Enterpsword.place(relx=0.1, rely=0.548, height=30, relwidth=0.550)
        self.Enterpsword.configure(background="#f2f6fe")
        self.Enterpsword.configure(disabledforeground="#a3a3a3")
        self.Enterpsword.configure(font="TkFixedFont")
        self.Enterpsword.configure(foreground="black")
        self.Enterpsword.configure(highlightbackground="#d9d9d9")
        self.Enterpsword.configure(highlightcolor="#000000")
        self.Enterpsword.configure(insertbackground="#000000")
        self.Enterpsword.configure(selectbackground="#d9d9d9")
        self.Enterpsword.configure(selectforeground="black")

        self.SUBMIT = tk.Button(self.Canvas1, command= lambda: login(id_var,passw_var,self,controller))
        self.SUBMIT.place(relx=0.305, rely=0.635, height=80, width=198)
        self.SUBMIT.configure(activebackground="#d9d9d9")
        self.SUBMIT.configure(activeforeground="black")
        self.SUBMIT.configure(background="#f2f6fe")
        self.SUBMIT.configure(disabledforeground="#a3a3a3")
        self.SUBMIT.configure(font="-family {Segoe UI Emoji} -size 12 -weight bold")
        self.SUBMIT.configure(foreground="black")
        self.SUBMIT.configure(highlightbackground="#d9d9d9")
        self.SUBMIT.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/login_button(1).png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.SUBMIT.configure(image=_img3)
        self.SUBMIT.configure(relief="flat")
        self.SUBMIT.configure(text='''SUBMIT''')

        self.img = tk.Button(self.Canvas1,relief=tk.FLAT)
        self.img.place(relx=0.305, rely=0.135, height=100, width=100)
        self.img.configure(activebackground="#d9d9d9")
        self.img.configure(activeforeground="black")
        self.img.configure(background="#f2f6fe")
        self.img.configure(disabledforeground="#a3a3a3")
        self.img.configure(font="-family {Segoe UI Emoji} -size 12 -weight bold")
        self.img.configure(foreground="black")
        self.img.configure(highlightbackground="#d9d9d9")
        self.img.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/user_icon.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.img.configure(image=_img2)
        self.img.configure(relief="flat")
        self.img.config(command=lambda: None)

        """self.LOGIN = tk.Label(self.Canvas1)
        self.LOGIN.place(relx=0.279, rely=0.072, height=50, width=204)
        self.LOGIN.configure(activebackground="#d9d9d9")
        self.LOGIN.configure(activeforeground="black")
        self.LOGIN.configure(anchor='w')
        self.LOGIN.configure(background="#dbe6ff")
        self.LOGIN.configure(compound='left')
        self.LOGIN.configure(disabledforeground="#a3a3a3")
        self.LOGIN.configure(font="-family {Browallia New} -size 48 -weight bold -underline 1")
        self.LOGIN.configure(foreground="black")
        self.LOGIN.configure(highlightbackground="#d9d9d9")
        self.LOGIN.configure(highlightcolor="#000000")
        self.LOGIN.configure(text='''LOGIN''')
        """
        """self.IMAGE1 = tk.Label(self.Canvas1)
        self.IMAGE1.place(relx=-0.305, rely=0.120, height=100, width=100)
        self.IMAGE1.configure(activebackground="#d9d9d9")
        self.IMAGE1.configure(activeforeground="black")
        self.IMAGE1.configure(anchor='w')
        self.IMAGE1.configure(background="#d9d9d9")
        self.IMAGE1.configure(compound='left')
        self.IMAGE1.configure(disabledforeground="#a3a3a3")
        self.IMAGE1.configure(foreground="#000000")
        self.IMAGE1.configure(highlightbackground="#d9d9d9")
        self.IMAGE1.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/user_icon.png")
        global _img01
        _img01= tk.PhotoImage(file=photo_location)
        self.IMAGE1.configure(image=_img01)
        self.IMAGE1.configure(text='''USER ID:''')"""

        self.USERID = tk.Label(self.Canvas1)
        self.USERID.place(relx=0.1, rely=0.332, height=31, width=114)
        self.USERID.configure(activebackground="#d9d9d9")
        self.USERID.configure(activeforeground="black")
        self.USERID.configure(anchor='w')
        self.USERID.configure(background="#dbe6ff")
        self.USERID.configure(compound='left')
        self.USERID.configure(disabledforeground="#a3a3a3")
        self.USERID.configure(font="-family {Segoe UI Black} -size 14 -weight bold")
        self.USERID.configure(foreground="black")
        self.USERID.configure(highlightbackground="#d9d9d9")
        self.USERID.configure(highlightcolor="#000000")
        self.USERID.configure(text='''USER ID''')

        self.PASSWORD = tk.Label(self.Canvas1)
        self.PASSWORD.place(relx=0.1, rely=0.505, height=21, width=174)
        self.PASSWORD.configure(activebackground="#d9d9d9")
        self.PASSWORD.configure(activeforeground="black")
        self.PASSWORD.configure(anchor='w')
        self.PASSWORD.configure(background="#dbe6ff")
        self.PASSWORD.configure(compound='left')
        self.PASSWORD.configure(disabledforeground="#a3a3a3")
        self.PASSWORD.configure(font="-family {Segoe UI Black} -size 14 -weight bold")
        self.PASSWORD.configure(foreground="black")
        self.PASSWORD.configure(highlightbackground="#d9d9d9")
        self.PASSWORD.configure(highlightcolor="#000000")
        self.PASSWORD.configure(text='''PASSWORD''')

        self.EnterID = tk.Entry(self.Canvas1, textvariable= id_var, font=(20))
        self.EnterID.place(relx=0.1, rely=0.39, height=30, relwidth=0.550)
        self.EnterID.configure(background="#f2f6fe")
        self.EnterID.configure(disabledforeground="#a3a3a3")
        self.EnterID.configure(font="TkFixedFont")
        self.EnterID.configure(foreground="black")
        self.EnterID.configure(highlightbackground="#d9d9d9")
        self.EnterID.configure(highlightcolor="#000000")
        self.EnterID.configure(insertbackground="#000000")
        self.EnterID.configure(selectbackground="#d9d9d9")
        self.EnterID.configure(selectforeground="black")

        self.IMAGE = tk.Label(self.top)
        self.IMAGE.place(relx=-0.0, rely=0.0, height=680, width=805)
        self.IMAGE.configure(activebackground="#d9d9d9")
        self.IMAGE.configure(activeforeground="black")
        self.IMAGE.configure(anchor='w')
        self.IMAGE.configure(background="#d9d9d9")
        self.IMAGE.configure(compound='left')
        self.IMAGE.configure(disabledforeground="#a3a3a3")
        self.IMAGE.configure(foreground="#000000")
        self.IMAGE.configure(highlightbackground="#d9d9d9")
        self.IMAGE.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/FLEX.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.IMAGE.configure(image=_img0)
        self.IMAGE.configure(text='''USER ID:''')

    def admin(self,controller):
        from adm_wlcm import admin
        controller.show_frame(admin)

    def student(self,controller):
        from stu_wlcm import student
        controller.show_frame(student)

