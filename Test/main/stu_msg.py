import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

class msg_stu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,height=1020,width=1960)

        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        self.top = self
        self.Admin = tk.StringVar()

        self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.053, rely=0.044, relheight=0.104
                , relwidth=0.192)
        self.Message1.configure(background="#dbe6ff")
        self.Message1.configure(font="-family {Arial Black} -size 24 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="#000000")
        self.Message1.configure(padx="1")
        self.Message1.configure(pady="1")
        self.Message1.configure(text='''Message''')
        self.Message1.configure(width=254)

        self.Button1 = tk.Button(self.top)
        self.Button1.place(relx=0.784, rely=0.390, height=60, width=160)
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

        self.Entry1 = tk.Entry(self.top)
        self.Entry1.place(relx=0.09, rely=0.148, height=160, relwidth=0.765)
        self.Entry1.configure(background="#f2f6fe")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(exportselection="0")
        self.Entry1.configure(font="-family {Courier New} -size 10")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="#000000")
        self.Entry1.configure(insertbackground="#000000")
        self.Entry1.configure(relief="solid")
        self.Entry1.configure(selectbackground="#d9d9d9")
        self.Entry1.configure(selectforeground="black")

       # _style_code()
        self.TCombobox1 = ttk.Combobox(self.top)
        self.TCombobox1.place(relx=0.083, rely=0.530, relheight=0.045
                , relwidth=0.109)
        self.TCombobox1.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.TCombobox1.configure(textvariable=self.Admin)
        self.TCombobox1.configure(foreground="#252525")
        self.TCombobox1.configure(background="#f2f6fe")
        self.TCombobox1.configure(cursor="arrow")

        self.Button2 = tk.Button(self.top)
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

        self.Text1 = tk.Text(self.top)
        self.Text1.place(relx=0.083, rely=0.607, relheight=0.304, relwidth=0.756)

        self.Text1.configure(background="#f2f6fe")
        self.Text1.configure(font="-family {Segoe UI} -size 9 -weight bold")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="#000000")
        self.Text1.configure(insertbackground="#000000")
        self.Text1.configure(selectbackground="#d9d9d9")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(setgrid="1")
        self.Text1.configure(spacing1="2")
        self.Text1.configure(spacing2="4")
        self.Text1.configure(spacing3="5")
        self.Text1.configure(tabs="3")

        self.Button3 = tk.Button(self.top,command=lambda:self.student(controller))
        self.Button3.place(relx=0.865, rely=0.898, height=60, width=160)
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
