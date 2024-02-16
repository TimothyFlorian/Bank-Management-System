from tkinter import *
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql

class application:
    def __init__(self,master):
        self.master=master

        def submit():
            acc_no = DoubleVar()
            acc_no = (e_acc_no.get())

            if (acc_no == "" ):
                MessageBox.showinfo("Illegal insert", "All Fields are Required")    
            else:
                con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                cur=con.cursor()
                cur.execute("SELECT amount FROM Acc where acc_no='" + acc_no + "'")
                res = cur.fetchall()
                for x in res:
                    e_detail.insert(0,x)    
                cur.execute("COMMIT")
                con.close()
             

        #frames
        self.top=Frame(master,height=100,bg="white")
        self.top.pack(fill=X)

        self.bottom=Frame(master,height=800,bg="pink")
        self.bottom.pack(fill=X)

        #frame labels
        self.image1=PhotoImage(file='icon\money.png')
        self.image1lbl=Label(self.top, image=self.image1, bg="white")
        self.image1lbl.place(x=50, y=15)

        self.image2=PhotoImage(file='icon\money.png')
        self.image2lbl=Label(self.top, image=self.image2, bg="white")
        self.image2lbl.place(x=580, y=15)

        self.heading=Label(self.top,text="Balance Enquiry",font="arial 18 bold",bg="white")
        self.heading.place(x=265, y=30)

        #buttons and lables
        acc_no= DoubleVar()
        acc_no = Label(self.bottom, text="Account number  :", font="arial 14 bold", bg="pink")
        acc_no.place(x=40, y=55)

        detail = Label(self.bottom, text="Details  :", font="arial 14 bold", bg="pink")
        detail.place(x=40, y=110)

        e_acc_no = Entry(self.bottom, width= "60", textvariable=acc_no)
        e_acc_no.place(x=320, y=55)

        e_detail = Entry(self.bottom, width="60" )
        e_detail.place(x=320 , y= 110)

        #submit
        self.sub= Button(self.bottom, text=" Submit ", font="arial 15 bold", width="10", command=submit)
        self.sub.place(x=300 , y=200)

root=Tk()
root.title("BANK MANAGEMENT SYSTEM")
app=application(root)
root.geometry("700x400+200+20")
root.resizable(height = 0, width = 0)
root.mainloop()