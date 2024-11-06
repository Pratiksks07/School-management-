import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from sql import enrollment

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

_location = os.path.dirname(__file__)

class stu_en(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,height=1020,width=1960)
        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        self.self = self

        global name_var,class_var,roll_var,adm_var,fname_var,mname_var,address_var,phone_var,sec_var
        name_var = tk.StringVar()
        class_var = tk.StringVar()
        roll_var = tk.StringVar()
        sec_var = tk.StringVar()
        adm_var = tk.StringVar()
        fname_var = tk.StringVar()
        mname_var = tk.StringVar()
        address_var = tk.StringVar()
        phone_var = tk.StringVar()
        

        self.upper = tk.Label(self.self)
        self.upper.place(relx=0.001, rely=0.0, relheight=0.240
                , relwidth=0.999)
        self.upper.configure(background="#8AA3F7")
        self.upper.configure(foreground="#000000")
        self.upper.configure(highlightbackground="#d9d9d9")
        self.upper.configure(highlightcolor="#000000")
        self.upper.configure(relief="raised")


        self.heading = tk.Label(self.self)
        self.heading.place(relx=0.065, rely=0.0, relheight=0.200
                , relwidth=0.600)
        self.heading.configure(activebackground="#8AA3F7")
        self.heading.configure(activeforeground="black")
        self.heading.configure(anchor='w')
        self.heading.configure(background="#8AA3F7")
        self.heading.configure(compound='left')
        self.heading.configure(disabledforeground="#a3a3a3")
        self.heading.configure(font="-family {Sitka Display} -size 55 -weight bold")
        self.heading.configure(foreground="#000000")
        self.heading.configure(highlightbackground="#d9d9d9")
        self.heading.configure(highlightcolor="#000000")
        self.heading.configure(text='''Student Enrollment''')

        self.enroll_icon = tk.Label(self.self)
        self.enroll_icon.place(relx=0.800, rely=0.0, height=150, width=150)  # Adjusted position for visibility
        self.enroll_icon.configure(
            background="#d9d9d9",
            foreground="#000000",
            anchor='center')
        photo_location = os.path.join(os.path.dirname(__file__), "../Image/Enrollment_icon.png")
        self.enroll_img = tk.PhotoImage(file=photo_location)
        self.enroll_icon.configure(image=self.enroll_img)
        self.enroll_icon.configure(relief="flat")


        self.adm = tk.Label(self.self)
        self.adm.place(relx=0.063, rely=0.524, height=31, width=130)
        self.adm.configure(activebackground="#d9d9d9")
        self.adm.configure(activeforeground="black")
        self.adm.configure(anchor='w')
        self.adm.configure(background="#dbe6ff")
        self.adm.configure(compound='left')
        self.adm.configure(disabledforeground="#a3a3a3")
        self.adm.configure(font="-family {Segoe UI Variable Display} -size 16 -weight bold")
        self.adm.configure(foreground="#000000")
        self.adm.configure(highlightbackground="#d9d9d9")
        self.adm.configure(highlightcolor="#000000")
        self.adm.configure(text='''Adm. no:''')


        self.mom = tk.Label(self.self)
        self.mom.place(relx=0.063, rely=0.647, height=31, width=160)
        self.mom.configure(activebackground="#d9d9d9")
        self.mom.configure(activeforeground="black")
        self.mom.configure(anchor='w')
        self.mom.configure(background="#dbe6ff")
        self.mom.configure(compound='left')
        self.mom.configure(disabledforeground="#a3a3a3")
        self.mom.configure(font="-family {Segoe UI Variable Display} -size 16 -weight bold")
        self.mom.configure(foreground="#000000")
        self.mom.configure(highlightbackground="#d9d9d9")
        self.mom.configure(highlightcolor="#000000")
        self.mom.configure(text='''Mother's Name:''')


        self.address = tk.Label(self.self)
        self.address.place(relx=0.063, rely=0.709, height=31, width=124)
        self.address.configure(activebackground="#d9d9d9")
        self.address.configure(activeforeground="black")
        self.address.configure(anchor='w')
        self.address.configure(background="#dbe6ff")
        self.address.configure(compound='left')
        self.address.configure(disabledforeground="#a3a3a3")
        self.address.configure(font="-family {Segoe UI Variable Display} -size 16 -weight bold")
        self.address.configure(foreground="#000000")
        self.address.configure(highlightbackground="#d9d9d9")
        self.address.configure(highlightcolor="#000000")
        self.address.configure(text='''Address:''')


        self.phone = tk.Label(self.self)
        self.phone.place(relx=0.063, rely=0.771, height=31, width=124)
        self.phone.configure(activebackground="#d9d9d9")
        self.phone.configure(activeforeground="black")
        self.phone.configure(anchor='w')
        self.phone.configure(background="#dbe6ff")
        self.phone.configure(compound='left')
        self.phone.configure(disabledforeground="#a3a3a3")
        self.phone.configure(font="-family {Segoe UI Variable Display} -size 16 -weight bold")
        self.phone.configure(foreground="#000000")
        self.phone.configure(highlightbackground="#d9d9d9")
        self.phone.configure(highlightcolor="#000000")
        self.phone.configure(text='''Phone:''')


        self.cls = tk.Label(self.self)
        self.cls.place(relx=0.063, rely=0.339, height=31, width=70)
        self.cls.configure(activebackground="#d9d9d9")
        self.cls.configure(activeforeground="black")
        self.cls.configure(anchor='w')
        self.cls.configure(background="#dbe6ff")
        self.cls.configure(compound='left')
        self.cls.configure(disabledforeground="#a3a3a3")
        self.cls.configure(font="-family {Segoe UI Variable Display} -size 16 -weight bold")
        self.cls.configure(foreground="#000000")
        self.cls.configure(highlightbackground="#d9d9d9")
        self.cls.configure(highlightcolor="#000000")
        self.cls.configure(text='''Class:''')


        self.roll = tk.Label(self.self)
        self.roll.place(relx=0.063, rely=0.462, height=31, width=102)
        self.roll.configure(activebackground="#d9d9d9")
        self.roll.configure(activeforeground="black")
        self.roll.configure(anchor='w')
        self.roll.configure(background="#dbe6ff")
        self.roll.configure(compound='left')
        self.roll.configure(disabledforeground="#a3a3a3")
        self.roll.configure(font="-family {Segoe UI Variable Display} -size 16 -weight bold")
        self.roll.configure(foreground="#000000")
        self.roll.configure(highlightbackground="#d9d9d9")
        self.roll.configure(highlightcolor="#000000")
        self.roll.configure(text='''Roll no:''')


        self.dad = tk.Label(self.self)
        self.dad.place(relx=0.063, rely=0.586, height=31, width=153)
        self.dad.configure(activebackground="#d9d9d9")
        self.dad.configure(activeforeground="black")
        self.dad.configure(anchor='w')
        self.dad.configure(background="#dbe6ff")
        self.dad.configure(compound='left')
        self.dad.configure(disabledforeground="#a3a3a3")
        self.dad.configure(font="-family {Segoe UI Variable Display} -size 16 -weight bold")
        self.dad.configure(foreground="#000000")
        self.dad.configure(highlightbackground="#d9d9d9")
        self.dad.configure(highlightcolor="#000000")
        self.dad.configure(text='''Father's Name:''')


        self.name = tk.Label(self.self)
        self.name.place(relx=0.063, rely=0.277, height=31, width=84)
        self.name.configure(activebackground="#d9d9d9")
        self.name.configure(activeforeground="black")
        self.name.configure(anchor='w')
        self.name.configure(background="#dbe6ff")
        self.name.configure(compound='left')
        self.name.configure(disabledforeground="#a3a3a3")
        self.name.configure(font="-family {Segoe UI Variable Display} -size 16 -weight bold")
        self.name.configure(foreground="#000000")
        self.name.configure(highlightbackground="#d9d9d9")
        self.name.configure(highlightcolor="#000000")
        self.name.configure(text='''Name:''')


        #SECTION
        self.sec = tk.Label(self.self)
        self.sec.place(relx=0.063, rely=0.401, height=31, width=84)
        self.sec.configure(activebackground="#d9d9d9")
        self.sec.configure(activeforeground="black")
        self.sec.configure(anchor='w')
        self.sec.configure(background="#dbe6ff")
        self.sec.configure(compound='left')
        self.sec.configure(disabledforeground="#a3a3a3")
        self.sec.configure(font="-family {Segoe UI Variable Display} -size 16 -weight bold")
        self.sec.configure(foreground="#000000")
        self.sec.configure(highlightbackground="#d9d9d9")
        self.sec.configure(highlightcolor="#000000")
        self.sec.configure(text='''Section:''')

        #Submit 
        self.submit = tk.Button(self.self, command= lambda: enrollment(name_var,roll_var,class_var,sec_var,adm_var,fname_var,mname_var,phone_var,address_var,self,controller))
        self.submit.place(relx=0.400, rely=0.840, height=60, width=160)
        self.submit.configure(activebackground="#d9d9d9")
        self.submit.configure(activeforeground="black")
        self.submit.configure(background="#f2f6fe")
        self.submit.configure(disabledforeground="#a3a3a3")
        self.submit.configure(font="-family {Segoe UI Black} -size 13 -weight bold")
        self.submit.configure(foreground="#000000")
        self.submit.configure(highlightbackground="#d9d9d9")
        self.submit.configure(highlightcolor="#000000")
        self.submit.configure(text='''SUBMIT''')
        photo_location = os.path.join(_location,"../Image/Submit_button.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.submit.configure(image=_img4)
        self.submit.configure(relief="flat")


        self.back = tk.Button(self.self, command=lambda: self.page(controller))
        self.back.place(relx=0.833, rely=0.840, height=60, width=160)
        self.back.configure(activebackground="#d9d9d9")
        self.back.configure(activeforeground="black")
        self.back.configure(background="#f2f6fe")
        self.back.configure(disabledforeground="#a3a3a3")
        self.back.configure(font="-family {Segoe UI Black} -size 13 -weight bold")
        self.back.configure(foreground="#000000")
        self.back.configure(highlightbackground="#d9d9d9")
        self.back.configure(highlightcolor="#000000")
        self.back.configure(text='''BACK''')
        photo_location = os.path.join(_location,"../Image/Back_button.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.back.configure(image=_img3)
        self.back.configure(relief="flat")


        self.Enter_adm = tk.Entry(self.self, textvariable=adm_var)
        self.Enter_adm.place(relx=0.215, rely=0.524, height=25, relwidth=0.3)
        self.Enter_adm.configure(background="white")
        self.Enter_adm.configure(disabledforeground="#a3a3a3")
        self.Enter_adm.configure(font="TkFixedFont")
        self.Enter_adm.configure(foreground="#000000")
        self.Enter_adm.configure(highlightbackground="#d9d9d9")
        self.Enter_adm.configure(highlightcolor="#000000")
        self.Enter_adm.configure(insertbackground="#000000")
        self.Enter_adm.configure(selectbackground="#d9d9d9")
        self.Enter_adm.configure(selectforeground="black")


        self.Enter_roll = tk.Entry(self.self, textvariable= roll_var)
        self.Enter_roll.place(relx=0.215, rely=0.462, height=25, relwidth=0.3)
        self.Enter_roll.configure(background="white")
        self.Enter_roll.configure(disabledforeground="#a3a3a3")
        self.Enter_roll.configure(font="TkFixedFont")
        self.Enter_roll.configure(foreground="#000000")
        self.Enter_roll.configure(highlightbackground="#d9d9d9")
        self.Enter_roll.configure(highlightcolor="#000000")
        self.Enter_roll.configure(insertbackground="#000000")
        self.Enter_roll.configure(selectbackground="#d9d9d9")
        self.Enter_roll.configure(selectforeground="black")


        self.Enter_sec = tk.Entry(self.self, textvariable = sec_var)
        self.Enter_sec.place(relx=0.215, rely=0.401, height=25, relwidth=0.3)
        self.Enter_sec.configure(background="white")
        self.Enter_sec.configure(disabledforeground="#a3a3a3")
        self.Enter_sec.configure(font="TkFixedFont")
        self.Enter_sec.configure(foreground="#000000")
        self.Enter_sec.configure(highlightbackground="#d9d9d9")
        self.Enter_sec.configure(highlightcolor="#000000")
        self.Enter_sec.configure(insertbackground="#000000")
        self.Enter_sec.configure(selectbackground="#d9d9d9")
        self.Enter_sec.configure(selectforeground="black")


        self.Enter_class = tk.Entry(self.self, textvariable= class_var)
        self.Enter_class.place(relx=0.215, rely=0.345, height=25, relwidth=0.3)
        self.Enter_class.configure(background="white")
        self.Enter_class.configure(disabledforeground="#a3a3a3")
        self.Enter_class.configure(font="TkFixedFont")
        self.Enter_class.configure(foreground="#000000")
        self.Enter_class.configure(highlightbackground="#d9d9d9")
        self.Enter_class.configure(highlightcolor="#000000")
        self.Enter_class.configure(insertbackground="#000000")
        self.Enter_class.configure(selectbackground="#d9d9d9")
        self.Enter_class.configure(selectforeground="black")


        self.Enter_name = tk.Entry(self.self, textvariable=name_var)
        self.Enter_name.place(relx=0.215, rely=0.290, height=25, relwidth=0.3)
        self.Enter_name.configure(background="white")
        self.Enter_name.configure(disabledforeground="#a3a3a3")
        self.Enter_name.configure(font="TkFixedFont")
        self.Enter_name.configure(foreground="#000000")
        self.Enter_name.configure(highlightbackground="#d9d9d9")
        self.Enter_name.configure(highlightcolor="#000000")
        self.Enter_name.configure(insertbackground="#000000")
        self.Enter_name.configure(selectbackground="#d9d9d9")
        self.Enter_name.configure(selectforeground="black")


        self.Enter_dad = tk.Entry(self.self,textvariable=fname_var)
        self.Enter_dad.place(relx=0.215, rely=0.586, height=25, relwidth=0.3)
        self.Enter_dad.configure(background="white")
        self.Enter_dad.configure(disabledforeground="#a3a3a3")
        self.Enter_dad.configure(font="TkFixedFont")
        self.Enter_dad.configure(foreground="#000000")
        self.Enter_dad.configure(highlightbackground="#d9d9d9")
        self.Enter_dad.configure(highlightcolor="#000000")
        self.Enter_dad.configure(insertbackground="#000000")
        self.Enter_dad.configure(selectbackground="#d9d9d9")
        self.Enter_dad.configure(selectforeground="black")


        self.Enter_mom = tk.Entry(self.self,textvariable=mname_var)
        self.Enter_mom.place(relx=0.215, rely=0.647, height=25, relwidth=0.3)
        self.Enter_mom.configure(background="white")
        self.Enter_mom.configure(disabledforeground="#a3a3a3")
        self.Enter_mom.configure(font="TkFixedFont")
        self.Enter_mom.configure(foreground="#000000")
        self.Enter_mom.configure(highlightbackground="#d9d9d9")
        self.Enter_mom.configure(highlightcolor="#000000")
        self.Enter_mom.configure(insertbackground="#000000")
        self.Enter_mom.configure(selectbackground="#d9d9d9")
        self.Enter_mom.configure(selectforeground="black")


        self.Enter_add = tk.Entry(self.self,textvariable=address_var)
        self.Enter_add.place(relx=0.215, rely=0.709, height=25, relwidth=0.3)
        self.Enter_add.configure(background="white")
        self.Enter_add.configure(disabledforeground="#a3a3a3")
        self.Enter_add.configure(font="TkFixedFont")
        self.Enter_add.configure(foreground="#000000")
        self.Enter_add.configure(highlightbackground="#d9d9d9")
        self.Enter_add.configure(highlightcolor="#000000")
        self.Enter_add.configure(insertbackground="#000000")
        self.Enter_add.configure(selectbackground="#d9d9d9")
        self.Enter_add.configure(selectforeground="black")


        self.enter_phone = tk.Entry(self.self,textvariable=phone_var)
        self.enter_phone.place(relx=0.215, rely=0.771, height=25, relwidth=0.3)
        self.enter_phone.configure(background="white")
        self.enter_phone.configure(disabledforeground="#a3a3a3")
        self.enter_phone.configure(font="TkFixedFont")
        self.enter_phone.configure(foreground="#000000")
        self.enter_phone.configure(highlightbackground="#d9d9d9")
        self.enter_phone.configure(highlightcolor="#000000")
        self.enter_phone.configure(insertbackground="#000000")
        self.enter_phone.configure(selectbackground="#d9d9d9")
        self.enter_phone.configure(selectforeground="black")


        

        
    def page(self,controller):
        from adm_wlcm import admin
        controller.show_frame(admin)