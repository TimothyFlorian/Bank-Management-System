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
            opassw= StringVar()
            npassw= StringVar()
            user= (e_user.get())
            opassw=(e_opass.get())
            npassw=(e_npass.get())
            mode= (i.get())
            if (user == "" or opassw == "" or npassw == "" ):
                MessageBox.showinfo("Illegal insert", "All Fields are Required")
            else:
                if (mode == "2"):
                    con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                    cur=con.cursor()
                    cur.execute("SELECT * FROM Staff WHERE staffid='" + user + "'")
                    res = cur.fetchall()
                    for x in res:
                        uchk=x[0]
                        pchk=x[1]
                        if (user == uchk and opassw == pchk):
                            con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                            cur=con.cursor()
                            cur.execute("UPDATE Staff SET passwd='"+ npassw +"' WHERE staffid='"+user+"' AND passwd='"+opassw+"'")
                            cur.execute("COMMIT")
                            MessageBox.showinfo("Sucessful", "Password Changed")
                        else:
                            MessageBox.showinfo("Illegal Insert", "Wrong password")
                else:
                    if (mode == "3"):
                        con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                        cur=con.cursor()
                        cur.execute("SELECT * FROM Customer WHERE custid='" + user + "'")
                        res = cur.fetchall()
                        for x in res:
                            uchk=x[0]
                            pchk=x[1]
                            if (user == uchk and opassw == pchk):
                                con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                                cur=con.cursor()
                                cur.execute("UPDATE Customer SET pass='"+ npassw +"' WHERE custid='"+user+"' AND pass='"+opassw+"'")
                                cur.execute("COMMIT")
                                MessageBox.showinfo("Sucessful", "Password Changed")
                            else:
                                MessageBox.showinfo("Illegal Insert", "Wrong password")

        def Clear():
            e_user.delete(0,END)
            e_opass.delete(0,END)
            e_npass.delete(0,END)
            e_user.focus()

        #frames

        self.top= Frame(master, height=140 , bg= "white")
        self.top.pack(fill=X)

        self.bottom= Frame(master, height=530, bg="pink")
        self.bottom.pack(fill=X)

        #top Frame design
        self.top_image=PhotoImage(file='icon/money.png')
        self.top_image_lable= Label(self.top, image=self.top_image, bg="white")
        self.top_image_lable.place(x=70, y=15)

        self.top_image2=PhotoImage(file='icon/money.png')
        self.top_image2_lable= Label(self.top, image=self.top_image, bg="white")
        self.top_image2_lable.place(x=480, y=15)

        self.heading= Label(self.top, text="Golden Horizon Bank", font="arial 15 bold", bg="white")
        self.heading.place(x= 180, y=30)
        self.heading= Label(self.top, text="Change User Password", font="arial 19 bold", bg="white")
        self.heading.place(x= 170, y=90)

        self.date_lbl = Label(self.bottom, text="Date : "+date, bg="pink")
        self.date_lbl.place(x=250, y=20)

        #Lable and Enteries
        self.user_lbl = Label(self.bottom, text="Username : ", bg="pink", font="arial 15 bold")
        self.user_lbl.place(x=70, y=70)

        self.oppass_lbl = Label(self.bottom, text="Old Password : ", bg="pink", font="arial 15 bold")
        self.oppass_lbl.place(x=70, y=150)

        self.nppass_lbl = Label(self.bottom, text="New Password : ", bg="pink", font="arial 15 bold")
        self.nppass_lbl.place(x=70, y=230)

        e_user= Entry(self.bottom, width= "40")
        e_user.place(x=270, y=75)

        e_opass= Entry(self.bottom, width= "40")
        e_opass.place(x=270, y=155)

        e_npass= Entry(self.bottom, width= "40")
        e_npass.place(x=270, y=235)

        i= StringVar()
        Radiobutton(self.bottom, text="Bank Staff",  value="2", bg="pink", variable=i).place(x=175, y=300)
        Radiobutton(self.bottom, text="Customer",  value="3", bg="pink", variable=i).place(x=345, y=300)

        # submit
        self.submit= Button(self.bottom, text=" Submit ", font="arial 15 bold", width="10", command=submit)
        self.submit.place(x=100 , y=365)

        self.clr=Button(self.bottom,text="Clear",font="arial 15 bold",width="10",command=Clear)
        self.clr.place(x=300,y=365)

root=Tk()
root.title("BANK MANAGEMENT SYSTEM")
app=application(root)
root.geometry("600x580+200+20")
root.resizable(height = 0, width = 0)
root.mainloop()