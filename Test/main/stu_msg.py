import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from sql import *


_location = os.path.dirname(__file__)

class msg_stu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,height=1020,width=1960)

        message = tk.StringVar()
        category = tk.StringVar()

        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        self.top = self
        self.Admin = tk.StringVar()

        self.upper = tk.Label(self.top)
        self.upper.place(relx=0.001, rely=0.0, relheight=0.240
                , relwidth=0.999)
        self.upper.configure(background="#8AA3F7")
        self.upper.configure(foreground="#000000")
        self.upper.configure(highlightbackground="#d9d9d9")
        self.upper.configure(highlightcolor="#000000")
        self.upper.configure(relief="raised")

        self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.065, rely=0.0, relheight=0.200
                , relwidth=0.600)
        self.Message1.configure(background="#8AA3F7")
        self.Message1.configure(font="-family {Sitka Display} -size 55 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="#000000")
        #self.Message1.configure(padx="1")
        #self.Message1.configure(pady="1")
        self.Message1.configure(text='''Message''')
        self.Message1.configure(width=500)
        self.Message1.configure(anchor='w')


        self.Text1 = tk.Text(self.top)
        self.Text1.place(relx=0.09, rely=0.265, height=130, relwidth=0.765)
        self.Text1.configure(background="#f2f6fe")
        #self.Text1.configure(disabledforeground="#a3a3a3")
        self.Text1.configure(font="-family {Courier New} -size 15")
        self.Text1.configure(foreground="#000000")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="#000000")
        self.Text1.configure(insertbackground="#000000")
        self.Text1.configure(relief="solid")
        self.Text1.configure(selectbackground="#d9d9d9")
        self.Text1.configure(selectforeground="black")


        self.Button1 = tk.Button(self.top, command= lambda: self.sent())
        self.Button1.place(relx=0.784, rely=0.458, height=60, width=160)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#f2f6fe")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 9")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''Send''')
        photo_location = os.path.join(_location,"../Image/Send_button.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img2)
        self.Button1.configure(relief="flat")

        
        #_style_code()
        self.TCombobox1 = ttk.Combobox(self.top,values=['Self','Admin'],textvariable=category)
        self.TCombobox1.place(relx=0.083, rely=0.533, relheight=0.037
                , relwidth=0.109)
        self.TCombobox1.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.TCombobox1.configure(textvariable=self.Admin)
        self.TCombobox1.configure(foreground="#252525")
        self.TCombobox1.configure(background="#f2f6fe")
        self.TCombobox1.configure(cursor="arrow")


        self.Button2 = tk.Button(self.top,command=lambda:self.display_table(category))
        self.Button2.place(relx=0.211, rely=0.510, height=60, width=160)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="black")
        self.Button2.configure(background="#f2f6fe")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(font="-family {Segoe UI} -size 9")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="#000000")
        self.Button2.configure(text='''Show''')
        photo_location = os.path.join(_location,"../Image/Show_button.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.Button2.configure(image=_img3)
        self.Button2.configure(relief="flat")


        self.Text2 = tk.Text(self.top)
        self.Text2.place(relx=0.083, rely=0.607, relheight=0.304, relwidth=0.756)
        self.Text2.configure(background="#f2f6fe")
        self.Text2.configure(font="-family {Segoe UI} -size 15 -weight bold")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="#000000")
        self.Text2.configure(insertbackground="#000000")
        self.Text2.configure(selectbackground="#d9d9d9")
        self.Text2.configure(selectforeground="black")
        self.Text2.configure(setgrid="1")
        self.Text2.configure(spacing1="2")
        self.Text2.configure(spacing2="4")
        self.Text2.configure(spacing3="5")
        self.Text2.configure(tabs="3")
        self.Text2.bind("<Key>", lambda e: "break")
        self.Text2.bind("<Button-1>", lambda e: "break")


        self.Button3 = tk.Button(self.top,command=lambda:self.student(controller))
        self.Button3.place(relx=0.860, rely=0.898, height=60, width=160)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="black")
        self.Button3.configure(background="#f2f6fe")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(font="-family {Segoe UI} -size 9")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="#000000")
        self.Button3.configure(text='''Back''')
        photo_location = os.path.join(_location,"../Image/Back_button.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Button3.configure(image=_img4)
        self.Button3.configure(relief="flat")

    def student(self,controller):
        from stu_wlcm import student
        controller.show_frame(student)
        self.Text2.delete("1.0", "end")
        self.Text1.delete("1.0","end")

    def sent(self):
        from sql import stu_msgsent
        message = self.Text1.get("1.0", "end-1c")
        stu_msgsent(message)
        self.Text1.delete("1.0", "end")

    def display_table(self,cat):

        cat = self.TCombobox1.get()
        columns, rows = fetch_data_stu(type=cat)
        table = format_table(columns, rows)
        
        # Clear the Text widget and insert the table data
        self.Text2.delete("1.0", tk.END)
        self.Text2.insert("1.0", table)
