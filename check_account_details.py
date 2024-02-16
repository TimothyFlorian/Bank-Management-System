from tkinter import *
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql

class application:
    def __init__(self,master):
        self.master=master

        def submit():
            acc_no= DoubleVar()
            acc_no = (e_acc_no.get())

            if (acc_no == "" ):
                MessageBox.showinfo("Illegal insert", "All Fields are Required")    
            else:
                con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                cur=con.cursor()
                cur.execute("SELECT * FROM Acc WHERE acc_no='" + acc_no + "'")
                res = cur.fetchall()

                for x in res:
                    e_fname.insert(0,x[1])
                    e_lname.insert(0,x[2])
                    e_dob.insert(0,x[3])
                    e_acc_type.insert(0,x[4])
                    e_amount.insert(0,x[5])
                    e_address.insert(0,x[6])
                    e_phone_no.insert(0,x[7])
                    e_sex.insert(0,x[8])
                 
                cursor.execute("commit")
                con.close()

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

        self.heading=Label(self.top,text="Check Account Details",font="arial 18 bold",bg="white")
        self.heading.place(x=600,y=30)

        #buttons and lables
        acc_no= DoubleVar()
        acc_no = Label(self.bottom, text="Account number ", font="arial 14 bold", bg="pink")
        acc_no.place(x=40, y=55)

        fname = Label(self.bottom, text="First Name ", font="arial 14 bold", bg="pink")
        fname.place(x=40, y=110)

        lname = Label(self.bottom, text="Last Name ", font="arial 14 bold", bg="pink")
        lname.place(x=40, y=165)
        
        dob = Label(self.bottom, text="Date of Birth ", font="arial 14 bold", bg="pink")
        dob.place(x=40,y=220)

        acc_type = Label(self.bottom, text="Account Type ", font="arial 14 bold", bg="pink")
        acc_type.place(x=40, y=275)

        amount= DoubleVar()
        amount = Label(self.bottom, text="Initial Amount ", font="arial 14 bold", bg="pink")
        amount.place(x=40, y=330)

        address = Label(self.bottom, text="Address ", font="arial 14 bold", bg="pink")
        address.place(x=40, y=385)
        
        phone_no= DoubleVar()
        phone_no = Label(self.bottom, text="Phone Number ", font="arial 14 bold", bg="pink")
        phone_no.place(x=40, y=440)

        sex = Label(self.bottom, text="Sex ", font="arial 14 bold", bg="pink")
        sex.place(x=40, y=495)


        #Enteries

        e_acc_no= Entry(self.bottom, width= "60", textvariable=acc_no)
        e_acc_no.place(x=320, y=55)

        e_fname= Entry(self.bottom, width= "60")
        e_fname.place(x=320, y=110)

        e_lname= Entry(self.bottom, width= "60")
        e_lname.place(x=320, y=165)

        e_dob= Entry(self.bottom, width= "40")
        e_dob.place(x=320,y=220)

        e_acc_type= Entry(self.bottom, width= "40")
        e_acc_type.place(x=320, y=275)

        e_amount= Entry(self.bottom, width= "60")
        e_amount.place(x=320, y=330)

        e_address= Entry(self.bottom, width= "60")
        e_address.place(x=320, y=385)
        
        e_phone_no= Entry(self.bottom, width= "60")
        e_phone_no.place(x=320, y=440)

        e_sex= Entry(self.bottom, width= "40" )
        e_sex.place(x=320, y=495)

        #submit
        self.sub= Button(self.bottom, text=" Submit ", font="arial 15 bold", width="10", command=submit)
        self.sub.place(x=320 , y=540)

        self.qt= Button(self.bottom, text=" Quit", font="arial 15 bold", width="10", command=quit)
        self.qt.place(x=520 , y=540)

root=Tk()
root.title("BANK MANAGEMENT SYSTEM")
app=application(root)
root.geometry("1366x768")
root.resizable(True,True)
root.mainloop()

