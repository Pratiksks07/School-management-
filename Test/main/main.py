#Importing Modules
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

#Importing page classes from different files
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
from adm_qbank import qbank_adm
from stu_qbank import qbank_stu

#Declaring Constants
_location = os.path.dirname(__file__)
LARGEFONT = ("Verdana", 35)


#This class represents the entire application and manages switching between frames (pages)
class tkinterApp(tk.Tk):

    # __init__ function for class tkinterApp
    def __init__(self, *args, **kwargs):
        #__init__ method is used to initialize objects of a class. It is also called a constructor
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)


        #Creates a Frame widget that will act as a container for all the different pages.
        self.state('zoomed') # Maximize the frames
        container = tk.Frame(self,height=1020,width=1960)
        container.pack(side="top", fill="both", expand=True)
    

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Dictionary to store each page (frame) in the application.
        self.frames = {}


        # Iterating(looping) through a tuple consisting
        # of the different page layouts (frames)
        for F in (loginpage, admin, stu_en, atd_admin, student, msg_adm, msg_stu, timetable, atd_stu,profile_stu,qbank_adm,qbank_stu):
            frame = F(container, self)  # 'self' is passed as 'controller' here

            # Store the frame in self.frames
            self.frames[F] = frame

            # Initialize the frame and set it invisible (stacked)
            #Stacking it over one another
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(loginpage)  # Show login page first



    # Show the current frame passed as the parameter
    def show_frame(self, cont):
        
        frame = self.frames[cont]
        frame.tkraise()  # Bring the selected frame to the front


#Runs the application
app = tkinterApp()
app.mainloop()

