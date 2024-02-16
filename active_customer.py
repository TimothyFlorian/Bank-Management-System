from tkinter import *
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql


class application:
    def __init__(self,master):
        self.master=master

        #frames
        self.top= Frame(master, height=100 , bg= "white")
        self.top.pack(fill=X)

        self.bottom= Frame(master, height=800, bg="pink")
        self.bottom.pack(fill=X)

        self.top_image=PhotoImage(file='icon/money.png')
        self.top_image_lable= Label(self.top, image=self.top_image, bg="white")
        self.top_image_lable.place(x=50, y=15)

        self.top_image2=PhotoImage(file='icon/money.png')
        self.top_image2_lable= Label(self.top, image=self.top_image, bg="white")
        self.top_image2_lable.place(x=580, y=15)

        self.heading= Label(self.top, text="All Active Customers", font="arial 18 bold", bg="white")
        self.heading.place(x= 185, y=30)

        lb= Listbox(self.bottom,height="35", width="110" )
        lb.place(x=20 , y= 20)

        con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
        cur=con.cursor()
        cur.execute("SELECT * FROM Customer ")
        res = cur.fetchall()
        for x in res:
            lb.insert(1, "User Id:   "+ x[0]+"                        Password:   "+ x[1])
        cur.execute("COMMIT")
        con.close()

root=Tk()
root.title("BANK MANAGEMENT SYSTEM")
app=application(root)
root.geometry("700x700+300+0")
root.resizable(height = 0, width = 0)
root.mainloop()