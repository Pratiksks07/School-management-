#Importing Required modules
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from PIL import Image, ImageTk


_location = os.path.dirname(__file__) #Stores the path of the current file


#Admin page class
class admin(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,height=1020,width=1960)
        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")


        self.top = self

        # Background Image
        # Load and set the background image
        background_image_path = os.path.join(_location, "../Image/background.png")
        self.bg_image = Image.open(background_image_path)
        self.bg_image = self.bg_image.resize((1960, 1020), Image.ANTIALIAS)
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
        photo_location = os.path.join(os.path.dirname(__file__), "../Image/Wlcm_adm.png")
        self.wlcm_img = tk.PhotoImage(file=photo_location)
        self.upper.configure(image=self.wlcm_img)
        self.upper.configure(relief="flat")


        # Question Bank Button
        self.Assg = tk.Button(self.top, command= lambda: self.qbank(controller))
        self.Assg.place(relx=0.547, rely=0.479, height=160, width=160)
        self.Assg.configure(background="#d9d9d9")
        self.Assg.configure(font="-family {Segoe UI} -size 9")
        photo_location = os.path.join(_location,"../Image/Question_bank2.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Assg.configure(image=_img0)
        self.Assg.configure(relief="groove")

        
        # Attendence Button
        self.atd = tk.Button(self.top,command=lambda:self.atd_admin(controller))
        self.atd.place(relx=0.766, rely=0.479, height=160, width=160)
        self.atd.configure(background="#d9d9d9")
        self.atd.configure(font="-family {Segoe UI} -size 9")
        photo_location = os.path.join(_location,"../Image/Attendance2.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.atd.configure(image=_img1)
        self.atd.configure(relief="groove")


        # Student Enrollment Button
        self.stu_en = tk.Button(self.top,command=lambda:self.enroll(controller))
        self.stu_en.place(relx=0.109, rely=0.479, height=160, width=160)
        self.stu_en.configure(background="#d9d9d9")
        photo_location = os.path.join(_location,"../Image/Enrollment2.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.stu_en.configure(image=_img2)
        self.stu_en.configure(relief="groove")


        # Message Button
        self.msg = tk.Button(self.top,command=lambda:self.msg_adm(controller))
        self.msg.place(relx=0.328, rely=0.479, height=160, width=160)
        self.msg.configure(background="#d9d9d9")
        self.msg.configure(font="-family {Segoe UI} -size 9")
        photo_location = os.path.join(_location,"../Image/Message2.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.msg.configure(image=_img3)
        self.msg.configure(relief="groove")


        # Logout Button
        self.back = tk.Button(self.top,command=lambda:self.login(controller))
        self.back.place(relx=0.820, rely=0.850, height=60, width=160)
        self.back.configure(background="#f2f6fe")
        self.back.configure(text='''BACK''')
        photo_location = os.path.join(_location,"../Image/Logout_button2.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.back.configure(image=_img4)
        self.back.configure(relief="flat")


    # Functions for switching between pages
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

    def qbank(self,controller):
        from adm_qbank import qbank_adm
        controller.show_frame(qbank_adm)
