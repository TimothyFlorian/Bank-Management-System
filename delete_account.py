from tkinter import *
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql

class application:
    def __init__(self,master):
        self.master=master

        def delt():
            acc_no= DoubleVar()
            acc_no = (e_acc_no.get())

            if (acc_no == "" ):
                MessageBox.showinfo("ID is required for delete", "All Fields are Required")    
            else:
                con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                cur=con.cursor()
                cur.execute("DELETE FROM Acc WHERE acc_no='" + acc_no + "'")
                cur.execute("COMMIT")
                e_detail.delete(1,'end')
                e_detail.delete(2,'end')
                e_detail.delete(3,'end')
                e_detail.delete(4,'end')
                e_detail.delete(5,'end')
                e_detail.delete(6,'end')
                e_detail.delete(7,'end')
                e_detail.delete(8,'end')
                e_detail.delete(9,'end')
                e_detail.delete(10,'end')
                e_detail.delete(11,'end')
                e_detail.delete(12,'end')
                e_detail.delete(13,'end')
                e_detail.delete(14,'end')
                e_acc_no.delete(0,'end')
                MessageBox.showinfo("Delete Status", "Deleted Successfully")
                con.close()

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
                print(res)
                for x in res:
                    e_detail.insert(1,"Account Number : "+x[0])
                    e_detail.insert(2,"Name                     : "+x[1] + " " + x[2])
                    e_detail.insert(3,"Date of Birth          : "+x[3])
                    e_detail.insert(4,"Account Type        : "+x[4])
                    e_detail.insert(5,"Amount                  : "+str(x[5]))
                    e_detail.insert(6,"Address                  : "+x[6])
                    e_detail.insert(7,"Phone Number     : "+str(x[7]))
                    e_detail.insert(8,"Sex                          : "+x[8])
                    
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

        self.heading=Label(self.top,text="Delete Account",font="arial 18 bold",bg="white")
        self.heading.place(x=265, y=30)

        #buttons and lables
        acc_no= DoubleVar()
        acc_no = Label(self.bottom, text="Account number  :", font="arial 14 bold", bg="pink")
        acc_no.place(x=40, y=55)

        detail = Label(self.bottom, text="Details  :", font="arial 14 bold", bg="pink")
        detail.place(x=40, y=110)

        #Enteries
        e_acc_no = Entry(self.bottom, width= "60", textvariable=acc_no)
        e_acc_no.place(x=320, y=55)

        e_detail = Listbox(self.bottom, height="16", width="60" )
        e_detail.place(x=320 , y= 110)

        #Buttons
        self.sub= Button(self.bottom, text=" Submit ", font="arial 15 bold", width="10", command=submit)
        self.sub.place(x=60 , y=270)

        self.dlt= Button(self.bottom, text=" Delete ", font="arial 15 bold", width="10", command=delt)
        self.dlt.place(x=60 , y=330)


root=Tk()
root.title("BANK MANAGEMENT SYSTEM")
app=application(root)
root.geometry("700x500+200+20")
root.resizable(height = 0, width = 0)
root.mainloop()