# Importing Modules
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from sql import *


_location = os.path.dirname(__file__) #Stores the path of the current file


# Student Profile page class
class profile_stu(tk.Frame):
    

    def __init__(self, parent, controller):
        
        
        tk.Frame.__init__(self, parent,height=1020,width=1960)
        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")


        self.top = self


        # Top border
        self.upper = tk.Label(self.top)
        self.upper.place(relx=0.001, rely=0.0, relheight=0.240
                , relwidth=0.999)
        self.upper.configure(background="#8AA3F7")
        self.upper.configure(relief="raised")


        # Profile Message 
        self.heading = tk.Message(self.top)
        self.heading.place(relx=0.065, rely=0.0, relheight=0.200
                , relwidth=0.600)
        self.heading.configure(background="#8AA3F7")
        self.heading.configure(font="-family {Sitka Display} -size 55 -weight bold")
        self.heading.configure(padx="1")
        self.heading.configure(pady="1")
        self.heading.configure(text='''Profile''')
        self.heading.configure(width=600)
        self.heading.configure(anchor="w")


        #Top Border Icon
        self.akela = tk.Label(self.top)
        self.akela.place(relx=0.800, rely=0.0, height=150, width=150)  # Adjusted position for visibility
        self.akela.configure(
            background="#d9d9d9",
            foreground="#000000",
            anchor='center')
        photo_location = os.path.join(os.path.dirname(__file__), "../Image/akela.png")
        self.akela_img = tk.PhotoImage(file=photo_location)
        self.akela.configure(image=self.akela_img)
        self.akela.configure(relief="flat")

        
        # Phone Text Box
        self.tphone = tk.Text(self.top)
        self.tphone.place(relx=0.242, rely=0.893, relheight=0.040
                , relwidth=0.175)
        self.tphone.configure(background="#f2f6fe")
        self.tphone.configure(font="TkTextFont 15")
        self.tphone.configure(wrap="word")
        self.tphone.bind("<Key>", lambda e: "break")
        self.tphone.bind("<Button-1>", lambda e: "break")
        
        # Address Text Box
        self.tadd = tk.Text(self.top)
        self.tadd.place(relx=0.242, rely=0.817, relheight=0.040
                , relwidth=0.175)
        self.tadd.configure(background="#f2f6fe")
        self.tadd.configure(font="TkTextFont 15")
        self.tadd.configure(wrap="word")
        self.tadd.bind("<Key>", lambda e: "break")
        self.tadd.bind("<Button-1>", lambda e: "break")
        

        # Mother's name Text Box
        self.tmname = tk.Text(self.top)
        self.tmname.place(relx=0.242, rely=0.741, relheight=0.040
                , relwidth=0.175)
        self.tmname.configure(background="#f2f6fe")
        self.tmname.configure(font="TkTextFont 15")
        self.tmname.configure(wrap="word")
        self.tmname.bind("<Key>", lambda e: "break")
        self.tmname.bind("<Button-1>", lambda e: "break")
        

        # Father's name Text Box
        self.tfname = tk.Text(self.top)
        self.tfname.place(relx=0.242, rely=0.664, relheight=0.040, relwidth=0.175)
        self.tfname.configure(background="#f2f6fe")
        self.tfname.configure(font="TkTextFont 15")
        self.tfname.configure(wrap="word")
        self.tfname.bind("<Key>", lambda e: "break")
        self.tfname.bind("<Button-1>", lambda e: "break")
        

        # Adm no Text Box
        self.tadm = tk.Text(self.top)
        self.tadm.place(relx=0.242, rely=0.588, relheight=0.040
                , relwidth=0.175)
        self.tadm.configure(background="#f2f6fe")
        self.tadm.configure(font="TkTextFont 15")
        self.tadm.configure(wrap="word")
        self.tadm.bind("<Key>", lambda e: "break")
        self.tadm.bind("<Button-1>", lambda e: "break")
        

        # Roll Text Box
        self.troll = tk.Text(self.top)
        self.troll.place(relx=0.242, rely=0.512, relheight=0.040
                , relwidth=0.175)
        self.troll.configure(background="#f2f6fe")
        self.troll.configure(font="TkTextFont 15")
        self.troll.configure(wrap="word")
        self.troll.bind("<Key>", lambda e: "break")
        self.troll.bind("<Button-1>", lambda e: "break")

        # Sec Text Box
        self.tsec = tk.Text(self.top)
        self.tsec.place(relx=0.242, rely=0.436, relheight=0.040
                , relwidth=0.175)
        self.tsec.configure(background="#f2f6fe")
        self.tsec.configure(font="TkTextFont 15")
        self.tsec.configure(wrap="word")
        self.tsec.bind("<Key>", lambda e: "break")
        self.tsec.bind("<Button-1>", lambda e: "break")

        # Name Text Box
        self.tname = tk.Text(self.top)
        self.tname.place(relx=0.242, rely=0.284, relheight=0.040
                , relwidth=0.175)
        self.tname.configure(background="#f2f6fe")
        self.tname.configure(font="TkTextFont 15")
        self.tname.configure(wrap="word")
        self.tname.bind("<Key>", lambda e: "break")
        self.tname.bind("<Button-1>", lambda e: "break")
        
        # Class Text Box
        self.tclass = tk.Text(self.top)
        self.tclass.place(relx=0.242, rely=0.360, relheight=0.040
                , relwidth=0.175)
        self.tclass.configure(background="#f2f6fe")
        self.tclass.configure(font="TkTextFont 15")
        self.tclass.configure(wrap="word")
        self.tclass.bind("<Key>", lambda e: "break")
        self.tclass.bind("<Button-1>", lambda e: "break")

        
        #Show Button
        self.Button = tk.Button(self.top,command=lambda:self.fetch1(controller))
        self.Button.place(relx=0.470, rely=0.898, height=60, width=160)
        self.Button.configure(background="#dbe6ff")
        self.Button.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Button.configure(text='''SHOW''')
        photo_location = os.path.join(_location,"../Image/Show_button.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Button.configure(image=_img4)
        self.Button.configure(relief="flat")


        #Back Button
        self.Button1 = tk.Button(self.top,command=lambda:self.student(controller))
        self.Button1.place(relx=0.833, rely=0.898, height=60, width=160)
        self.Button1.configure(background="#dbe6ff")
        self.Button1.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Button1.configure(text='''BACK''')
        photo_location = os.path.join(_location,"../Image/Back_button.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img3)
        self.Button1.configure(relief="flat")


        #Top Icon Image
        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.600, rely=0.310, height=352, width=381)
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        photo_location = os.path.join(_location,"..\\Image\\profile_icon.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(relief="flat")
        self.Label1.configure(anchor="center")
        

        #Name Message
        self.name = tk.Message(self.top)
        self.name.place(relx=0.086, rely=0.274, relheight=0.058, relwidth=0.063)
        self.name.configure(background="#dbe6ff")
        self.name.configure(font="-family {Arial} -size 16 -weight bold")
        self.name.configure(padx="1")
        self.name.configure(pady="1")
        self.name.configure(text='''Name :''')
        self.name.configure(width=81)

        #Class Message
        self.cls = tk.Message(self.top)
        self.cls.place(relx=0.075, rely=0.35, relheight=0.044, relwidth=0.08)
        self.cls.configure(background="#dbe6ff")
        self.cls.configure(font="-family {Arial} -size 16 -weight bold")
        self.cls.configure(padx="1")
        self.cls.configure(pady="1")
        self.cls.configure(text='''Class :''')
        self.cls.configure(width=101)

        #Sec Message 
        self.sec = tk.Message(self.top)
        self.sec.place(relx=0.07, rely=0.411, relheight=0.075, relwidth=0.08)
        self.sec.configure(background="#dbe6ff")
        self.sec.configure(cursor="fleur")
        self.sec.configure(font="-family {Arial} -size 16 -weight bold")
        self.sec.configure(padx="1")
        self.sec.configure(pady="1")
        self.sec.configure(text='''Sec :''')
        self.sec.configure(width=102)

        #Roll Message
        self.roll = tk.Message(self.top)
        self.roll.place(relx=0.068, rely=0.502, relheight=0.044, relwidth=0.109)
        self.roll.configure(background="#dbe6ff")
        self.roll.configure(font="-family {Arial} -size 16 -weight bold")
        self.roll.configure(padx="1")
        self.roll.configure(pady="1")
        self.roll.configure(text='''Roll no :''')
        self.roll.configure(width=140)

        #Adm No. Message
        self.adm = tk.Message(self.top)
        self.adm.place(relx=0.07, rely=0.578, relheight=0.059, relwidth=0.109)
        self.adm.configure(background="#dbe6ff")
        self.adm.configure(font="-family {Arial} -size 16 -weight bold")
        self.adm.configure(padx="1")
        self.adm.configure(pady="1")
        self.adm.configure(text='''Adm no :''')
        self.adm.configure(width=140)

        #Father's Name Message
        self.fname = tk.Message(self.top)
        self.fname.place(relx=0.068, rely=0.654, relheight=0.058, relwidth=0.163)
        self.fname.configure(background="#dbe6ff")
        self.fname.configure(font="-family {Arial} -size 16 -weight bold")
        self.fname.configure(padx="1")
        self.fname.configure(pady="1")
        self.fname.configure(text='''Father's Name :''')
        self.fname.configure(width=208)

        #Mother's Name Message
        self.mname = tk.Message(self.top)
        self.mname.place(relx=0.07, rely=0.731, relheight=0.058
                , relwidth=0.163)
        self.mname.configure(background="#dbe6ff")
        self.mname.configure(font="-family {Arial} -size 16 -weight bold")
        self.mname.configure(padx="1")
        self.mname.configure(pady="1")
        self.mname.configure(text='''Mother's Name :''')
        self.mname.configure(width=208)

        #Address Message
        self.add = tk.Message(self.top)
        self.add.place(relx=0.08, rely=0.807, relheight=0.043
                , relwidth=0.095)
        self.add.configure(background="#dbe6ff")
        self.add.configure(font="-family {Arial} -size 16 -weight bold")
        self.add.configure(padx="1")
        self.add.configure(pady="1")
        self.add.configure(text='''Address :''')
        self.add.configure(width=121)

        #Phone Message
        self.phone = tk.Message(self.top)
        self.phone.place(relx=0.073, rely=0.883, relheight=0.043
                , relwidth=0.095)
        self.phone.configure(background="#dbe6ff")
        self.phone.configure(font="-family {Arial} -size 16 -weight bold")
        self.phone.configure(padx="1")
        self.phone.configure(pady="1")
        self.phone.configure(text='''Phone :''')
        self.phone.configure(width=121)


     #Function for switching pages
    def student(self,controller):
        from stu_wlcm import student
        controller.show_frame(student)
        #Set all the boxes blank
        self.tphone.delete("1.0", "end")
        self.tadd.delete("1.0", "end")
        self.tmname.delete("1.0", "end")
        self.tfname.delete("1.0", "end")
        self.tadm.delete("1.0", "end")
        self.troll.delete("1.0", "end")
        self.tsec.delete("1.0", "end")
        self.tclass.delete("1.0", "end")
        self.tname.delete("1.0", "end")
        
    
    def fetch1(self,controller):
        from sql import fetch
        #Insert Data in the boxes
        self.tphone.insert(END,fetch(8))
        self.tadd.insert(END,fetch(7))
        self.tmname.insert(END,fetch(6))
        self.tfname.insert(END,fetch(5))
        self.tadm.insert(END,fetch(4))
        self.troll.insert(END,fetch(3))
        self.tsec.insert(END,fetch(2))
        self.tclass.insert(END,fetch(1))
        self.tname.insert(END,fetch(0))

