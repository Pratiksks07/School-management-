import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path


from login_page import loginpage
from adm_wlcm import admin
from stu_enroll import stu_en
from adm_atd import atd_admin
from stu_wlcm import student
from adm_msg import msg_adm
from stu_msg import msg_stu
from time_table import timetable
from stu_atd import atd_stu
from stu_profile import profile_stu

_location = os.path.dirname(__file__)


# Large Font
LARGEFONT = ("Verdana", 35)

class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # Creating a container
        container = tk.Frame(self,height=1020,width=1960)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Initializing frames to an empty array
        self.frames = {}

        # Iterating through a tuple consisting
        # of the different page layouts (frames)

        for F in (loginpage, admin, stu_en, atd_admin, student, msg_adm, msg_stu, timetable, atd_stu,profile_stu):
            frame = F(container, self)  # 'self' is passed as 'controller' here

            # Store the frame in self.frames
            self.frames[F] = frame

            # Initialize the frame and set it invisible (stacked)
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(loginpage)  # Show login page first

    # Show the current frame passed as the parameter
    
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()  # Bring the selected frame to the front

# Driver Code
app = tkinterApp()
app.mainloop()

