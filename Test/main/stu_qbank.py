import sys
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path
from sql import *

_location = os.path.dirname(__file__)

_bgcolor = '#d9d9d9'
_fgcolor = '#000000'
_tabfg1 = 'black' 
_tabfg2 = 'white' 
_bgmode = 'light' 
_tabbg1 = '#d9d9d9' 
_tabbg2 = 'gray40' 

class qbank_stu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,height=1020,width=1960)
        self.configure(background="#dbe6ff")
        self.configure(highlightbackground="#d9d9d9")
        self.configure(highlightcolor="#000000")

        global data
        data = {
            "Class 9": {"Maths": ["Polynomials", "Number System", "Lines & Angles","Circles","Triangles"],
                "Science": ["Motion","Gravitation","Atoms & molecules","Human cell","Tissue"],
                "English":[],
                "Hindi": [],
                "SST":[],
                "AI":[]},

            "Class 10": {"Maths": ["Sequence & series","Trigonometry", "Hight & distance","Statistics", "Probability"],
                "Science": ["Light", "Electricity", "Human Eye", "Carbon & Its Compounds","Acid, Bases & salt"],
                "English":[],
                "Hindi": [],
                "SST":[],
                "AI":[]
                },

            "Class 11": {"Physics": ["Mechanics", "Waves","Rotation","Gravitation", "Thermodynamics"],
                "Chemistry": ["Mole Concept", "Chemical Equilibrium", "Hydrocarbons"],
                "Maths":["Trigonometry","Calculus","stright Lines","Conic Sections"],
                "Biology":[],
                "English":[],
                "IP":[],
                "Accountancy":[],
                "BST": [],
                "History": [],
                "Pol. Sci." : []
                },

            "Class 12": {"Physics": ["Electrostatics", "Optics", "Semi conductors","Alternating Current","Magnetism"],
                "Chemistry": ["Chemical Kinetics", "Solutions", "Akyl Halids","Aldehyde & Ketones", "Bio molecules"],
                "Maths":["Relation & Functions","ITF","Matices & determinant","Calculus","Vectors"],
                "Biology":[],
                "English":[],
                "IP":[],
                "Accountancy":[],
                "BST": [],
                "History": [],
                "Pol. Sci." : []
                },
            }

        
        self.top = self
        global cls,subj,chapter
        cls = tk.StringVar()
        subj = tk.StringVar()
        chapter = tk.StringVar()
        #question = tk.StringVar()


        self.upper = tk.Label(self.top)
        self.upper.place(relx=0.001, rely=0.0, relheight=0.240
                , relwidth=0.999)
        self.upper.configure(background="#8AA3F7")
        self.upper.configure(foreground="#000000")
        self.upper.configure(highlightbackground="#d9d9d9")
        self.upper.configure(highlightcolor="#000000")
        self.upper.configure(relief="raised")
        

        self.qbank_icon = tk.Label(self.top)
        self.qbank_icon.place(relx=0.800, rely=0.0, height=150, width=150)  # Adjusted position for visibility
        self.qbank_icon.configure(
            background="#d9d9d9",
            foreground="#000000",
            anchor='center')
        photo_location = os.path.join(os.path.dirname(__file__), "../Image/Questionbank_icon.png")
        self.message_img = tk.PhotoImage(file=photo_location)
        self.qbank_icon.configure(image=self.message_img)
        self.qbank_icon.configure(relief="flat")


        self.Message1 = tk.Message(self.top)
        self.Message1.place(relx=0.065, rely=0.0, relheight=0.200
                , relwidth=0.600)
        self.Message1.configure(background="#8AA3F7")
        self.Message1.configure(font="-family {Sitka Display} -size 55 -weight bold")
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="#000000")
        self.Message1.configure(text='''Question Bank''')
        self.Message1.configure(width=500)
        self.Message1.configure(anchor='w')


        self.cls = ttk.Combobox(self.top, values=list(data.keys()), textvariable=cls)
        self.cls.place(relx=0.080, rely=0.300, relheight=0.050
                , relwidth=0.135)
        self.cls.configure(font="-family {Segoe UI Black} -size 14 -weight bold")
        self.cls.configure(foreground="#252525")
        self.cls.configure(background="#f2f6fe")
        self.cls.configure(cursor="arrow")
        self.cls.bind("<<ComboboxSelected>>", self.update_subjects)  # Bind event for updating subjects

        self.sub = ttk.Combobox(self.top,textvariable=subj)
        self.sub.place(relx=0.400, rely=0.300, relheight=0.050
                , relwidth=0.135)
        self.sub.configure(font="-family {Segoe UI Black} -size 14 -weight bold")
        self.sub.configure(foreground="#252525")
        self.sub.configure(background="#f2f6fe")
        self.sub.configure(cursor="arrow")
        self.sub.bind("<<ComboboxSelected>>", self.update_chapters)  # Bind event for updating chapters


        self.chapter = ttk.Combobox(self.top, textvariable=chapter)
        self.chapter.place(relx=0.720, rely=0.300, relheight=0.050
                , relwidth=0.135)
        self.chapter.configure(font="-family {Segoe UI Black} -size 14 -weight bold")
        self.chapter.configure(foreground="#252525")
        self.chapter.configure(background="#f2f6fe")
        self.chapter.configure(cursor="arrow")


        self.Text2 = tk.Text(self.top)
        self.Text2.place(relx=0.080, rely=0.430, relheight=0.370, relwidth=0.800)
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

        
        self.Button1 = tk.Button(self.top,command=lambda:self.page(controller))
        self.Button1.place(relx=0.820, rely=0.850, height=60, width=160)
        self.Button1.configure(activebackground="#f2f6fe")
        self.Button1.configure(activeforeground="black")
        self.Button1.configure(background="#f2f6fe")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(font="-family {Segoe UI} -size 9")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="#000000")
        self.Button1.configure(text='''Back''')
        photo_location = os.path.join(_location,"../Image/Back_button.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.Button1.configure(image=_img4)
        self.Button1.configure(relief="flat")

        self.show = tk.Button(self.top,command=lambda:self.show_ques())
        self.show.place(relx=0.100, rely=0.850, height=60, width=160)
        self.show.configure(activebackground="#f2f6fe")
        self.show.configure(activeforeground="black")
        self.show.configure(background="#f2f6fe")
        self.show.configure(disabledforeground="#a3a3a3")
        self.show.configure(font="-family {Segoe UI} -size 9")
        self.show.configure(foreground="#000000")
        self.show.configure(highlightbackground="#d9d9d9")
        self.show.configure(highlightcolor="#000000")
        self.show.configure(text='''Back''')
        photo_location = os.path.join(_location,"../Image/Show_button.png")
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.show.configure(image=_img5)
        self.show.configure(relief="flat")

    def page(self,controller):
        from stu_wlcm import student
        controller.show_frame(student)
        self.Text2.delete("1.0", "end")

    # Update subjects based on class selection
    def update_subjects(self, event=None):
        selected_class = self.cls.get()
        if selected_class in data:
            subjects = list(data[selected_class].keys())
            self.sub['values'] = subjects
            self.sub.set("")  # Clear subject selection
            self.chapter.set("")  # Clear chapter selection in case of previous values
            self.chapter['values'] = []
    
    # Update chapters based on subject selection
    def update_chapters(self, event=None):
        selected_class = self.cls.get()
        selected_subject = self.sub.get()
        if selected_class in data and selected_subject in data[selected_class]:
            chapters = data[selected_class][selected_subject]
            self.chapter['values'] = chapters
            self.chapter.set("")  # Clear chapter selection

    def show_ques(self):
        self.Text2.delete("1.0", tk.END)
        result = ques_fetch(cls,subj,chapter)

        # Formatting and displaying each item
        for i, row in enumerate(result, start=1):
            self.Text2.insert(tk.END, f"{i}. {row[0]}\n")  # Display each question on a new line with numbering

        # Scroll to the top
        self.Text2.yview_moveto(0)

        #messagebox.showinfo(title="Question Added", message="Question has been added!!")
        #self.Text2.delete("1.0", "end")