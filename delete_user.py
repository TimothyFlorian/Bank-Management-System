from tkinter import *
import tkinter.messagebox as MessageBox
from subprocess import call
import mysql.connector as mysql

class application:
    def __init__(self,master):
        self.master=master

        def delt():
            user= StringVar()
            user = (e_user.get())
            mode= (i.get())
            if (user == "" ):
                MessageBox.showinfo("ID is required for delete", "All Fields are Required")    
            else:
                if( mode == "2" ):
                    con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                    cur=con.cursor()
                    cur.execute("DELETE FROM Staff WHERE staffid='" + user + "'")
                    res = cur.fetchall()
                    for x in res:
                        lb.delete(1,"end" )
                        lb.delete(2,"end")
                        lb.delete(3,"end")
                        lb.delete(4,"end")
                    MessageBox.showinfo("Sucessful", "User has been Deleted")
                    cur.execute("COMMIT")
                    con.close()
                else:
                    if( mode == "3"):
                        con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                        cur=con.cursor()
                        cur.execute("DELETE FROM Customer WHERE custid='" + user + "'")
                        res = cur.fetchall()
                        for x in res:
                            lb.delete(1,"end" )
                            lb.delete(2,"end")
                            lb.delete(3,"end")
                            lb.delete(4,"end")
                        MessageBox.showinfo("Sucessful", "User has been Deleted")
                        cur.execute("COMMIT")
                        con.close()

        def submit():
            user= StringVar()
            user = (e_user.get())
            mode= (i.get())

            if (user == "" ):
                MessageBox.showinfo("Illegal insert", "All Fields are Required")    
            else:
                if( mode == "2" ):
                    con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                    cur=con.cursor()
                    cur.execute("SELECT * FROM Staff WHERE staffid='" + user + "'")
                    res = cur.fetchall()
                    for x in res:
                        lb.insert(1,"User ID :" )
                        lb.insert(2,x[0])
                        lb.insert(3,"Password:")
                        lb.insert(4,x[1])
                    cur.execute("COMMIT")
                    con.close()
                else:
                    if( mode == "3"):
                        con=mysql.connect(host="localhost",user="root",password="1205",database="bank_management")
                        cur=con.cursor()
                        cur.execute("SELECT * FROM Customer WHERE custid='" + user + "'")
                        res = cur.fetchall()
                        for x in res:
                            lb.insert(1,"User ID :  "+x[0] )
                            lb.insert(2,"Password:  "+x[1])
                        cur.execute("COMMIT")
                        con.close()

        def Clear():
            e_user.delete(0,END)
            lb.delete(0,END)
            e_user.focus()

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

        self.heading=Label(self.top,text="Delete User",font="arial 18 bold",bg="white")
        self.heading.place(x= 285, y=30)

        #buttons and lables
        user_lbl = Label(self.bottom, text="User Name : ", font="arial 14 bold", bg="pink")
        user_lbl.place(x=90, y=55)

        i= StringVar()
        Radiobutton(self.bottom, text="Bank Staff",  value="2", bg="pink", variable=i).place(x=380, y=110)
        Radiobutton(self.bottom, text="Customer",  value="3", bg="pink", variable=i).place(x=520, y=110)

        #Enteries
        user= StringVar()
        e_user= Entry(self.bottom, width= "60", textvariable=user)
        e_user.place(x=320, y=55)


        #list
        lb=Listbox(self.bottom,height="10", width="60" )
        lb.place(x=320 , y= 180)



        #submit
        self.sub=Button(self.bottom, text=" Submit ", font="arial 15 bold", width="10", command=submit)
        self.sub.place(x=60 , y=200)

        self.delu= Button(self.bottom, text=" Delete ", font="arial 15 bold", width="10", command=delt)
        self.delu.place(x=60 , y=250)

        self.clr=Button(self.bottom,text="Clear",font="arial 15 bold",width="10",command=Clear)
        self.clr.place(x=60,y=300)

root=Tk()
root.title("BANK MANAGEMENT SYSTEM")
app=application(root)
root.geometry("700x500+200+20")
root.resizable(height = 0, width = 0)
root.mainloop()
