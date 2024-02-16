from tkinter import *
import datetime
from subprocess import call



def balance_enquiry():
    call(["python","balance_enquiry.py"])

def check_account_details():
    call(["python","check_account_details.py"])

def withdraw_amount():
    call(["python","withdraw_amount.py"])

def deposit_amount():
    call(["python","deposit_amount.py"])

def pwd_admin():
    call(["python", "pwd_admin.py"])



date = datetime.datetime.now().date()
date= str(date)


class application:
    def __init__(self,master):
        self.master=master

        def logout():
            master.quit()

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

        self.date_lbl=Label(self.bottom,text="Date : "+date,bg="pink")
        self.date_lbl.place(x=650,y=20)

        self.welcome_lbl=Label(self.bottom,text="Welcome Customer",bg="pink",font="arial 18 bold")
        self.welcome_lbl.place(x=590, y=42)

        #buttons and labels

        #balance enquiry
        self.be=Button(self.bottom,text="Balance Enquiry",font="arial 13 bold",width=20,command=balance_enquiry)
        self.be.place(x=80, y=100)
        self.be_lbl=Label(self.bottom,text="--> Check account balance",bg="pink",font="arial 13 bold")
        self.be_lbl.place(x=320, y=102)

        #Withdraw Amount
        self.wa=Button(self.bottom,text="Withdraw Amount",font="arial 13 bold",width=20,command=withdraw_amount)
        self.wa.place(x=80, y=200)
        self.wa_lbl=Label(self.bottom,text="--> Withdraw amount from user account",bg="pink",font="arial 13 bold")
        self.wa_lbl.place(x=320, y=202)

        #Deposit Amount
        self.da=Button(self.bottom,text="Deposit Amount",font="arial 13 bold",width=20,command=deposit_amount)
        self.da.place(x=80, y=300)
        self.da_lbl=Label(self.bottom,text="--> Deposit amount from user account",bg="pink",font="arial 13 bold")
        self.da_lbl.place(x=320, y=302)

        #check account details
        self.cad=Button(self.bottom,text="Check Account Details",font="arial 13 bold",width=20,command=check_account_details)
        self.cad.place(x=80, y=400)
        self.cad_lbl=Label(self.bottom,text="--> Check account details",bg="pink",font="arial 13 bold")
        self.cad_lbl.place(x=320, y=402)

        #Update password
        self.Caa= Button(self.bottom, text=" Change password ", font="arial 13 bold", command=pwd_admin, width=20)
        self.Caa.place(x=80, y=500)
        self.caa_lbl = Label(self.bottom, text="--> Update User Access Password", bg="pink", font="arial 13 bold")
        self.caa_lbl.place(x=320, y=502)

        #logout
        self.log=Button(self.bottom,text="Logout",font="arial 13 bold",width=7,command=logout)
        self.log.place(x=1200,y=20)

root=Tk()
root.title("BANK MANAGEMENT SYSTEM")
app=application(root)
root.geometry("1366x768")
root.resizable(True,True)
root.mainloop()