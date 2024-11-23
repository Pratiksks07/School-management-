#Importing Required modules
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from sql import login


_location = os.path.dirname(__file__) #Stores the path of the current file


# Login page class
class loginpage(tk.Frame):

    def __init__(self, parent, controller):

        #Initating tkinter frame
        tk.Frame.__init__(self, parent,height=1020,width=1960)
        self.configure(background="#d9d9d9")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")
        

        self.top = self


        #Assigning variables for entry box
        global id_var,passw_var
        id_var=tk.StringVar()
        passw_var=tk.StringVar()

        # Canvas in which all elements are kept
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


        #Entry Box For User Id
        self.EnterID = tk.Entry(self.Canvas1, textvariable= id_var)
        self.EnterID.place(relx=0.1, rely=0.39, height=30, relwidth=0.550)
        self.EnterID.configure(background="#f2f6fe")   
        self.EnterID.configure(font="TkFixedFont -20")
        

        #Entry Box for Password
        self.Enterpsword = tk.Entry(self.Canvas1, textvariable= passw_var, show="*")
        self.Enterpsword.place(relx=0.1, rely=0.548, height=30, relwidth=0.550)
        self.Enterpsword.configure(background="#f2f6fe")
        self.Enterpsword.configure(font="TkFixedFont -20")
        

        #User Id Text
        self.USERID = tk.Label(self.Canvas1)
        self.USERID.place(relx=0.1, rely=0.332, height=31, width=114)
        self.USERID.configure(anchor='w')
        self.USERID.configure(background="#dbe6ff")
        self.USERID.configure(compound='left')
        self.USERID.configure(font="-family {Segoe UI Black} -size 14 -weight bold")
        self.USERID.configure(text='''USER ID''')


        #Password Text
        self.PASSWORD = tk.Label(self.Canvas1)
        self.PASSWORD.place(relx=0.1, rely=0.505, height=21, width=174)
        self.PASSWORD.configure(anchor='w')
        self.PASSWORD.configure(background="#dbe6ff")
        self.PASSWORD.configure(compound='left')
        self.PASSWORD.configure(font="-family {Segoe UI Black} -size 14 -weight bold")
        self.PASSWORD.configure(text='''PASSWORD''')


        #Submit Button
        self.SUBMIT = tk.Button(self.Canvas1, command= lambda: login(id_var,passw_var,self,controller))
        self.SUBMIT.place(relx=0.305, rely=0.635, height=60, width=185)
        self.SUBMIT.configure(background="#f2f6fe")
        self.SUBMIT.configure(font="-family {Segoe UI Emoji} -size 12 -weight bold")
        photo_location = os.path.join(_location,"../Image/login_button(1).png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.SUBMIT.configure(image=_img3)
        self.SUBMIT.configure(relief="flat")
        self.SUBMIT.configure(text='''SUBMIT''')


        #User Icon
        self.img = tk.Button(self.Canvas1,relief=tk.FLAT)
        self.img.place(relx=0.305, rely=0.135, height=100, width=100)
        self.img.configure(background="#f2f6fe")
        self.img.configure(font="-family {Segoe UI Emoji} -size 12 -weight bold")
        photo_location = os.path.join(_location,"../Image/user_icon.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.img.configure(image=_img2)
        self.img.configure(relief="flat")
        self.img.config(command=lambda: None)


        #Background Image
        self.IMAGE = tk.Label(self.top)
        self.IMAGE.place(relx=-0.0, rely=0.0, height=680, width=805)
        self.IMAGE.configure(anchor='w')
        self.IMAGE.configure(background="#d9d9d9")
        self.IMAGE.configure(compound='left')
        photo_location = os.path.join(_location,"../Image/FLEX.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.IMAGE.configure(image=_img0)
        self.IMAGE.configure(text='''USER ID:''')


    # Functions for switching between pages
    def admin(self,controller):
        from adm_wlcm import admin
        controller.show_frame(admin)

    def student(self,controller):
        from stu_wlcm import student
        controller.show_frame(student)

