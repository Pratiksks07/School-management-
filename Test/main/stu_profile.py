import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from sql import *

_location = os.path.dirname(__file__)

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'





class profile_stu(tk.Frame):
    
    #global tname,tmname,tfname,tclass,tadm,tadd,tphone,troll,tsec

    def __init__(self, parent, controller):
        
        
        tk.Frame.__init__(self, parent,height=1020,width=1960)
        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        self.top = self

        self.upper = tk.Label(self.top)
        self.upper.place(relx=0.001, rely=0.0, relheight=0.240
                , relwidth=0.999)
        self.upper.configure(background="#8AA3F7")
        self.upper.configure(foreground="#000000")
        self.upper.configure(highlightbackground="#d9d9d9")
        self.upper.configure(highlightcolor="#000000")
        self.upper.configure(relief="raised")

        self.heading = tk.Message(self.top)
        self.heading.place(relx=0.065, rely=0.0, relheight=0.200
                , relwidth=0.600)
        self.heading.configure(background="#8AA3F7")
        self.heading.configure(font="-family {Sitka Display} -size 55 -weight bold")
        self.heading.configure(foreground="#000000")
        self.heading.configure(highlightbackground="#d9d9d9")
        self.heading.configure(highlightcolor="#000000")
        self.heading.configure(padx="1")
        self.heading.configure(pady="1")
        self.heading.configure(text='''Profile''')
        self.heading.configure(width=600)
        self.heading.configure(anchor="w")

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

        
        self.tphone = tk.Text(self.top)
        self.tphone.place(relx=0.242, rely=0.893, relheight=0.040
                , relwidth=0.175)
        self.tphone.configure(background="#f2f6fe")
        self.tphone.configure(font="TkTextFont 15")
        self.tphone.configure(foreground="black")
        self.tphone.configure(highlightbackground="#d9d9d9")
        self.tphone.configure(highlightcolor="#000000")
        self.tphone.configure(insertbackground="#000000")
        self.tphone.configure(selectbackground="#d9d9d9")
        self.tphone.configure(selectforeground="black")
        self.tphone.configure(wrap="word")
        self.tphone.bind("<Key>", lambda e: "break")
        self.tphone.bind("<Button-1>", lambda e: "break")
        #self.tphone.insert(END,fetch(8)
        #self.tphone.config(state="disabled")

        self.tadd = tk.Text(self.top)
        self.tadd.place(relx=0.242, rely=0.817, relheight=0.040
                , relwidth=0.175)
        self.tadd.configure(background="#f2f6fe")
        self.tadd.configure(font="TkTextFont 15")
        self.tadd.configure(foreground="black")
        self.tadd.configure(highlightbackground="#d9d9d9")
        self.tadd.configure(highlightcolor="#000000")
        self.tadd.configure(insertbackground="#000000")
        self.tadd.configure(selectbackground="#d9d9d9")
        self.tadd.configure(selectforeground="black")
        self.tadd.configure(wrap="word")
        self.tadd.bind("<Key>", lambda e: "break")
        self.tadd.bind("<Button-1>", lambda e: "break")
        #self.tadd.insert(END,fetch(7)
        #self.tadd.config(state="disabled")


        self.tmname = tk.Text(self.top)
        self.tmname.place(relx=0.242, rely=0.741, relheight=0.040
                , relwidth=0.175)
        self.tmname.configure(background="#f2f6fe")
        self.tmname.configure(font="TkTextFont 15")
        self.tmname.configure(foreground="black")
        self.tmname.configure(highlightbackground="#d9d9d9")
        self.tmname.configure(highlightcolor="#000000")
        self.tmname.configure(insertbackground="#000000")
        self.tmname.configure(selectbackground="#d9d9d9")
        self.tmname.configure(selectforeground="black")
        self.tmname.configure(wrap="word")
        self.tmname.bind("<Key>", lambda e: "break")
        self.tmname.bind("<Button-1>", lambda e: "break")
        #self.tmname.insert(END,fetch(6)
        #self.tmname.config(state="disabled")

        self.tfname = tk.Text(self.top)
        self.tfname.place(relx=0.242, rely=0.664, relheight=0.040, relwidth=0.175)
        self.tfname.configure(background="#f2f6fe")
        self.tfname.configure(font="TkTextFont 15")
        self.tfname.configure(foreground="black")
        self.tfname.configure(highlightbackground="#d9d9d9")
        self.tfname.configure(highlightcolor="#000000")
        self.tfname.configure(insertbackground="#000000")
        self.tfname.configure(selectbackground="#d9d9d9")
        self.tfname.configure(selectforeground="black")
        self.tfname.configure(wrap="word")
        self.tfname.bind("<Key>", lambda e: "break")
        self.tfname.bind("<Button-1>", lambda e: "break")
        #self.tfname.insert(END,fetch(5)
        #self.tfname.config(state="disabled")

        self.tadm = tk.Text(self.top)
        self.tadm.place(relx=0.242, rely=0.588, relheight=0.040
                , relwidth=0.175)
        self.tadm.configure(background="#f2f6fe")
        self.tadm.configure(font="TkTextFont 15")
        self.tadm.configure(foreground="black")
        self.tadm.configure(highlightbackground="#d9d9d9")
        self.tadm.configure(highlightcolor="#000000")
        self.tadm.configure(insertbackground="#000000")
        self.tadm.configure(selectbackground="#d9d9d9")
        self.tadm.configure(selectforeground="black")
        self.tadm.configure(wrap="word")
        self.tadm.bind("<Key>", lambda e: "break")
        self.tadm.bind("<Button-1>", lambda e: "break")
        #self.tadm.insert(END,fetch(4)
        #self.tadm.config(state="disabled")

        self.troll = tk.Text(self.top)
        self.troll.place(relx=0.242, rely=0.512, relheight=0.040
                , relwidth=0.175)
        self.troll.configure(background="#f2f6fe")
        self.troll.configure(font="TkTextFont 15")
        self.troll.configure(foreground="black")
        self.troll.configure(highlightbackground="#d9d9d9")
        self.troll.configure(highlightcolor="#000000")
        self.troll.configure(insertbackground="#000000")
        self.troll.configure(selectbackground="#d9d9d9")
        self.troll.configure(selectforeground="black")
        self.troll.configure(wrap="word")
        self.troll.bind("<Key>", lambda e: "break")
        self.troll.bind("<Button-1>", lambda e: "break")
        #self.troll.insert(END,fetch(3)
        #self.troll.config(state="disabled")

        self.tsec = tk.Text(self.top)
        self.tsec.place(relx=0.242, rely=0.436, relheight=0.040
                , relwidth=0.175)
        self.tsec.configure(background="#f2f6fe")
        self.tsec.configure(font="TkTextFont 15")
        self.tsec.configure(foreground="black")
        self.tsec.configure(highlightbackground="#d9d9d9")
        self.tsec.configure(highlightcolor="#000000")
        self.tsec.configure(insertbackground="#000000")
        self.tsec.configure(selectbackground="#d9d9d9")
        self.tsec.configure(selectforeground="black")
        self.tsec.configure(wrap="word")
        self.tsec.bind("<Key>", lambda e: "break")
        self.tsec.bind("<Button-1>", lambda e: "break")
        #self.tsec.insert(END,fetch(2)
        #self.tsec.config(state="disabled")

        self.tname = tk.Text(self.top)
        self.tname.place(relx=0.242, rely=0.284, relheight=0.040
                , relwidth=0.175)
        self.tname.configure(background="#f2f6fe")
        self.tname.configure(font="TkTextFont 15")
        self.tname.configure(foreground="black")
        self.tname.configure(highlightbackground="#d9d9d9")
        self.tname.configure(highlightcolor="#000000")
        self.tname.configure(insertbackground="#000000")
        self.tname.configure(selectbackground="#d9d9d9")
        self.tname.configure(selectforeground="black")
        self.tname.configure(wrap="word")
        self.tname.bind("<Key>", lambda e: "break")
        self.tname.bind("<Button-1>", lambda e: "break")
        #self.tname.insert(END,fetch(0)
        #self.tname.config(state="disabled")

        self.tclass = tk.Text(self.top)
        self.tclass.place(relx=0.242, rely=0.360, relheight=0.040
                , relwidth=0.175)
        self.tclass.configure(background="#f2f6fe")
        self.tclass.configure(font="TkTextFont 15")
        self.tclass.configure(foreground="black")
        self.tclass.configure(highlightbackground="#d9d9d9")
        self.tclass.configure(highlightcolor="#000000")
        self.tclass.configure(insertbackground="#000000")
        self.tclass.configure(selectbackground="#d9d9d9")
        self.tclass.configure(selectforeground="black")
        self.tclass.configure(wrap="word")
        self.tclass.bind("<Key>", lambda e: "break")
        self.tclass.bind("<Button-1>", lambda e: "break")
        #self.tclass.insert(END,fetch(1)
        #self.tclass.config(state="disabled")

        self.Button = tk.Button(self.top,command=lambda:self.fetch1(controller))
        self.Button.place(relx=0.470, rely=0.898, height=60, width=160)
        self.Button.configure(activebackground="#d9d9d9")
        self.Button.configure(activeforeground="black")
        self.Button.configure(background="#dbe6ff")
        self.Button.configure(disabledforeground="#a3a3a3")
        self.Button.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Button.configure(foreground="#000000")
        self.Button.configure(highlightbackground="#d9d9d9")
        self.Button.configure(highlightcolor="#000000")
        self.Button.configure(text='''SHOW''')
        photo_location = os.path.join(_location,"../Image/Show_button.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Button.configure(image=_img4)
        self.Button.configure(relief="flat")

        self.Button1 = tk.Button(self.top,command=lambda:self.student(controller))
        self.Button1.place(relx=0.833, rely=0.898, height=60, width=160)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#dbe6ff")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''BACK''')
        photo_location = os.path.join(_location,"../Image/Back_button.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img3)
        self.Button1.configure(relief="flat")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.600, rely=0.310, height=352, width=381)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"..\\Image\\profile_icon.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)
        self.Label1.configure(relief="flat")
        self.Label1.configure(anchor="center")
        

        
        self.name = tk.Message(self.top)
        self.name.place(relx=0.086, rely=0.274, relheight=0.058, relwidth=0.063)
        self.name.configure(background="#dbe6ff")
        self.name.configure(font="-family {Arial} -size 16 -weight bold")
        self.name.configure(foreground="#000000")
        self.name.configure(highlightbackground="#d9d9d9")
        self.name.configure(highlightcolor="#000000")
        self.name.configure(padx="1")
        self.name.configure(pady="1")
        self.name.configure(text='''Name :''')
        self.name.configure(width=81)


        self.cls = tk.Message(self.top)
        self.cls.place(relx=0.075, rely=0.35, relheight=0.044, relwidth=0.08)
        self.cls.configure(background="#dbe6ff")
        self.cls.configure(font="-family {Arial} -size 16 -weight bold")
        self.cls.configure(foreground="#000000")
        self.cls.configure(highlightbackground="#d9d9d9")
        self.cls.configure(highlightcolor="#000000")
        self.cls.configure(padx="1")
        self.cls.configure(pady="1")
        self.cls.configure(text='''Class :''')
        self.cls.configure(width=101)

        self.sec = tk.Message(self.top)
        self.sec.place(relx=0.07, rely=0.411, relheight=0.075, relwidth=0.08)
        self.sec.configure(background="#dbe6ff")
        self.sec.configure(cursor="fleur")
        self.sec.configure(font="-family {Arial} -size 16 -weight bold")
        self.sec.configure(foreground="#000000")
        self.sec.configure(highlightbackground="#d9d9d9")
        self.sec.configure(highlightcolor="#000000")
        self.sec.configure(padx="1")
        self.sec.configure(pady="1")
        self.sec.configure(text='''Sec :''')
        self.sec.configure(width=102)

        self.roll = tk.Message(self.top)
        self.roll.place(relx=0.068, rely=0.502, relheight=0.044, relwidth=0.109)
        self.roll.configure(background="#dbe6ff")
        self.roll.configure(font="-family {Arial} -size 16 -weight bold")
        self.roll.configure(foreground="#000000")
        self.roll.configure(highlightbackground="#d9d9d9")
        self.roll.configure(highlightcolor="#000000")
        self.roll.configure(padx="1")
        self.roll.configure(pady="1")
        self.roll.configure(text='''Roll no :''')
        self.roll.configure(width=140)

        self.adm = tk.Message(self.top)
        self.adm.place(relx=0.07, rely=0.578, relheight=0.059, relwidth=0.109)
        self.adm.configure(background="#dbe6ff")
        self.adm.configure(font="-family {Arial} -size 16 -weight bold")
        self.adm.configure(foreground="#000000")
        self.adm.configure(highlightbackground="#d9d9d9")
        self.adm.configure(highlightcolor="#000000")
        self.adm.configure(padx="1")
        self.adm.configure(pady="1")
        self.adm.configure(text='''Adm no :''')
        self.adm.configure(width=140)

        self.fname = tk.Message(self.top)
        self.fname.place(relx=0.068, rely=0.654, relheight=0.058, relwidth=0.163)
        self.fname.configure(background="#dbe6ff")
        self.fname.configure(font="-family {Arial} -size 16 -weight bold")
        self.fname.configure(foreground="#000000")
        self.fname.configure(highlightbackground="#d9d9d9")
        self.fname.configure(highlightcolor="#000000")
        self.fname.configure(padx="1")
        self.fname.configure(pady="1")
        self.fname.configure(text='''Father's Name :''')
        self.fname.configure(width=208)

        self.mname = tk.Message(self.top)
        self.mname.place(relx=0.07, rely=0.731, relheight=0.058
                , relwidth=0.163)
        self.mname.configure(background="#dbe6ff")
        self.mname.configure(font="-family {Arial} -size 16 -weight bold")
        self.mname.configure(foreground="#000000")
        self.mname.configure(highlightbackground="#d9d9d9")
        self.mname.configure(highlightcolor="#000000")
        self.mname.configure(padx="1")
        self.mname.configure(pady="1")
        self.mname.configure(text='''Mother's Name :''')
        self.mname.configure(width=208)

        self.add = tk.Message(self.top)
        self.add.place(relx=0.08, rely=0.807, relheight=0.043
                , relwidth=0.095)
        self.add.configure(background="#dbe6ff")
        self.add.configure(font="-family {Arial} -size 16 -weight bold")
        self.add.configure(foreground="#000000")
        self.add.configure(highlightbackground="#d9d9d9")
        self.add.configure(highlightcolor="#000000")
        self.add.configure(padx="1")
        self.add.configure(pady="1")
        self.add.configure(text='''Address :''')
        self.add.configure(width=121)


        self.phone = tk.Message(self.top)
        self.phone.place(relx=0.073, rely=0.883, relheight=0.043
                , relwidth=0.095)
        self.phone.configure(background="#dbe6ff")
        self.phone.configure(font="-family {Arial} -size 16 -weight bold")
        self.phone.configure(foreground="#000000")
        self.phone.configure(highlightbackground="#d9d9d9")
        self.phone.configure(highlightcolor="#000000")
        self.phone.configure(padx="1")
        self.phone.configure(pady="1")
        self.phone.configure(text='''Phone :''')
        self.phone.configure(width=121)

    def student(self,controller):
        from stu_wlcm import student
        controller.show_frame(student)

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
        self.tphone.insert(END,fetch(8))
        self.tadd.insert(END,fetch(7))
        self.tmname.insert(END,fetch(6))
        self.tfname.insert(END,fetch(5))
        self.tadm.insert(END,fetch(4))
        self.troll.insert(END,fetch(3))
        self.tsec.insert(END,fetch(2))
        self.tclass.insert(END,fetch(1))
        self.tname.insert(END,fetch(0))

