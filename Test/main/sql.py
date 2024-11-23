from tkinter import messagebox 
import mysql.connector as my
import random


con = my.connect(host = 'localhost', user = 'root', password = '1234', database = 'smdb')
cur = con.cursor()

def login(id,passwd,self,controller):
    global userid,password
    userid=id.get()
    password=passwd.get()
    
    print("The name is : " + userid)
    print("The password is : " + password)

    Q = "select type from login where userid = %s and passwd = %s;"
    val=(userid,password)

    cur.execute(Q,val)
    result = cur.fetchall()

    if result == []:
        messagebox.showerror(title="Login Status",message="Invalid UserId or Password")
        
    else:
        for i in result:
            for j in i:
                if j =="A":
                    from adm_wlcm import admin
                    controller.show_frame(admin)
                elif j =="S":
                    from stu_wlcm import student
                    controller.show_frame(student)
                    profile()
                    print(var)
                    
                    
    
    id.set("")
    passwd.set("")



def enrollment(name,roll,cls,sec,adm,fname,mname,phone,add,self,controller):
    stu_name = name.get()
    stu_roll = roll.get()
    stu_cls = cls.get()
    stu_sec = sec.get()
    stu_adm = adm.get()
    stu_fname = fname.get()
    stu_mname = mname.get()
    stu_phone = phone.get()
    stu_add = add.get()

    r = random.randint(1000,9999)
    stu_pass = random.randint(10000,99999)
    stu_id = "ST"+ str(r)

    Q = "Insert into students (userid,name,roll,class,sec,fname,mname,address,phone,admno,passwd) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"
    val = (stu_id,stu_name,stu_roll,stu_cls,stu_sec,stu_fname,stu_mname,stu_add,stu_phone,stu_adm,stu_pass)

    cur.execute(Q,val)
    con.commit()
    
    Q = "Insert into login (userid,passwd,type,name) values(%s,%s,%s,%s)"
    values = (stu_id,stu_pass,"S",stu_name)

    cur.execute(Q,values)
    con.commit()
    
    messagebox.showinfo(title="Login Credentials", message=" UserId : {id} \n Password : {passw}".format(id = stu_id,passw = stu_pass))

    name.set("")
    roll.set("")
    cls.set("")
    sec.set("")
    sec.set("")
    adm.set("")
    fname.set("")
    mname.set("")
    phone.set("")
    add.set("")


def profile():

    global userid

    # code for info retival
    global name, cls, sec, roll, adm, fname, mname, add, phone, var
    Q = "Select name,class,sec,roll,admno,fname,mname,address,phone from students where userid = %s;"
    val = [userid]

    cur.execute(Q,val)
    res = cur.fetchall()

    for row in res:
        name, cls, sec, roll, adm, fname, mname, add, phone = row
        var = [name, cls, sec, roll, adm, fname, mname, add, phone]

    return var

def fetch(index):
    return var[index]


def stu_details(self,id): # Fetch details for attendance

    user_id = id
    global variable
    Q = "Select name,class,sec,roll from students where userid = %s;"
    val = [user_id]

    cur.execute(Q,val)
    res = cur.fetchall()

    for row in res:
        name,cls,sec,roll = row
    variable = [name,cls,sec,roll]
    print(variable)
    return variable

def show(index):
    return variable[index]


def atd_update(id,pres,ab,ttl):
    global percent
    user_id = id
    pres_days = int(pres)
    ab_days = int(ab)
    total_days = int(ttl)

    percent = pres_days/total_days*100
    
    print(user_id,pres_days,ab_days,percent)
    Q = "Update students set totaldays = %s, present = %s, absent = %s, percent = %s where userid = %s"
    val = [total_days,pres_days,ab_days,percent,user_id]

    cur.execute(Q,val)
    con.commit()

def show_percent():
    return percent


def stu_percent():
    Q = "Select totaldays, present,absent, percent from students where userid = %s"
    val = [userid]

    cur.execute(Q,val)
    res = cur.fetchall()
    for row in res:
        total,present,absent,percentage = row
        value = [total,present,absent,percentage]
    return value


def adm_msgsent(msg):
    Q = "Insert into message values (%s,%s,%s,%s,now());"
    val = ("admin","admin","A",msg)

    cur.execute(Q,val)
    con.commit()

    messagebox.showinfo(title="Message Sent", message="Message has been sent!!")


def stu_msgsent(msg):
    Q = "Select name from students where userid = %s;"
    val = [userid]

    cur.execute(Q,val)
    res = cur.fetchall()

    for row in res:
        for i in row:
            name = i

    
    Q = "Insert into message values (%s,%s,%s,%s,now());"
    val = (userid,name,"S",msg)

    cur.execute(Q,val)
    con.commit()

    messagebox.showinfo(title="Message Sent", message="Message has been sent!!")


def fetch_data_admin(type):
    if type == "Self":
        t = "A"
    else:
        t = "S"

    Q = "Select userid,name,message from message where type = %s order by date desc;"
    val = [t]
    cur.execute(Q,val)
    rows = cur.fetchall()
    
    columns = [description[0] for description in cur.description]
    return columns,rows


def fetch_data_stu(type):
    if type == "Self":
        t = userid
    else:
        t = "A"

    Q = "Select userid,name,message from message where type = %s or userid = %s order by date desc;"
    val = [t,t]
    cur.execute(Q,val)
    rows = cur.fetchall()
    
    columns = [description[0] for description in cur.description]
    return columns,rows



def format_table(columns, rows):
    # Create a header
    header = " | ".join(f"{col:<15}" for col in columns)  # Adjust column width as needed
    separator = "-" * len(header)
    
    # Create each row of data
    data = "\n".join(" | ".join(f"{str(item):<15}" for item in row) for row in rows)
    
    # Combine header, separator, and data
    table = f"{header}\n{separator}\n{data}"
    return table



def ques(qus,stu_cls,sub,ch):
    ques_var = str(qus)
    cls_var = stu_cls.get()
    subj_var = sub.get()
    chap_var = ch.get()

    print(cls_var,subj_var,chap_var,ques_var)
    Q = "Insert into questions values (%s,%s,%s,%s);"
    val = [cls_var,subj_var,chap_var,ques_var]

    cur.execute(Q,val)
    con.commit()
    

def ques_fetch(stu_cls,sub,ch):
    cls_var = stu_cls.get()
    subj_var = sub.get()
    chap_var = ch.get()

    Q = "Select ques from questions where class = %s and subject = %s and chapter = %s order by rand() limit 5;"
    val = [cls_var,subj_var,chap_var]

    cur.execute(Q,val)
    res = cur.fetchall()
    return res
