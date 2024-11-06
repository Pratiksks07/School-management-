import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from PIL import Image, ImageTk

_location = os.path.dirname(__file__)

class admin(tk.Frame):
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
        photo_location = os.path.join(os.path.dirname(__file__), "../Image/Wlcm_adm.png")
        self.wlcm_img = tk.PhotoImage(file=photo_location)
        self.upper.configure(image=self.wlcm_img)
        self.upper.configure(relief="flat")


        """self.Message2 = tk.Message(self.top)
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
        self.Message1.configure(width=460)"""


        #Assignment 
        self.Assg = tk.Button(self.top)
        self.Assg.place(relx=0.547, rely=0.479, height=160, width=160)
        self.Assg.configure(activebackground="#d9d9d9")
        self.Assg.configure(activeforeground="black")
        self.Assg.configure(background="#d9d9d9")
        self.Assg.configure(disabledforeground="#a3a3a3")
        self.Assg.configure(font="-family {Segoe UI} -size 9")
        self.Assg.configure(foreground="#000000")
        self.Assg.configure(highlightbackground="#d9d9d9")
        self.Assg.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Assignment2.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Assg.configure(image=_img0)
        self.Assg.configure(relief="groove")

        
        #Attendence Option
        self.atd = tk.Button(self.top,command=lambda:self.atd_admin(controller))
        self.atd.place(relx=0.766, rely=0.479, height=160, width=160)
        self.atd.configure(activebackground="#d9d9d9")
        self.atd.configure(activeforeground="black")
        self.atd.configure(background="#d9d9d9")
        self.atd.configure(disabledforeground="#a3a3a3")
        self.atd.configure(font="-family {Segoe UI} -size 9")
        self.atd.configure(foreground="#000000")
        self.atd.configure(highlightbackground="#d9d9d9")
        self.atd.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Attendance2.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.atd.configure(image=_img1)
        self.atd.configure(relief="groove")

        #Student Enrollment Option
        self.stu_en = tk.Button(self.top,command=lambda:self.enroll(controller))
        self.stu_en.place(relx=0.109, rely=0.479, height=160, width=160)
        self.stu_en.configure(activebackground="#d9d9d9")
        self.stu_en.configure(activeforeground="black")
        self.stu_en.configure(background="#d9d9d9")
        self.stu_en.configure(disabledforeground="#a3a3a3")
        self.stu_en.configure(foreground="#000000")
        self.stu_en.configure(highlightbackground="#d9d9d9")
        self.stu_en.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Enrollment2.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.stu_en.configure(image=_img2)
        self.stu_en.configure(relief="groove")

        #Message Option
        self.msg = tk.Button(self.top,command=lambda:self.msg_adm(controller))
        self.msg.place(relx=0.328, rely=0.479, height=160, width=160)
        self.msg.configure(activebackground="#d9d9d9")
        self.msg.configure(activeforeground="black")
        self.msg.configure(background="#d9d9d9")
        self.msg.configure(disabledforeground="#a3a3a3")
        self.msg.configure(font="-family {Segoe UI} -size 9")
        self.msg.configure(foreground="#000000")
        self.msg.configure(highlightbackground="#d9d9d9")
        self.msg.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Message2.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.msg.configure(image=_img3)
        self.msg.configure(relief="groove")


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
        photo_location = os.path.join(_location,"../Image/Logout_button2.png")
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
