import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from sql import *
from stu_profile import profile_stu
from PIL import Image, ImageTk
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

        # Load and set the background image
        background_image_path = os.path.join(_location, "../Image/background.png")  # Change to your image path
        self.bg_image = Image.open(background_image_path)
        self.bg_image = self.bg_image.resize((1960, 1020), Image.ANTIALIAS)  # Adjust size if needed
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        # Create a label for the background image and place it
        self.bg_label = tk.Label(self, image=self.bg_image_tk)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)




        self.upper = tk.Label(self.top)
        self.upper.place(relx=0.001, rely=0.0, relheight=0.240
                , relwidth=0.999)
        self.upper.configure(background="Black")
        self.upper.configure(foreground="#000000")
        self.upper.configure(highlightbackground="#d9d9d9")
        self.upper.configure(highlightcolor="#000000")
        self.upper.configure(relief="raised")
        photo_location = os.path.join(os.path.dirname(__file__), "../Image/Welcome2.png")
        self.wlcm_img = tk.PhotoImage(file=photo_location)
        self.upper.configure(image=self.wlcm_img)
        self.upper.configure(relief="flat")


        """self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.055, rely=0.00, relheight=0.137
                , relwidth=0.359)
        self.Message1.configure(background="#000000")
        self.Message1.configure(font="-family {Sitka Display} -size 55 -weight bold")
        self.Message1.configure(foreground="White")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="White")
        self.Message1.configure(padx="1")
        self.Message1.configure(pady="1")
        self.Message1.configure(text='''WELCOME''')
        self.Message1.configure(width=460)
        self.Message1.configure(anchor='n')
        

        self.Message2 = tk.Message(self.top)
        self.Message2.place(relx=0.100, rely=0.150, relheight=0.080, relwidth=0.155)
        self.Message2.configure(background="#000000")
        self.Message2.configure(font="-family {Sitka Display} -size 40 -weight bold")
        self.Message2.configure(foreground="White")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="White")
        self.Message2.configure(padx="1")
        self.Message2.configure(pady="1")
        self.Message2.configure(text='''Student''')
        self.Message2.configure(width=280)
        self.Message2.configure(anchor='s')

        self.admi = tk.Label(self.top)
        self.admi.place(relx=0.800, rely=0.0, height=150, width=150)  # Adjusted position for visibility
        self.admi.configure(
            background="#d9d9d9",
            foreground="#000000",
            anchor='center')
        photo_location = os.path.join(os.path.dirname(__file__), "../Image/user_icon1.png")
        self.admi_img = tk.PhotoImage(file=photo_location)
        self.admi.configure(image=self.admi_img)
        self.admi.configure(relief="flat")"""



        self.prof = tk.Button(self.top,command=lambda:self.profile_page(controller))
        self.prof.place(relx=0.109, rely=0.36, height=160, width=160)
        self.prof.configure(activebackground="#d9d9d9")
        self.prof.configure(activeforeground="black")
        self.prof.configure(background="#dbe6ff")
        self.prof.configure(disabledforeground="#a3a3a3")
        self.prof.configure(foreground="#000000")
        self.prof.configure(highlightbackground="#d9d9d9")
        self.prof.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Details2.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.prof.configure(image=_img0)
        self.prof.configure(relief="groove")

        self.msg_stud = tk.Button(self.top,command=lambda:self.msg_stu(controller))
        self.msg_stud.place(relx=0.328, rely=0.36, height=160, width=160)
        self.msg_stud.configure(activebackground="#d9d9d9")
        self.msg_stud.configure(activeforeground="black")
        self.msg_stud.configure(background="#dbe6ff")
        self.msg_stud.configure(disabledforeground="#a3a3a3")
        self.msg_stud.configure(font="-family {Segoe UI} -size 9")
        self.msg_stud.configure(foreground="#000000")
        self.msg_stud.configure(highlightbackground="#d9d9d9")
        self.msg_stud.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Message2.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.msg_stud.configure(image=_img1)
        self.msg_stud.configure(relief="groove")

        self.asg_stu = tk.Button(self.top)
        self.asg_stu.place(relx=0.547, rely=0.36, height=160, width=160)
        self.asg_stu.configure(activebackground="#d9d9d9")
        self.asg_stu.configure(activeforeground="black")
        self.asg_stu.configure(background="#dbe6ff")
        self.asg_stu.configure(disabledforeground="#a3a3a3")
        self.asg_stu.configure(font="-family {Segoe UI} -size 9")
        self.asg_stu.configure(foreground="#000000")
        self.asg_stu.configure(highlightbackground="#d9d9d9")
        self.asg_stu.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Assignment2.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.asg_stu.configure(image=_img2)
        self.asg_stu.configure(relief="groove")
        self.asg_stu.configure(text='''Button''')

        self.atd_stu1 = tk.Button(self.top,command=lambda:self.atd_stu(controller))
        self.atd_stu1.place(relx=0.766, rely=0.36, height=160, width=160)
        self.atd_stu1.configure(activebackground="#d9d9d9")
        self.atd_stu1.configure(activeforeground="black")
        self.atd_stu1.configure(background="#dbe6ff")
        self.atd_stu1.configure(disabledforeground="#a3a3a3")
        self.atd_stu1.configure(font="-family {Segoe UI} -size 9")
        self.atd_stu1.configure(foreground="#000000")
        self.atd_stu1.configure(highlightbackground="#d9d9d9")
        self.atd_stu1.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Attendance2.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.atd_stu1.configure(image=_img3)
        self.atd_stu1.configure(relief="groove")
        self.atd_stu1.configure(text='''Button''')

        self.tbd = tk.Button(self.top,command=lambda:self.timetable(controller))
        self.tbd.place(relx=0.109, rely=0.700, height=160, width=160)
        self.tbd.configure(activebackground="#d9d9d9")
        self.tbd.configure(activeforeground="black")
        self.tbd.configure(background="#dbe6ff")
        self.tbd.configure(disabledforeground="#a3a3a3")
        self.tbd.configure(font="-family {Segoe UI} -size 9")
        self.tbd.configure(foreground="#000000")
        self.tbd.configure(highlightbackground="#d9d9d9")
        self.tbd.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Time_table2.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.tbd.configure(image=_img4)
        self.tbd.configure(relief="groove")
        self.tbd.configure(text='''Button''')

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
        photo_location = os.path.join(_location,"../Image/Logout_button2.png")
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.back.configure(image=_img5)
        self.back.configure(relief="flat")

        

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
