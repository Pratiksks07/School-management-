# Importing Modules
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from sql import *
from stu_profile import profile_stu
from PIL import Image, ImageTk


_location = os.path.dirname(__file__) #Stores the path of the current file


# Student Page class
class student(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,height=1020,width=1960)
        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        self.top = self

        # Load and set the background image
        background_image_path = os.path.join(_location, "../Image/background.png")  # Change to your image path
        self.bg_image = Image.open(background_image_path)
        self.bg_image = self.bg_image.resize((1960, 1020), Image.ANTIALIAS)  # Adjust size if needed
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        # Create a label for the background image and place it
        self.bg_label = tk.Label(self, image=self.bg_image_tk)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)


        # Top border Image
        self.upper = tk.Label(self.top)
        self.upper.place(relx=0.001, rely=0.0, relheight=0.240
                , relwidth=0.999)
        self.upper.configure(background="Black")
        self.upper.configure(relief="raised")
        photo_location = os.path.join(os.path.dirname(__file__), "../Image/Welcome2.png")
        self.wlcm_img = tk.PhotoImage(file=photo_location)
        self.upper.configure(image=self.wlcm_img)
        self.upper.configure(relief="flat")


        # Profile Button
        self.prof = tk.Button(self.top,command=lambda:self.profile_page(controller))
        self.prof.place(relx=0.109, rely=0.36, height=160, width=160)
        self.prof.configure(background="#dbe6ff")
        photo_location = os.path.join(_location,"../Image/Details2.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.prof.configure(image=_img0)
        self.prof.configure(relief="groove")


        # Message Button
        self.msg_stud = tk.Button(self.top,command=lambda:self.msg_stu(controller))
        self.msg_stud.place(relx=0.328, rely=0.36, height=160, width=160)
        self.msg_stud.configure(background="#dbe6ff")
        self.msg_stud.configure(font="-family {Segoe UI} -size 9")
        photo_location = os.path.join(_location,"../Image/Message2.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.msg_stud.configure(image=_img1)
        self.msg_stud.configure(relief="groove")


        # Question Bank Button
        self.qbank_stu = tk.Button(self.top,command=lambda:self.qbank(controller))
        self.qbank_stu.place(relx=0.547, rely=0.36, height=160, width=160)
        self.qbank_stu.configure(background="#dbe6ff")
        self.qbank_stu.configure(font="-family {Segoe UI} -size 9")
        photo_location = os.path.join(_location,"../Image/Question_bank2.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.qbank_stu.configure(image=_img2)
        self.qbank_stu.configure(relief="groove")


        # Attendence Button
        self.atd_stu1 = tk.Button(self.top,command=lambda:self.atd_stu(controller))
        self.atd_stu1.place(relx=0.766, rely=0.36, height=160, width=160)
        self.atd_stu1.configure(background="#dbe6ff")
        self.atd_stu1.configure(font="-family {Segoe UI} -size 9")
        photo_location = os.path.join(_location,"../Image/Attendance2.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.atd_stu1.configure(image=_img3)
        self.atd_stu1.configure(relief="groove")


        # Time Table Button
        self.tbd = tk.Button(self.top,command=lambda:self.timetable(controller))
        self.tbd.place(relx=0.109, rely=0.700, height=160, width=160)
        self.tbd.configure(background="#dbe6ff")
        self.tbd.configure(font="-family {Segoe UI} -size 9")
        photo_location = os.path.join(_location,"../Image/Time_table2.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.tbd.configure(image=_img4)
        self.tbd.configure(relief="groove")


        # Back Button
        self.back = tk.Button(self.top,command=lambda:self.login(controller))
        self.back.place(relx=0.820, rely=0.850, height=60, width=160)
        self.back.configure(background="#f2f6fe")
        self.back.configure(text='''Back''')
        photo_location = os.path.join(_location,"../Image/Logout_button2.png")
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.back.configure(image=_img5)
        self.back.configure(relief="flat")

        
    # Functions for switching between pages
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
    
    def qbank(self,controller):
        from stu_qbank import qbank_stu
        controller.show_frame(qbank_stu)
