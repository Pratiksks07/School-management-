#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Oct 06, 2024 12:18:14 PM IST  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
#ghjkl 
_location = os.path.dirname(__file__)

import Admin_support

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

_style_code_ran = 0
def _style_code():
    global _style_code_ran
    if _style_code_ran: return        
    try: Admin_support.root.tk.call('source',
                os.path.join(_location, 'themes', 'default.tcl'))
    except: pass
    style = ttk.Style()
    style.theme_use('default')
    style.configure('.', font = "TkDefaultFont")
    if sys.platform == "win32":
       style.theme_use('winnative')    
    _style_code_ran = 1

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        top.geometry("600x450+329+148")
        top.minsize(120, 1)
        top.maxsize(1330, 727)
        top.resizable(1,  1)
        top.title("Login")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#000000")

        self.top = top

        _style_code()
        self.TFrame1 = ttk.Frame(self.top)
        self.TFrame1.place(relx=0.0, rely=0.0, relheight=1.011, relwidth=0.613)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=-0.785, rely=-0.336, height=817, width=946)
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='center')
        self.TLabel1.configure(justify='center')
        photo_location = os.path.join(_location,"C:/Users/LENOVO/Desktop/New folder/School-management-/Test/Web-Development-at-Auxous-Network.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.TLabel1.configure(image=_img0)
        self.TLabel1.configure(compound='left')

        self.Canvas1 = tk.Canvas(self.top)
        self.Canvas1.place(relx=0.603, rely=0.0, relheight=1.0, relwidth=0.397)
        self.Canvas1.configure(background="#94adef")
        self.Canvas1.configure(borderwidth="2")
        self.Canvas1.configure(highlightbackground="#d9d9d9")
        self.Canvas1.configure(highlightcolor="#000000")
        self.Canvas1.configure(insertbackground="#000000")
        self.Canvas1.configure(relief="ridge")
        self.Canvas1.configure(selectbackground="#d9d9d9")
        self.Canvas1.configure(selectforeground="black")

        self.Message1 = tk.Message(self.Canvas1)
        self.Message1.place(relx=0.34, rely=0.22, relheight=0.056
                , relwidth=0.336)
        self.Message1.configure(background="#94adef")
        self.Message1.configure(font="-family {Segoe UI Variable Display Semib} -size 11 -weight bold")
        self.Message1.configure(foreground="black")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="#000000")
        self.Message1.configure(justify='center')
        self.Message1.configure(padx="1")
        self.Message1.configure(pady="1")
        self.Message1.configure(text='''LOGIN''')
        self.Message1.configure(width=60)

        self.Entry1_1 = tk.Entry(self.Canvas1)
        self.Entry1_1.place(relx=0.101, rely=0.571, height=20, relwidth=0.605)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="-family {Courier New} -size 10")
        self.Entry1_1.configure(foreground="black")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="#000000")
        self.Entry1_1.configure(insertbackground="#000000")
        self.Entry1_1.configure(relief="solid")
        self.Entry1_1.configure(selectbackground="#d9d9d9")
        self.Entry1_1.configure(selectforeground="black")

        self.Entry1 = tk.Entry(self.Canvas1)
        self.Entry1.place(relx=0.101, rely=0.44, height=20, relwidth=0.605)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="black")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="#000000")
        self.Entry1.configure(insertbackground="#000000")
        self.Entry1.configure(relief="solid")
        self.Entry1.configure(selectbackground="#d9d9d9")
        self.Entry1.configure(selectforeground="black")

        self.Message2 = tk.Message(self.Canvas1)
        self.Message2.place(relx=0.101, rely=0.373, relheight=0.042
                , relwidth=0.168)
        self.Message2.configure(background="#94adef")
        self.Message2.configure(foreground="black")
        self.Message2.configure(highlightbackground="#d9d9d9")
        self.Message2.configure(highlightcolor="#000000")
        self.Message2.configure(justify='center')
        self.Message2.configure(padx="1")
        self.Message2.configure(pady="1")
        self.Message2.configure(text='''USER ID''')
        self.Message2.configure(width=60)

        self.Button1 = tk.Button(self.Canvas1)
        self.Button1.place(relx=0.307, rely=0.702, height=26, width=67)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#b9c9f4")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="black")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''SUBMIT''')

        self.Message3 = tk.Message(self.Canvas1)
        self.Message3.place(relx=0.084, rely=0.511, relheight=0.042
                , relwidth=0.277)
        self.Message3.configure(background="#94adef")
        self.Message3.configure(foreground="black")
        self.Message3.configure(highlightbackground="#d9d9d9")
        self.Message3.configure(highlightcolor="#000000")
        self.Message3.configure(padx="1")
        self.Message3.configure(pady="1")
        self.Message3.configure(text='''PASSWORD''')
        self.Message3.configure(width=66)

def start_up():
    Admin_support.main()

if __name__ == '__main__':
    Admin_support.main()




