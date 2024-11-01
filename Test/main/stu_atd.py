import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from PIL import Image, ImageTk
from sql import *


_location = os.path.dirname(__file__)

class atd_stu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,height=1020,width=1960)
        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        self.top = self

        self.atd = tk.Message(self.top)
        self.atd.place(relx=0.078, rely=0.167, relheight=0.085, relwidth=0.334)
        self.atd.configure(background="#dbe6ff")
        self.atd.configure(font="-family {Sitka Display} -size 48 -weight bold")
        self.atd.configure(foreground="#000000")
        self.atd.configure(highlightbackground="#d9d9d9")
        self.atd.configure(highlightcolor="#000000")
        self.atd.configure(padx="1")
        self.atd.configure(pady="1")
        self.atd.configure(text='''ATTENDENCE''')
        self.atd.configure(width=427)

        self.total = tk.Message(self.top)
        self.total.place(relx=0.117, rely=0.426, relheight=0.044, relwidth=0.076)

        self.total.configure(background="#dbe6ff")
        self.total.configure(font="-family {@Yu Gothic UI Semibold} -size 20 -weight bold")
        self.total.configure(foreground="#000000")
        self.total.configure(highlightbackground="#d9d9d9")
        self.total.configure(highlightcolor="#000000")
        self.total.configure(padx="1")
        self.total.configure(pady="1")
        self.total.configure(text='''Total -''')
        self.total.configure(width=97)

        self.pst = tk.Message(self.top)
        self.pst.place(relx=0.102, rely=0.502, relheight=0.059, relwidth=0.091)
        self.pst.configure(background="#dbe6ff")
        self.pst.configure(font="-family {@Yu Gothic UI Semibold} -size 20 -weight bold")
        self.pst.configure(foreground="#000000")
        self.pst.configure(highlightbackground="#d9d9d9")
        self.pst.configure(highlightcolor="#000000")
        self.pst.configure(padx="1")
        self.pst.configure(pady="1")
        self.pst.configure(text='''Present -''')
        self.pst.configure(width=116)

        self.total_opt = tk.Text(self.top)
        self.total_opt.place(relx=0.211, rely=0.426, relheight=0.052
                , relwidth=0.066)
        self.total_opt.configure(background="#f2f6fe")
        self.total_opt.configure(font="TkTextFont 18 ")
        self.total_opt.configure(foreground="black")
        self.total_opt.configure(highlightbackground="#d9d9d9")
        self.total_opt.configure(highlightcolor="#000000")
        self.total_opt.configure(insertbackground="#000000")
        self.total_opt.configure(selectbackground="#d9d9d9")
        self.total_opt.configure(selectforeground="black")
        self.total_opt.configure(wrap="word")
        self.total_opt.bind("<Button-1>", lambda e: "break")
        self.total_opt.bind("<Key>", lambda e: "break")

        self.pst_opt = tk.Text(self.top)
        self.pst_opt.place(relx=0.211, rely=0.502, relheight=0.052
                , relwidth=0.066)
        self.pst_opt.configure(background="#f2f6fe")
        self.pst_opt.configure(font="TkTextFont 18")
        self.pst_opt.configure(foreground="black")
        self.pst_opt.configure(highlightbackground="#d9d9d9")
        self.pst_opt.configure(highlightcolor="#000000")
        self.pst_opt.configure(insertbackground="#000000")
        self.pst_opt.configure(selectbackground="#d9d9d9")
        self.pst_opt.configure(selectforeground="black")
        self.pst_opt.configure(wrap="word")
        self.pst_opt.bind("<Button-1>", lambda e: "break")
        self.pst_opt.bind("<Key>", lambda e: "break")

        self.abst = tk.Message(self.top)
        self.abst.place(relx=0.102, rely=0.578, relheight=0.058, relwidth=0.098)
        self.abst.configure(background="#dbe6ff")
        self.abst.configure(font="-family {@Yu Gothic UI Semibold} -size 20 -weight bold")
        self.abst.configure(foreground="#000000")
        self.abst.configure(highlightbackground="#d9d9d9")
        self.abst.configure(highlightcolor="#000000")
        self.abst.configure(padx="1")
        self.abst.configure(pady="1")
        self.abst.configure(text='''Absent -''')
        self.abst.configure(width=126)

        self.per = tk.Message(self.top)
        self.per.place(relx=0.086, rely=0.7, relheight=0.088, relwidth=0.184)
        self.per.configure(background="#dbe6ff")
        self.per.configure(font="-family {@Yu Gothic UI Semibold} -size 36 -weight bold")
        self.per.configure(foreground="#000000")
        self.per.configure(highlightbackground="#d9d9d9")
        self.per.configure(highlightcolor="#000000")
        self.per.configure(padx="1")
        self.per.configure(pady="1")
        self.per.configure(text='''Percent -''')
        self.per.configure(width=235)

        self.Button1 = tk.Button(self.top,command=lambda:self.student(controller))
        self.Button1.place(relx=0.82, rely=0.860, height=60, width=160)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#f2f6fe")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI Semibold} -size 11 -weight bold")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''BACK''')
        photo_location = os.path.join(_location,"../Image/Back_button.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img4)
        self.Button1.configure(relief="flat")


        self.Button = tk.Button(self.top, command= lambda:self.percent_show())
        self.Button.place(relx=0.400, rely=0.860, height=60, width=160)
        self.Button.configure(activebackground="#d9d9d9")
        self.Button.configure(activeforeground="black")
        self.Button.configure(background="#f2f6fe")
        self.Button.configure(disabledforeground="#a3a3a3")
        self.Button.configure(font="-family {Segoe UI Semibold} -size 11 -weight bold")
        self.Button.configure(foreground="#000000")
        self.Button.configure(highlightbackground="#d9d9d9")
        self.Button.configure(highlightcolor="#000000")
        self.Button.configure(text='''BACK''')
        photo_location = os.path.join(_location,"../Image/Show_button.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Button.configure(image=_img3)
        self.Button.configure(relief="flat")



        self.abst_opt = tk.Text(self.top)
        self.abst_opt.place(relx=0.211, rely=0.578, relheight=0.052
                , relwidth=0.066)
        self.abst_opt.configure(background="#f2f6fe")
        self.abst_opt.configure(font="TkTextFont 18")
        self.abst_opt.configure(foreground="black")
        self.abst_opt.configure(highlightbackground="#d9d9d9")
        self.abst_opt.configure(highlightcolor="#000000")
        self.abst_opt.configure(insertbackground="#000000")
        self.abst_opt.configure(selectbackground="#d9d9d9")
        self.abst_opt.configure(selectforeground="black")
        self.abst_opt.configure(wrap="word")
        self.abst_opt.bind("<Button-1>", lambda e: "break")
        self.abst_opt.bind("<Key>", lambda e: "break")

        self.per_opt = tk.Text(self.top)
        self.per_opt.place(relx=0.281, rely=0.715, relheight=0.067
                , relwidth=0.12)
        self.per_opt.configure(background="#f2f6fe")
        self.per_opt.configure(font="TkTextFont 25")
        self.per_opt.configure(foreground="black")
        self.per_opt.configure(highlightbackground="#d9d9d9")
        self.per_opt.configure(highlightcolor="#000000")
        self.per_opt.configure(insertbackground="#000000")
        self.per_opt.configure(selectbackground="#d9d9d9")
        self.per_opt.configure(selectforeground="black")
        self.per_opt.configure(wrap="word")
        self.per_opt.bind("<Button-1>", lambda e: "break")
        self.per_opt.bind("<Key>", lambda e: "break")

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.555, rely=0.183, height=341, width=338)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="black")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        photo_location = os.path.join(_location,"../Image/Untitled1.png")
        global _img0
        _img0 = ImageTk.PhotoImage(file=photo_location)
        self.Label1.configure(image=_img0)

    def student(self,controller):
        from stu_wlcm import student
        controller.show_frame(student)
        self.total_opt.delete("1.0", "end")
        self.pst_opt.delete("1.0", "end")
        self.abst_opt.delete("1.0", "end")
        self.per_opt.delete("1.0", "end")


    def percent_show(self):
        per = stu_percent()
        self.total_opt.insert(END,per[0])
        self.pst_opt.insert(END,per[1])
        self.abst_opt.insert(END,per[2])
        self.per_opt.insert(END,per[3])