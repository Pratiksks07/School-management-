# Importing Modules
import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path


_location = os.path.dirname(__file__) #Stores the path of the current file


#Time table page class
class timetable(tk.Frame):
    
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent,height=1020,width=1960)
        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")


        self.top = self

        #Top border
        self.upper = tk.Label(self.top)
        self.upper.place(relx=0.001, rely=0.0, relheight=0.240
                , relwidth=0.999)
        self.upper.configure(background="#8AA3F7")
        self.upper.configure(relief="raised")


        #Time table message
        self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.065, rely=0.0, relheight=0.200
                , relwidth=0.600)
        self.Message1.configure(background="#8AA3F7")
        self.Message1.configure(font="-family {Sitka Display} -size 55 -weight bold")
        self.Message1.configure(text='''Time Table''')
        self.Message1.configure(width=500)
        self.Message1.configure(anchor='w')


        #Time Table (Kept as an Image)
        self.time_table = tk.Label(self.top)
        self.time_table.place(relx=0.080, rely=0.280, height=450, width=900)  # Adjusted position for visibility
        self.time_table.configure(
            background="#d9d9d9",
            foreground="#000000",
            anchor='center')
        photo_location = os.path.join(os.path.dirname(__file__), "../Image/Time_table.png")
        self.table_img = tk.PhotoImage(file=photo_location)
        self.time_table.configure(image=self.table_img)
        self.time_table.configure(relief="flat")


        # Time table icon (Used on top border)
        self.Time_table_icon = tk.Label(self.top)
        self.Time_table_icon.place(relx=0.800, rely=0.0, height=150, width=150)  # Adjusted position for visibility
        self.Time_table_icon.configure(
            background="#d9d9d9",
            foreground="#000000",
            anchor='center')
        photo_location = os.path.join(os.path.dirname(__file__), "../Image/Time_table_icon.png")
        self.icon_img = tk.PhotoImage(file=photo_location)
        self.Time_table_icon.configure(image=self.icon_img)
        self.Time_table_icon.configure(relief="flat")

        
        #Back Button
        self.Button1 = tk.Button(self.top,command=lambda:self.student(controller))
        self.Button1.place(relx=0.833, rely=0.840, height=60, width=160)
        self.Button1.configure(background="#f2f6fe")
        self.Button1.configure(font="-family {Segoe UI} -size 9")
        photo_location = os.path.join(_location,"../Image/Back_button.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img4)
        self.Button1.configure(relief="flat")
        

    #Function for switching pages
    def student(self,controller):
        from stu_wlcm import student
        controller.show_frame(student)