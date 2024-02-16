from tkinter import *
import tkinter.messagebox as MessageBox
import datetime
import mysql.connector as mysql
from subprocess import call



date=datetime.datetime.now().date()
date=str(date)

class application:
    def __init__(self,master):
        self.master=master

        def submit():
            user=StringVar()
            pwd=StringVar()
            user=e_user.get()
            pwd=e_pwd.get()
            mode=i.get()

            if (user == "" or pwd == "" ):
                MessageBox.showinfo("Invalid insert", "All Fields are Required")

            #admin
            elif (mode == "1"):
                if ( user == "Administrator" and pwd == "admin"):
                    MessageBox.showinfo("Successful", "Welcome Admin")
                    call(["python","admin.py"])
                else:
                    MessageBox.showinfo("Invalid insert", "Username or Password is wrong")

            #staff
            elif (mode == "2"):
                con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                cur=con.cursor()
                cur.execute("SELECT * FROM Staff WHERE staffid='"+user+"'")
                res=cur.fetchall()
                for x in res:
                    userchk=x[0]
                    pwdchk=x[1]
                    if(user == userchk and pwd == pwdchk):
                        MessageBox.showinfo("Successful","Welcome Management Staff")
                        call(["python","staff.py"])
                else:
                    MessageBox.showinfo("Invalid insert", "Username or Password is wrong")
            
            #customers
            elif (mode == "3"):
                con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                cur=con.cursor()
                cur.execute("SELECT * FROM Customer WHERE custid='"+user+"'")
                res=cur.fetchall()
                for x in res:
                    userchk=x[0]
                    pwdchk=x[1]
                    if(user == userchk and pwd == pwdchk):
                        MessageBox.showinfo("Successful", "Welcome Customer")
                        call(["python","customer.py"])
                else:
                    MessageBox.showinfo("Invalid insert", "Username or Password is wrong")
                    
        
        def Clear():
            e_user.delete(0,END)
            e_pwd.delete(0,END)
            e_user.focus()


        #frames
        self.top=Frame(master,height=140,bg="white")
        self.top.pack(fill=X)

        self.bottom=Frame(master,height=580,bg="pink")
        self.bottom.pack(fill=X)

        #frame labels
        self.image1=PhotoImage(file='icon\money.png')
        self.image1lbl=Label(self.top, image=self.image1, bg="white")
        self.image1lbl.place(x=490,y=15)

        self.image2=PhotoImage(file='icon\money.png')
        self.image2lbl=Label(self.top, image=self.image2, bg="white")
        self.image2lbl.place(x=865,y=15)

        self.heading=Label(self.top,text=" Golden Horizon Bank",font="arial 15 bold",bg="white")
        self.heading.place(x=600,y=30)

        self.heading=Label(self.top,text="LOGIN",font=('Cambria','15','bold'),bg="white")
        self.heading.place(x=655,y=90)

        self.date_lbl=Label(self.bottom,text="Date : "+date,bg="pink")
        self.date_lbl.place(x=650,y=20)

        #lable and enteries
        self.user_lbl=Label(self.bottom,text="Username : ",font="arial 15 bold",bg="pink")
        self.user_lbl.place(x=480,y=100)

        self.pwd_lbl=Label(self.bottom,text="Password : ",font="arial 15 bold",bg="pink")
        self.pwd_lbl.place(x=480,y=180)

        e_user=Entry(self.bottom,width="40")
        e_user.place(x=630,y=105)

        e_pwd=Entry(self.bottom,width="40",show="*")
        e_pwd.place(x=630,y=185)

        #buttons
        i=StringVar()
        Radiobutton(self.bottom, text="Administrator",  value="1", bg="pink", variable=i).place(x=500, y=260)
        Radiobutton(self.bottom, text="Bank Staff",  value="2", bg="pink", variable=i).place(x=630, y=260)
        Radiobutton(self.bottom, text="Customer",  value="3", bg="pink", variable=i).place(x=750, y=260)

        self.clr=Button(self.bottom,text="Clear",font="arial 15 bold",width="6",command=Clear)
        self.clr.place(x=600,y=335)

        self.sub=Button(self.bottom,text=" Submit ",font="arial 15 bold",width="10",command=submit)
        self.sub.place(x=700,y=335)

        self.Qui=Button(self.bottom,text="Quit",font="arial 15 bold",width="5",command=quit)
        self.Qui.place(x=670,y=415)


root=Tk()
root.title("BANK MANAGEMENT SYSTEM")
app=application(root)
root.geometry("1366x768")
root.resizable(True,True)
root.mainloop()
