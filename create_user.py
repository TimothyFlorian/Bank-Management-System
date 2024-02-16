from tkinter import *
import datetime
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql

date = datetime.datetime.now().date()
date= str(date)


class application:
    def __init__(self,master):
        self.master=master

        def submit():
            user= StringVar()
            passw= StringVar()
            user= (e_user.get())
            passw=(e_pass.get())
            mode= (i.get())
            if (user == "" or passw == "" ):
                MessageBox.showinfo("Illegal insert", "All Fields are Required")
            else:
                if (mode == "2"):
                    con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                    cur=con.cursor()
                    cur.execute("INSERT INTO Staff VALUES('" + user + "','"+ passw +"')")
                    cur.execute("COMMIT")
                    MessageBox.showinfo("Insert Status", "User Created Sucessfully")
                else:
                    if (mode == "3"):
                        con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                        cur=con.cursor()
                        cur.execute("INSERT INTO Customer VALUES('" + user + "','"+ passw +"')")
                        cur.execute("COMMIT")
                        MessageBox.showinfo("Insert Status", "User Created Sucessfully")

        def Clear():
            e_user.delete(0,END)
            e_pass.delete(0,END)
            e_user.focus()


        #frames
        self.top=Frame(master,height=100,bg="white")
        self.top.pack(fill=X)

        self.bottom=Frame(master,height=600,bg="pink")
        self.bottom.pack(fill=X)

        #frame labels
        self.image1=PhotoImage(file='icon\money.png')
        self.image1lbl=Label(self.top, image=self.image1, bg="white")
        self.image1lbl.place(x=70, y=15)

        self.image2=PhotoImage(file='icon\money.png')
        self.image2lbl=Label(self.top, image=self.image2, bg="white")
        self.image2lbl.place(x=480, y=15)

        self.heading=Label(self.top,text=" Golden Horizon Bank",font="arial 15 bold",bg="white")
        self.heading.place(x= 180, y=20)

        self.heading= Label(self.top, text="Create User", font="arial 14 bold", bg="white")
        self.heading.place(x= 230, y=55)

        self.date_lbl=Label(self.bottom,text="Date : "+date,bg="pink")
        self.date_lbl.place(x=250, y=20)

        #Lable and Enteries
        self.user_lbl = Label(self.bottom, text="Username : ", bg="pink", font="arial 15 bold")
        self.user_lbl.place(x=90, y=100)

        self.pass_lbl = Label(self.bottom, text="Password : ", bg="pink", font="arial 15 bold")
        self.pass_lbl.place(x=90, y=180)

        e_user= Entry(self.bottom, width= "40")
        e_user.place(x=240, y=105)

        e_pass= Entry(self.bottom, width= "40")
        e_pass.place(x=240, y=185)

        i= StringVar()
        Radiobutton(self.bottom, text="Bank Staff",  value="2", bg="pink", variable=i).place(x=175, y=260)
        Radiobutton(self.bottom, text="Customer",  value="3", bg="pink", variable=i).place(x=345, y=260)

        # submit
        self.sub= Button(self.bottom, text=" Submit ", font="arial 15 bold", width="10", command=submit)
        self.sub.place(x=200 , y=335)

        self.clr=Button(self.bottom,text="Clear",font="arial 15 bold",width="10",command=Clear)
        self.clr.place(x=200,y=400)

root=Tk()
root.title("BANK MANAGEMENT SYSTEM")
app=application(root)
root.geometry("600x570+150+20")
root.resizable(height = 0, width = 0)
root.mainloop()