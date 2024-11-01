#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Oct 05, 2024 10:54:48 PM IST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from page2 import Toplevel1
_location = os.path.dirname(__file__)

def greet():
    print("Hello, welcome to the app!")

"""
def submit():
    id_var = id.get()
    passw1 = passw.get()

    print(id_var,passw1)

    id.set("")
    passw.set("")"""
import test_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

def submit():

    name=name_var.get()
    password=passw_var.get()
    
    print("The name is : " + name)
    print("The password is : " + password)
    
    name_var.set("")
    passw_var.set("")

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        global name_var,passw_var
        name_var=tk.StringVar()
        passw_var=tk.StringVar()

        top.geometry("600x450+337+177")
        top.minsize(120, 1)
        top.maxsize(1330, 727)
        top.resizable(1,  1)
        top.title("Toplevel 0")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top

        self.Label1 = tk.Label(self.top)
        self.Label1.place(relx=0.067, rely=0.067, height=50, width=510)
        self.Label1.configure(activebackground="#d9d9d9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(anchor='w')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(compound='left')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(relief="raised")
        self.Label1.configure(text='''Login''')

        self.Entry1 = tk.Entry(self.top,textvariable = name_var)
        self.Entry1.place(relx=0.15, rely=0.311, height=20, relwidth=0.14)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="#000000")
        self.Entry1.configure(insertbackground="#000000")
        self.Entry1.configure(selectbackground="#d9d9d9")
        self.Entry1.configure(selectforeground="black")

        self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.05, rely=0.311, relheight=0.042
                , relwidth=0.083)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="#000000")
        self.Message1.configure(padx="1")
        self.Message1.configure(pady="1")
        self.Message1.configure(text='''User Id''')
        self.Message1.configure(width=60)

        self.Message2 = tk.Message(self.top)
        self.Message2.place(relx=0.05, rely=0.4, relheight=0.042, relwidth=0.083)

        self.Message2.configure(background="#d9d9d9")
        self.Message2.configure(foreground="#000000")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="#000000")
        self.Message2.configure(padx="1")
        self.Message2.configure(pady="1")
        self.Message2.configure(text='''Password''')
        self.Message2.configure(width=60)

        self.Entry2 = tk.Entry(self.top,textvariable=passw_var)
        self.Entry2.place(relx=0.15, rely=0.4, height=20, relwidth=0.14)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(highlightbackground="#d9d9d9")
        self.Entry2.configure(highlightcolor="#000000")
        self.Entry2.configure(insertbackground="#000000")
        self.Entry2.configure(selectbackground="#d9d9d9")
        self.Entry2.configure(selectforeground="black")

        self.Button1 = tk.Button(self.top,command=submit)
        self.Button1.place(relx=0.167, rely=0.511, height=26, width=47)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''Submit 2.0''')

def start_up():
    test_support.main()

if __name__ == '__main__':
    test_support.main()
"""
id=tk.StringVar()
passw= tk.stringVar()

"""