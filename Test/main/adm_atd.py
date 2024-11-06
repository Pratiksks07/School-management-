import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from sql import *

_location = os.path.dirname(__file__)

class atd_admin(tk.Frame):
    def __init__(self, parent, controller):
        user = tk.StringVar()
        total = tk.StringVar()
        present = tk.StringVar()
        absenet = tk.StringVar()

        tk.Frame.__init__(self, parent,height=1020,width=1960)

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

        self.heading = tk.Label(self.top)
        self.heading.place(relx=0.065, rely=0.0, relheight=0.200
                , relwidth=0.600)
        self.heading.configure(activebackground="#dbe6ff")
        self.heading.configure(activeforeground="black")
        self.heading.configure(anchor='w')
        self.heading.configure(background="#8AA3F7")
        self.heading.configure(compound='left')
        self.heading.configure(disabledforeground="#a3a3a3")
        self.heading.configure(font="-family {Sitka Display} -size 55 -weight bold")
        self.heading.configure(foreground="#000000")
        self.heading.configure(highlightbackground="#d9d9d9")
        self.heading.configure(highlightcolor="#000000")
        self.heading.configure(text='''Attendance''')

        self.calender = tk.Label(self.top)
        self.calender.place(relx=0.800, rely=0.0, height=150, width=150)  # Adjusted position for visibility
        self.calender.configure(
            background="#d9d9d9",
            foreground="#000000",
            anchor='center')
        photo_location = os.path.join(os.path.dirname(__file__), "../Image/calender.png")
        self.admi_img = tk.PhotoImage(file=photo_location)
        self.calender.configure(image=self.admi_img)
        self.calender.configure(relief="flat")


        self.enter_total = tk.Entry(self.top, textvariable=total)
        self.enter_total.place(relx=0.609, rely=0.331, height=30, relwidth=0.128)

        self.enter_total.configure(background="white")
        self.enter_total.configure(disabledforeground="#a3a3a3")
        self.enter_total.configure(font="TkFixedFont 15")
        self.enter_total.configure(foreground="#000000")
        self.enter_total.configure(highlightbackground="#d9d9d9")
        self.enter_total.configure(highlightcolor="#000000")
        self.enter_total.configure(insertbackground="#000000")
        self.enter_total.configure(selectbackground="#d9d9d9")
        self.enter_total.configure(selectforeground="black")

        self.Enter_present = tk.Entry(self.top, textvariable= present)
        self.Enter_present.place(relx=0.609, rely=0.424, height=30
                , relwidth=0.128)
        self.Enter_present.configure(background="white")
        self.Enter_present.configure(disabledforeground="#a3a3a3")
        self.Enter_present.configure(font="TkFixedFont 15")
        self.Enter_present.configure(foreground="#000000")
        self.Enter_present.configure(highlightbackground="#d9d9d9")
        self.Enter_present.configure(highlightcolor="#000000")
        self.Enter_present.configure(insertbackground="#000000")
        self.Enter_present.configure(selectbackground="#d9d9d9")
        self.Enter_present.configure(selectforeground="black")

        self.Button1 = tk.Button(self.top, command=lambda:self.admin(controller))
        self.Button1.place(relx=0.823, rely=0.888, height=60, width=160)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#f2f6fe")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''BACK''')
        photo_location = os.path.join(_location,"../Image/Back_button.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img2)
        self.Button1.configure(relief="flat")

        self.Absent = tk.Label(self.top)
        self.Absent.place(relx=0.523, rely=0.508, height=40, width=105)
        self.Absent.configure(activebackground="#d9d9d9")
        self.Absent.configure(activeforeground="black")
        self.Absent.configure(anchor='w')
        self.Absent.configure(background="#dbe6ff")
        self.Absent.configure(compound='left')
        self.Absent.configure(disabledforeground="#a3a3a3")
        self.Absent.configure(font="-family {Segoe UI Variable Display} -size 18 -weight bold")
        self.Absent.configure(foreground="#000000")
        self.Absent.configure(highlightbackground="#d9d9d9")
        self.Absent.configure(highlightcolor="#000000")
        self.Absent.configure(text='''Absent:''')

        self.total = tk.Label(self.top)
        self.total.place(relx=0.523, rely=0.324, height=41, width=76)
        self.total.configure(activebackground="#d9d9d9")
        self.total.configure(activeforeground="black")
        self.total.configure(anchor='w')
        self.total.configure(background="#dbe6ff")
        self.total.configure(compound='left')
        self.total.configure(disabledforeground="#a3a3a3")
        self.total.configure(font="-family {Segoe UI Variable Display} -size 18 -weight bold")
        self.total.configure(foreground="#000000")
        self.total.configure(highlightbackground="#d9d9d9")
        self.total.configure(highlightcolor="#000000")
        self.total.configure(text='''Total:''')

        self.sec = tk.Label(self.top)
        self.sec.place(relx=0.063, rely=0.724, height=31, width=52)
        self.sec.configure(activebackground="#d9d9d9")
        self.sec.configure(activeforeground="black")
        self.sec.configure(anchor='w')
        self.sec.configure(background="#dbe6ff")
        self.sec.configure(compound='left')
        self.sec.configure(disabledforeground="#a3a3a3")
        self.sec.configure(font="-family {Segoe UI Variable Display} -size 15 -weight bold")
        self.sec.configure(foreground="#000000")
        self.sec.configure(highlightbackground="#d9d9d9")
        self.sec.configure(highlightcolor="#000000")
        self.sec.configure(text='''Sec:''')

        self.student_id = tk.Label(self.top)
        self.student_id.place(relx=0.063, rely=0.324, height=41, width=272)
        self.student_id.configure(activebackground="#d9d9d9")
        self.student_id.configure(activeforeground="black")
        self.student_id.configure(anchor='w')
        self.student_id.configure(background="#dbe6ff")
        self.student_id.configure(compound='left')
        self.student_id.configure(disabledforeground="#a3a3a3")
        self.student_id.configure(font="-family {Segoe UI Variable Display} -size 24 -weight bold")
        self.student_id.configure(foreground="#000000")
        self.student_id.configure(highlightbackground="#d9d9d9")
        self.student_id.configure(highlightcolor="#000000")
        self.student_id.configure(text='''Enter Student Id:''')

        self.present = tk.Label(self.top)
        self.present.place(relx=0.523, rely=0.416, height=31, width=96)
        self.present.configure(activebackground="#d9d9d9")
        self.present.configure(activeforeground="black")
        self.present.configure(anchor='w')
        self.present.configure(background="#dbe6ff")
        self.present.configure(compound='left')
        self.present.configure(disabledforeground="#a3a3a3")
        self.present.configure(font="-family {Segoe UI Variable Display} -size 18 -weight bold")
        self.present.configure(foreground="#000000")
        self.present.configure(highlightbackground="#d9d9d9")
        self.present.configure(highlightcolor="#000000")
        self.present.configure(text='''Present:''')

        self.submit = tk.Button(self.top,command=lambda:percentage(self,user,total,present,absenet))
        self.submit.place(relx=0.615, rely=0.605, height=60, width=160)
        self.submit.configure(activebackground="#d9d9d9")
        self.submit.configure(activeforeground="black")
        self.submit.configure(background="#f2f6fe")
        self.submit.configure(disabledforeground="#a3a3a3")
        self.submit.configure(font="-family {Segoe UI Black} -size 11 -weight bold")
        self.submit.configure(foreground="#000000")
        self.submit.configure(highlightbackground="#d9d9d9")
        self.submit.configure(highlightcolor="#000000")
        self.submit.configure(text='''SUBMIT''')
        photo_location = os.path.join(_location,"../Image/Submit_button.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.submit.configure(image=_img3)
        self.submit.configure(relief="flat")


        self.Enter_student_id = tk.Entry(self.top, textvariable= user)
        self.Enter_student_id.place(relx=0.063, rely=0.416, height=25
                , relwidth=0.214)
        self.Enter_student_id.configure(background="white")
        self.Enter_student_id.configure(disabledforeground="#a3a3a3")
        self.Enter_student_id.configure(font="TkFixedFont 15")
        self.Enter_student_id.configure(foreground="#000000")
        self.Enter_student_id.configure(highlightbackground="#d9d9d9")
        self.Enter_student_id.configure(highlightcolor="#000000")
        self.Enter_student_id.configure(insertbackground="#000000")
        self.Enter_student_id.configure(selectbackground="#d9d9d9")
        self.Enter_student_id.configure(selectforeground="black")

        self.roll_no = tk.Label(self.top)
        self.roll_no.place(relx=0.063, rely=0.786, height=31, width=84)
        self.roll_no.configure(activebackground="#d9d9d9")
        self.roll_no.configure(activeforeground="black")
        self.roll_no.configure(anchor='w')
        self.roll_no.configure(background="#dbe6ff")
        self.roll_no.configure(compound='left')
        self.roll_no.configure(disabledforeground="#a3a3a3")
        self.roll_no.configure(font="-family {Segoe UI Variable Display} -size 15 -weight bold")
        self.roll_no.configure(foreground="#000000")
        self.roll_no.configure(highlightbackground="#d9d9d9")
        self.roll_no.configure(highlightcolor="#000000")
        self.roll_no.configure(text='''Roll no :''')

        self.name = tk.Label(self.top)
        self.name.place(relx=0.063, rely=0.601, height=21, width=61)
        self.name.configure(activebackground="#d9d9d9")
        self.name.configure(activeforeground="black")
        self.name.configure(anchor='w')
        self.name.configure(background="#dbe6ff")
        self.name.configure(compound='left')
        self.name.configure(disabledforeground="#a3a3a3")
        self.name.configure(font="-family {Segoe UI Variable Display} -size 14 -weight bold")
        self.name.configure(foreground="#000000")
        self.name.configure(highlightbackground="#d9d9d9")
        self.name.configure(highlightcolor="#000000")
        self.name.configure(text='''Name:''')

        self.cls = tk.Label(self.top)
        self.cls.place(relx=0.063, rely=0.663, height=31, width=74)
        self.cls.configure(activebackground="#d9d9d9")
        self.cls.configure(activeforeground="black")
        self.cls.configure(anchor='w')
        self.cls.configure(background="#dbe6ff")
        self.cls.configure(compound='left')
        self.cls.configure(disabledforeground="#a3a3a3")
        self.cls.configure(font="-family {Segoe UI Variable Display} -size 15 -weight bold")
        self.cls.configure(foreground="#000000")
        self.cls.configure(highlightbackground="#d9d9d9")
        self.cls.configure(highlightcolor="#000000")
        self.cls.configure(text='''Class:''')

        self.percent = tk.Label(self.top)
        self.percent.place(relx=0.531, rely=0.74, height=41, width=103)
        self.percent.configure(activebackground="#d9d9d9")
        self.percent.configure(activeforeground="black")
        self.percent.configure(anchor='w')
        self.percent.configure(background="#dbe6ff")
        self.percent.configure(compound='left')
        self.percent.configure(disabledforeground="#a3a3a3")
        self.percent.configure(font="-family {Segoe UI Variable Display} -size 18 -weight bold")
        self.percent.configure(foreground="#000000")
        self.percent.configure(highlightbackground="#d9d9d9")
        self.percent.configure(highlightcolor="#000000")
        self.percent.configure(text='''Percent:''')

        self.Enter_absent = tk.Entry(self.top, textvariable = absenet)
        self.Enter_absent.place(relx=0.609, rely=0.516, height=30
                , relwidth=0.128)
        self.Enter_absent.configure(background="white")
        self.Enter_absent.configure(disabledforeground="#a3a3a3")
        self.Enter_absent.configure(font="TkFixedFont 15")
        self.Enter_absent.configure(foreground="#000000")
        self.Enter_absent.configure(highlightbackground="#d9d9d9")
        self.Enter_absent.configure(highlightcolor="#000000")
        self.Enter_absent.configure(insertbackground="#000000")
        self.Enter_absent.configure(selectbackground="#d9d9d9")
        self.Enter_absent.configure(selectforeground="black")

        self.enter_percent = tk.Text(self.top)
        self.enter_percent.place(relx=0.613, rely=0.74, relheight=0.052
                , relwidth=0.136)
        self.enter_percent.configure(background="white")
        self.enter_percent.configure(font="TkTextFont 18")
        self.enter_percent.configure(foreground="black")
        self.enter_percent.configure(highlightbackground="#d9d9d9")
        self.enter_percent.configure(highlightcolor="#000000")
        self.enter_percent.configure(insertbackground="#000000")
        self.enter_percent.configure(selectbackground="#d9d9d9")
        self.enter_percent.configure(selectforeground="black")
        self.enter_percent.configure(wrap="word")
        self.enter_percent.bind("<Button-1>", lambda e: "break")
        self.enter_percent.bind("<Key>", lambda e: "break")

        self.enter_name = tk.Text(self.top)
        self.enter_name.place(relx=0.133, rely=0.601, relheight=0.037
                , relwidth=0.152)
        self.enter_name.configure(background="white")
        self.enter_name.configure(font="TkTextFont 15")
        self.enter_name.configure(foreground="black")
        self.enter_name.configure(highlightbackground="#d9d9d9")
        self.enter_name.configure(highlightcolor="#000000")
        self.enter_name.configure(insertbackground="#000000")
        self.enter_name.configure(selectbackground="#d9d9d9")
        self.enter_name.configure(selectforeground="black")
        self.enter_name.configure(wrap="word")
        self.enter_name.bind("<Button-1>", lambda e: "break")
        self.enter_name.bind("<Key>", lambda e: "break")

        self.enter_class = tk.Text(self.top)
        self.enter_class.place(relx=0.133, rely=0.663, relheight=0.037
                , relwidth=0.152)
        self.enter_class.configure(background="white")
        self.enter_class.configure(font="TkTextFont 15")
        self.enter_class.configure(foreground="black")
        self.enter_class.configure(highlightbackground="#d9d9d9")
        self.enter_class.configure(highlightcolor="#000000")
        self.enter_class.configure(insertbackground="#000000")
        self.enter_class.configure(selectbackground="#d9d9d9")
        self.enter_class.configure(selectforeground="black")
        self.enter_class.configure(wrap="word")
        self.enter_class.bind("<Button-1>", lambda e: "break")
        self.enter_class.bind("<Key>", lambda e: "break")

        self.enter_sec = tk.Text(self.top)
        self.enter_sec.place(relx=0.133, rely=0.724, relheight=0.037
                , relwidth=0.152)
        self.enter_sec.configure(background="white")
        self.enter_sec.configure(font="TkTextFont 15")
        self.enter_sec.configure(foreground="black")
        self.enter_sec.configure(highlightbackground="#d9d9d9")
        self.enter_sec.configure(highlightcolor="#000000")
        self.enter_sec.configure(insertbackground="#000000")
        self.enter_sec.configure(selectbackground="#d9d9d9")
        self.enter_sec.configure(selectforeground="black")
        self.enter_sec.configure(wrap="word")
        self.enter_sec.bind("<Button-1>", lambda e: "break")
        self.enter_sec.bind("<Key>", lambda e: "break")

        self.enter_roll = tk.Text(self.top)
        self.enter_roll.place(relx=0.133, rely=0.794, relheight=0.037
                , relwidth=0.152)
        self.enter_roll.configure(background="white")
        self.enter_roll.configure(font="TkTextFont 15")
        self.enter_roll.configure(foreground="black")
        self.enter_roll.configure(highlightbackground="#d9d9d9")
        self.enter_roll.configure(highlightcolor="#000000")
        self.enter_roll.configure(insertbackground="#000000")
        self.enter_roll.configure(selectbackground="#d9d9d9")
        self.enter_roll.configure(selectforeground="black")
        self.enter_roll.configure(wrap="word")
        self.enter_roll.bind("<Button-1>", lambda e: "break")
        self.enter_roll.bind("<Key>", lambda e: "break")


        self.search = tk.Button(self.top, command=lambda: func(self,user))
        self.search.place(relx=0.285, rely=0.390, height=60, width=160)
        self.search.configure(activebackground="#d9d9d9")
        self.search.configure(activeforeground="black")
        self.search.configure(background="#f2f6fe")
        self.search.configure(disabledforeground="#a3a3a3")
        self.search.configure(foreground="#000000")
        self.search.configure(highlightbackground="#d9d9d9")
        self.search.configure(highlightcolor="#000000")
        self.search.configure(text='''Search''')
        photo_location = os.path.join(_location,"../Image/Search_button.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.search.configure(image=_img4)
        self.search.configure(relief="flat")

        


    def admin(self,controller):
        from adm_wlcm import admin
        controller.show_frame(admin)
        self.enter_name.delete("1.0", "end")
        self.enter_class.delete("1.0", "end")
        self.enter_sec.delete("1.0", "end")
        self.enter_roll.delete("1.0", "end")
        self.Enter_present.delete(0, tk.END)
        self.Enter_absent.delete(0, tk.END)
        self.enter_percent.delete("1.0", "end")
        self.Enter_student_id.delete(0, tk.END)
        self.enter_total.delete(0, tk.END)



    global stu_fetch
    def stu_fetch(self):
        from sql import show
        self.enter_name.insert(END,show(0))
        self.enter_class.insert(END,show(1))
        self.enter_sec.insert(END,show(2))
        self.enter_roll.insert(END,show(3))

        self.Enter_present.delete(0, tk.END)
        self.Enter_absent.delete(0, tk.END)
        self.enter_percent.delete("1.0", "end")
        self.enter_total.delete(0, tk.END)

    global func
    def func(self,id):
        uid = id.get()
        
        self.enter_name.delete("1.0", "end")
        self.enter_class.delete("1.0", "end")
        self.enter_sec.delete("1.0", "end")
        self.enter_roll.delete("1.0", "end")


        stu_details(self,uid)
        stu_fetch(self)

        #id.set("")
        
    global percentage
    def percentage (self,id,t,p,a):
        self.enter_percent.delete("1.0", "end")
        uid = id.get()
        pres = p.get()
        total = t.get()
        ab = a.get()
        atd_update(uid,pres,ab,total)
        percn = show_percent()
        self.enter_percent.insert(END,percn)
        
    
        
