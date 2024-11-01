import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

class admin(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,height=1020,width=1960)
        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        self.top = self

        self.Message2 = tk.Message(self.top)
        self.Message2.place(relx=0.063, rely=0.244, relheight=0.091
                , relwidth=0.152)
        self.Message2.configure(background="#dbe6ff")
        self.Message2.configure(font="-family {Sitka Display} -size 48 -weight bold")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="#000000")
        self.Message2.configure(padx="1")
        self.Message2.configure(pady="1")
        self.Message2.configure(text='''Admin''')
        self.Message2.configure(width=195)

        #Assignment 
        self.Assg = tk.Button(self.top)
        self.Assg.place(relx=0.547, rely=0.479, height=120, width=120)
        self.Assg.configure(activebackground="#d9d9d9")
        self.Assg.configure(activeforeground="black")
        self.Assg.configure(background="#d9d9d9")
        self.Assg.configure(disabledforeground="#a3a3a3")
        self.Assg.configure(font="-family {Segoe UI} -size 9")
        self.Assg.configure(foreground="#000000")
        self.Assg.configure(highlightbackground="#d9d9d9")
        self.Assg.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Assignment1.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Assg.configure(image=_img0)
        self.Assg.configure(relief="flat")

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

        #Attendence Option
        self.atd = tk.Button(self.top,command=lambda:self.atd_admin(controller))
        self.atd.place(relx=0.766, rely=0.479, height=120, width=120)
        self.atd.configure(activebackground="#d9d9d9")
        self.atd.configure(activeforeground="black")
        self.atd.configure(background="#d9d9d9")
        self.atd.configure(disabledforeground="#a3a3a3")
        self.atd.configure(font="-family {Segoe UI} -size 9")
        self.atd.configure(foreground="#000000")
        self.atd.configure(highlightbackground="#d9d9d9")
        self.atd.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Attendance1.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.atd.configure(image=_img1)
        self.atd.configure(relief="flat")

        #Student Enrollment Option
        self.stu_en = tk.Button(self.top,command=lambda:self.enroll(controller))
        self.stu_en.place(relx=0.109, rely=0.479, height=120, width=120)
        self.stu_en.configure(activebackground="#d9d9d9")
        self.stu_en.configure(activeforeground="black")
        self.stu_en.configure(background="#d9d9d9")
        self.stu_en.configure(disabledforeground="#a3a3a3")
        self.stu_en.configure(foreground="#000000")
        self.stu_en.configure(highlightbackground="#d9d9d9")
        self.stu_en.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Enrollment1.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.stu_en.configure(image=_img2)
        self.stu_en.configure(relief="flat")

        self.Message3_1_1_1 = tk.Message(self.top)
        self.Message3_1_1_1.place(relx=0.773, rely=0.67, relheight=0.058
                , relwidth=0.085)
        self.Message3_1_1_1.configure(background="#dbe6ff")
        self.Message3_1_1_1.configure(font="-family {Segoe UI Symbol} -size 14")
        self.Message3_1_1_1.configure(foreground="black")
        self.Message3_1_1_1.configure(highlightbackground="#d9d9d9")
        self.Message3_1_1_1.configure(highlightcolor="#000000")
        self.Message3_1_1_1.configure(justify='center')
        self.Message3_1_1_1.configure(padx="1")
        self.Message3_1_1_1.configure(pady="1")
        self.Message3_1_1_1.configure(text='''Attendence''')
        self.Message3_1_1_1.configure(width=109)

        self.Message3_1 = tk.Message(self.top)
        self.Message3_1.place(relx=0.328, rely=0.67, relheight=0.058
                , relwidth=0.093)
        self.Message3_1.configure(background="#dbe6ff")
        self.Message3_1.configure(font="-family {Segoe UI Symbol} -size 14")
        self.Message3_1.configure(foreground="black")
        self.Message3_1.configure(highlightbackground="#d9d9d9")
        self.Message3_1.configure(highlightcolor="#000000")
        self.Message3_1.configure(justify='center')
        self.Message3_1.configure(padx="1")
        self.Message3_1.configure(pady="1")
        self.Message3_1.configure(text='''Message''')
        self.Message3_1.configure(width=119)

        self.Message3_1_1 = tk.Message(self.top)
        self.Message3_1_1.place(relx=0.555, rely=0.67, relheight=0.058
                , relwidth=0.085)
        self.Message3_1_1.configure(background="#dbe6ff")
        self.Message3_1_1.configure(cursor="fleur")
        self.Message3_1_1.configure(font="-family {Segoe UI Symbol} -size 14")
        self.Message3_1_1.configure(foreground="black")
        self.Message3_1_1.configure(highlightbackground="#d9d9d9")
        self.Message3_1_1.configure(highlightcolor="#000000")
        self.Message3_1_1.configure(justify='center')
        self.Message3_1_1.configure(padx="1")
        self.Message3_1_1.configure(pady="1")
        self.Message3_1_1.configure(text='''Assignment''')
        self.Message3_1_1.configure(width=109)

        #Message Option
        self.msg = tk.Button(self.top,command=lambda:self.msg_adm(controller))
        self.msg.place(relx=0.328, rely=0.479, height=120, width=120)
        self.msg.configure(activebackground="#d9d9d9")
        self.msg.configure(activeforeground="black")
        self.msg.configure(background="#d9d9d9")
        self.msg.configure(disabledforeground="#a3a3a3")
        self.msg.configure(font="-family {Segoe UI} -size 9")
        self.msg.configure(foreground="#000000")
        self.msg.configure(highlightbackground="#d9d9d9")
        self.msg.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Message1.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.msg.configure(image=_img3)
        self.msg.configure(relief="flat")

        self.Message3 = tk.Message(self.top)
        self.Message3.place(relx=0.117, rely=0.67, relheight=0.073
                , relwidth=0.077)
        self.Message3.configure(background="#dbe6ff")
        self.Message3.configure(font="-family {Segoe UI Symbol} -size 14")
        self.Message3.configure(foreground="black")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="#000000")
        self.Message3.configure(justify='center')
        self.Message3.configure(padx="1")
        self.Message3.configure(pady="1")
        self.Message3.configure(text='''Student Enrollment''')
        self.Message3.configure(width=99)

        #Back Button
        self.back = tk.Button(self.top,command=lambda:self.login(controller))
        self.back.place(relx=0.820, rely=0.850, height=60, width=160)
        self.back.configure(activebackground="#d9d9d9")
        self.back.configure(activeforeground="black")
        self.back.configure(background="#f2f6fe")
        self.back.configure(disabledforeground="#a3a3a3")
        self.back.configure(foreground="black")
        self.back.configure(highlightbackground="#d9d9d9")
        self.back.configure(highlightcolor="#000000")
        self.back.configure(text='''BACK''')
        self.back.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Logout_button.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.back.configure(image=_img4)
        self.back.configure(relief="flat")


    def enroll(self,controller):
        from stu_enroll import stu_en
        controller.show_frame(stu_en)

    def login(self,controller):
        from login_page import loginpage
        controller.show_frame(loginpage)

    def atd_admin(self,controller):
        from adm_atd import atd_admin
        controller.show_frame(atd_admin)

    def msg_adm(self,controller):
        from adm_msg import msg_adm
        controller.show_frame(msg_adm)
