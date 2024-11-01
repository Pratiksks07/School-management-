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

