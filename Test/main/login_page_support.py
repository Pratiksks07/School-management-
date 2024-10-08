#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Oct 07, 2024 09:34:38 AM PDT  platform: Windows NT

import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import loginpage

_debug = True # False to eliminate debug printing from callback functions.

def main(*args):
    '''Main entry point for the application.'''
    global root
    root = tk.Tk()
    root.protocol( 'WM_DELETE_WINDOW' , root.destroy)
    # Creates a toplevel widget.
    global _top1, _w1
    _top1 = root
    _w1 = loginpage.Toplevel1(_top1)
    root.mainloop()

if __name__ == '__main__':
    loginpage.start_up()




