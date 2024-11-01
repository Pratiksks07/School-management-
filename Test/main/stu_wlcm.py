import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from sql import *
from stu_profile import profile_stu
_location = os.path.dirname(__file__)

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class student(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,height=1020,width=1960)
        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        self.top = self

        self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.055, rely=0.091, relheight=0.137
                , relwidth=0.359)
        self.Message1.configure(background="#dbe6ff")
        self.Message1.configure(font="-family {Sitka Display} -size 72 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="#000000")
        self.Message1.configure(padx="1")
        self.Message1.configure(pady="1")
        self.Message1.configure(text='''WELCOME''')
        self.Message1.configure(width=460)

        self.Button1_1_2 = tk.Button(self.top)
        self.Button1_1_2.place(relx=-0.174, rely=0.232, height=120, width=120)
        self.Button1_1_2.configure(activebackground="#d9d9d9")
        self.Button1_1_2.configure(activeforeground="black")
        self.Button1_1_2.configure(background="#d9d9d9")
        self.Button1_1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_1_2.configure(font="-family {Segoe UI} -size 9")
        self.Button1_1_2.configure(foreground="#000000")
        self.Button1_1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_1_2.configure(highlightcolor="#000000")
        self.Button1_1_2.configure(text='''Button''')


        self.prof = tk.Button(self.top,command=lambda:self.profile_page(controller))
        self.prof.place(relx=0.109, rely=0.46, height=120, width=120)
        self.prof.configure(activebackground="#d9d9d9")
        self.prof.configure(activeforeground="black")
        self.prof.configure(background="#dbe6ff")
        self.prof.configure(disabledforeground="#a3a3a3")
        self.prof.configure(foreground="#000000")
        self.prof.configure(highlightbackground="#d9d9d9")
        self.prof.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Details1.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.prof.configure(image=_img0)
        self.prof.configure(relief="flat")

        self.msg_stud = tk.Button(self.top,command=lambda:self.msg_stu(controller))
        self.msg_stud.place(relx=0.328, rely=0.46, height=120, width=120)
        self.msg_stud.configure(activebackground="#d9d9d9")
        self.msg_stud.configure(activeforeground="black")
        self.msg_stud.configure(background="#dbe6ff")
        self.msg_stud.configure(disabledforeground="#a3a3a3")
        self.msg_stud.configure(font="-family {Segoe UI} -size 9")
        self.msg_stud.configure(foreground="#000000")
        self.msg_stud.configure(highlightbackground="#d9d9d9")
        self.msg_stud.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Message1.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.msg_stud.configure(image=_img1)
        self.msg_stud.configure(relief="flat")

        self.asg_stu = tk.Button(self.top)
        self.asg_stu.place(relx=0.547, rely=0.46, height=120, width=120)
        self.asg_stu.configure(activebackground="#d9d9d9")
        self.asg_stu.configure(activeforeground="black")
        self.asg_stu.configure(background="#dbe6ff")
        self.asg_stu.configure(disabledforeground="#a3a3a3")
        self.asg_stu.configure(font="-family {Segoe UI} -size 9")
        self.asg_stu.configure(foreground="#000000")
        self.asg_stu.configure(highlightbackground="#d9d9d9")
        self.asg_stu.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Assignment1.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.asg_stu.configure(image=_img2)
        self.asg_stu.configure(relief="flat")
        self.asg_stu.configure(text='''Button''')

        self.atd_stu1 = tk.Button(self.top,command=lambda:self.atd_stu(controller))
        self.atd_stu1.place(relx=0.766, rely=0.46, height=120, width=120)
        self.atd_stu1.configure(activebackground="#d9d9d9")
        self.atd_stu1.configure(activeforeground="black")
        self.atd_stu1.configure(background="#dbe6ff")
        self.atd_stu1.configure(disabledforeground="#a3a3a3")
        self.atd_stu1.configure(font="-family {Segoe UI} -size 9")
        self.atd_stu1.configure(foreground="#000000")
        self.atd_stu1.configure(highlightbackground="#d9d9d9")
        self.atd_stu1.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Attendance1.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.atd_stu1.configure(image=_img3)
        self.atd_stu1.configure(relief="flat")
        self.atd_stu1.configure(text='''Button''')

        self.tbd = tk.Button(self.top,command=lambda:self.timetable(controller))
        self.tbd.place(relx=0.109, rely=0.719, height=120, width=120)
        self.tbd.configure(activebackground="#d9d9d9")
        self.tbd.configure(activeforeground="black")
        self.tbd.configure(background="#dbe6ff")
        self.tbd.configure(disabledforeground="#a3a3a3")
        self.tbd.configure(font="-family {Segoe UI} -size 9")
        self.tbd.configure(foreground="#000000")
        self.tbd.configure(highlightbackground="#d9d9d9")
        self.tbd.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Time_table1.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.tbd.configure(image=_img4)
        self.tbd.configure(relief="flat")
        self.tbd.configure(text='''Button''')

        self.Message3 = tk.Message(self.top)
        self.Message3.place(relx=0.130, rely=0.650, relheight=0.024
                , relwidth=0.046)
        self.Message3.configure(background="#dbe6ff")
        self.Message3.configure(font="-family {Segoe UI} -size 14")
        self.Message3.configure(foreground="black")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="#000000")
        self.Message3.configure(padx="1")
        self.Message3.configure(pady="1")
        self.Message3.configure(text='''Details''')
        self.Message3.configure(width=70)

        self.Message3_1 = tk.Message(self.top)
        self.Message3_1.place(relx=0.345, rely=0.645, relheight=0.039
                , relwidth=0.059)
        self.Message3_1.configure(background="#dbe6ff")
        self.Message3_1.configure(font="-family {Segoe UI} -size 14")
        self.Message3_1.configure(foreground="black")
        self.Message3_1.configure(highlightbackground="#d9d9d9")
        self.Message3_1.configure(highlightcolor="#000000")
        self.Message3_1.configure(padx="1")
        self.Message3_1.configure(pady="1")
        self.Message3_1.configure(text='''Message''')
        self.Message3_1.configure(width=90)

        self.Message3_1_1 = tk.Message(self.top)
        self.Message3_1_1.place(relx=0.555, rely=0.645, relheight=0.045
                , relwidth=0.075)
        self.Message3_1_1.configure(background="#dbe6ff")
        self.Message3_1_1.configure(font="-family {Segoe UI} -size 14")
        self.Message3_1_1.configure(foreground="black")
        self.Message3_1_1.configure(highlightbackground="#d9d9d9")
        self.Message3_1_1.configure(highlightcolor="#000000")
        self.Message3_1_1.configure(padx="1")
        self.Message3_1_1.configure(pady="1")
        self.Message3_1_1.configure(text='''Assignment''')
        self.Message3_1_1.configure(width=101)

        self.Message3_1_1_1 = tk.Message(self.top)
        self.Message3_1_1_1.place(relx=0.775, rely=0.645, relheight=0.039
                , relwidth=0.074)
        self.Message3_1_1_1.configure(background="#dbe6ff")
        self.Message3_1_1_1.configure(font="-family {Segoe UI} -size 14")
        self.Message3_1_1_1.configure(foreground="black")
        self.Message3_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Message3_1_1_1.configure(highlightcolor="#000000")
        self.Message3_1_1_1.configure(padx="1")
        self.Message3_1_1_1.configure(pady="1")
        self.Message3_1_1_1.configure(text='''Attendance''')
        self.Message3_1_1_1.configure(width=112)

        self.Message3_1_1_1_1 = tk.Message(self.top)
        self.Message3_1_1_1_1.place(relx=0.118, rely=0.900, relheight=0.039
                , relwidth=0.074)
        self.Message3_1_1_1_1.configure(background="#dbe6ff")
        self.Message3_1_1_1_1.configure(font="-family {Segoe UI} -size 14")
        self.Message3_1_1_1_1.configure(foreground="black")
        self.Message3_1_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Message3_1_1_1_1.configure(highlightcolor="#000000")
        self.Message3_1_1_1_1.configure(padx="1")
        self.Message3_1_1_1_1.configure(pady="1")
        self.Message3_1_1_1_1.configure(text='''Time Table''')
        self.Message3_1_1_1_1.configure(width=112)

        self.back = tk.Button(self.top,command=lambda:self.login(controller))
        self.back.place(relx=0.820, rely=0.850, height=60, width=160)
        self.back.configure(activebackground="#d9d9d9")
        self.back.configure(activeforeground="black")
        self.back.configure(background="#f2f6fe")
        self.back.configure(disabledforeground="#a3a3a3")
        self.back.configure(foreground="black")
        self.back.configure(highlightbackground="#d9d9d9")
        self.back.configure(highlightcolor="#000000")
        self.back.configure(text='''Back''')
        photo_location = os.path.join(_location,"../Image/Logout_button.png")
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.back.configure(image=_img5)
        self.back.configure(relief="flat")

        self.Message2 = tk.Message(self.top)
        self.Message2.place(relx=0.063, rely=0.244, relheight=0.105
                , relwidth=0.165)
        self.Message2.configure(background="#dbe6ff")
        self.Message2.configure(font="-family {Sitka Display} -size 48 -weight bold")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="#000000")
        self.Message2.configure(padx="1")
        self.Message2.configure(pady="1")
        self.Message2.configure(text='''Student''')
        self.Message2.configure(width=300)


    def login(self,controller):
        from login_page import loginpage
        controller.show_frame(loginpage)

    def msg_stu(self,controller):
        from stu_msg import msg_stu
        controller.show_frame(msg_stu)

    def timetable(self,controller):
        from time_table import timetable
        controller.show_frame(timetable)

    def atd_stu(self,controller):
        from stu_atd import atd_stu
        controller.show_frame(atd_stu)

    def profile_page(self,controller):
        from stu_profile import profile_stu
        controller.show_frame(profile_stu)
