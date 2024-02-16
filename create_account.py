from tkinter import *
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql
import datetime

date = datetime.datetime.now().date()
date= str(date)

class application:
    def __init__(self,master):
        self.master=master

        def submit():
            acc_no= DoubleVar()
            amount= DoubleVar()
            phone_no= DoubleVar()
            acc_no = (e_acc_no.get())
            fname = (e_fname.get())
            lname = (e_lname.get())
            dob= (e_dob.get())
            acc_type = (t.get())
            amount = (e_amount.get())
            address = (e_address.get())
            phone_no = (e_phone_no.get())
            sex = (i.get())

            if (acc_no == "" or fname == "" or acc_type == "" or amount =="" or address =="" or phone_no == "" or sex ==""):
                MessageBox.showinfo("Illegal insert", "All Fields are Required")

            else:
                con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                cur=con.cursor()
                cur.execute("INSERT INTO Acc VALUES('" + acc_no + "','"+ fname +"','"+ lname +"','"+ dob +"', '"+ acc_type +"','"+ amount +"' , '"+ address +"','" + phone_no + "', '"+ sex +"')")
                cur.execute("COMMIT")
                MessageBox.showinfo("Insert Status", "Inserted Successfully")
                e_acc_no.delete(0, 'end')
                e_fname.delete(0,'end')
                e_lname.delete(0,'end')
                e_amount.delete(0,'end')
                e_address.delete(0,'end')
                e_phone_no.delete(0,'end')
                e_dob.delete(0,'end')
                e_acc_no.focus()
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

        self.heading=Label(self.top,text="  Create Account",font="arial 18 bold",bg="white")
        self.heading.place(x=600,y=30)

        #buttons and lables
        acc_no= DoubleVar()
        acc_no = Label(self.bottom, text="Account number ", font="arial 14 bold", bg="pink")
        acc_no.place(x=40, y=55)

        fname = Label(self.bottom, text="First Name ", font="arial 14 bold", bg="pink")
        fname.place(x=40, y=110)

        lname = Label(self.bottom, text="Last Name ", font="arial 14 bold", bg="pink")
        lname.place(x=40, y=165)

        acc_type = Label(self.bottom, text="Account Type ", font="arial 14 bold", bg="pink")
        acc_type.place(x=40, y=220)

        amount= DoubleVar()
        amount = Label(self.bottom, text="Initial Amount ", font="arial 14 bold", bg="pink")
        amount.place(x=40, y=275)

        address = Label(self.bottom, text="Address ", font="arial 14 bold", bg="pink")
        address.place(x=40, y=330)
        
        phone_no= DoubleVar()
        phone_no = Label(self.bottom, text="Phone Number ", font="arial 14 bold", bg="pink")
        phone_no.place(x=40, y=385)

        sex = Label(self.bottom, text="Sex ", font="arial 14 bold", bg="pink")
        sex.place(x=40, y=440)

        dob = Label(self.bottom, text="Date of Birth ", font="arial 14 bold", bg="pink")
        dob.place(x=40, y=495)

        #Enteries
        
        e_acc_no= Entry(self.bottom, width= "60", textvariable=acc_no)
        e_acc_no.place(x=320, y=55)

        e_fname= Entry(self.bottom, width= "60")
        e_fname.place(x=320, y=110)

        e_lname= Entry(self.bottom, width= "60")
        e_lname.place(x=320, y=165)

        t= StringVar()
        Radiobutton(self.bottom, text="Savings Account",  value="Savings", bg="pink", variable=t).place(x=320, y=220)
        Radiobutton(self.bottom, text="Current Account",  value="Current", bg="pink", variable=t).place(x=450, y=220)

        e_amount= Entry(self.bottom, width= "60")
        e_amount.place(x=320, y=275)

        e_address= Entry(self.bottom, width= "60")
        e_address.place(x=320, y=330)
        
        e_phone_no= Entry(self.bottom, width= "60")
        e_phone_no.place(x=320, y=385)

        i= StringVar()
        Radiobutton(self.bottom, text="Male",  value="Male", bg="pink", variable=i).place(x=320, y=440)
        Radiobutton(self.bottom, text="Female",  value="Female", bg="pink", variable=i).place(x=430, y=440)

        e_dob= Entry(self.bottom, width= "60")
        e_dob.place(x=320, y=495)

        #submit
        self.sub= Button(self.bottom, text=" Submit ", font="arial 15 bold", width="30", command=submit)
        self.sub.place(x=320 , y=540)

root=Tk()
root.title("BANK MANAGEMENT SYSTEM")
app=application(root)
root.geometry("1366x768")
root.resizable(True,True)
root.mainloop()