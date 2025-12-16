
from multiprocessing import connection
from tkinter import *
import sqlite3


con=sqlite3.connect("medical.db")
dat=con.cursor()


def emp_view():
    global root, log
    root = Tk()
    log.destroy()
    
    root.title("Employee Interface")
    
    Label(root, text="SARASWATI MEDICAL STORE COMPANY").grid(row=0, column=0, columnspan=3)
    Label(root, text='*' * 80).grid(row=1, column=0, columnspan=3)
    Label(root, text='-' * 80).grid(row=3, column=0, columnspan=3)

    Label(root, text="Stock Maintenance", bg='green', fg='white').grid(row=2, column=0)
    Button(root, text='New Customer', width=25, bg='green', fg='white').grid(row=4, column=0)
    Button(root, text='Add product to Stock', bg='green', fg='white', width=25).grid(row=5, column=0)
    Button(root, text='Delete product from Stock', bg='red', fg='white', width=25).grid(row=6, column=0)

    Label(root, text="Access Database", bg='blue', fg='white').grid(row=2, column=1)
    Button(root, text='Modify', width=15, bg='blue', fg='white').grid(row=4, column=1)
    Button(root, text='Search', width=15, bg='blue', fg='white').grid(row=5, column=1)
    Button(root, text='Expiry Check', bg='red', fg='white', width=15).grid(row=6, column=1)

    Label(root, text="Handle Cash Flows", bg='skyblue', fg='black').grid(row=2, column=2)
    Button(root, text="Check Today's Revenue", bg='skyblue', fg='black', width=20).grid(row=5,column=2)
    Button(root, text='Billing', width=20, bg='skyblue', fg='black').grid(row=4, column=2)
    Button(root, text='Logout', bg='red', fg='white', width=20,command=aux).grid(row=6, column=2)
    root.mainloop()
    
def aux():
    global log,root
    root.destroy()
    emp_view()
    

def login():
    global root,log,ver,val
    
    log = Tk()
    log.title("MAIN MENU")
    log.geometry('300x150')
    log.title('AUXILIARY COMPANY')
    
    Label(log, text='SARASWATI MEDICAL STORE COMPANY').grid(row=0, column=0, columnspan=5)
    Label(log, text="KHARGHAR BRANCH").grid(row=1, column=0, columnspan=5)
    
    Label(log, text='-------------------------------------------------------').grid(row=2, column=0, columnspan=5)
    
    Label(log, text='Username').grid(row=3, column=0)
    un = Entry(log, width=30).grid(row=3, column=1)
    
    Label(log, text='Password').grid(row=4, column=0)
    pwd = Entry(log, width=30).grid(row=4, column=1)
    
    Button(log, width=6, bg='blue', fg='white', text='Enter',command=emp_view).grid(row=5, column=0)
    Button(log, width=6, bg='red', fg='white', text='Close',command=quit).grid(row=5, column=1)
    
    log.mainloop()
    




def cust_signup():
    global root,log,ver,val
    val = Tk()
    val.title("SIGN UP")
    Label(val, bg='blue', fg='white', text="****CUSTOMER SIGN UP****").grid(row=0, column=0, columnspan=3)
    Label(val, text="-" * 60).grid(row=1, column=0, columnspan=3)
    Label(val, text="Name: ").grid(row=2, column=0)
    name_vc = Entry(val)
    name_vc.grid(row=2, column=1)
    Label(val, text="Address: ").grid(row=3, column=0)
    add_vc = Entry(val)
    add_vc.grid(row=3, column=1)
    Label(val, text="Aadhar number: ").grid(row=4, column=0)
    vc_id = Entry(val)
    vc_id.grid(row=4, column=1)
    Button(val, text='Submit', bg='blue', fg='white').grid(row=5, column=1)
    Button(val, text='Main Menu', bg='green', fg='white').grid(row=5, column=2)
    Label(val, text='-' * 60).grid(row=6, column=0, columnspan=3)
    val.mainloop()

'''start of main window and front end'''

def main_win():
    global root,log,ver,val
    ver = Tk()
    ver.title("LOGIN")
    
    Label(ver, text="SARASWATI MEDICAL STORE COMPANY").grid(row=0, column=0, columnspan=3)
    Label(ver, text="WELCOME! WE PROVIDE EVERY PHARMA FACILITY THAT YOU NEED").grid(row=2, column=0, columnspan=3)
    
    Label(ver, text='*' * 80).grid(row=1, column=0, columnspan=3)
    Label(ver, text='-' * 80).grid(row=3, column=0, columnspan=3)
    
    Label(ver, text="YOU CAN JOIN US AS CUSTOMER!").grid(row=4, column=0, columnspan=3)
    Label(ver, text=" ").grid(row=5, column=0)
    Button(ver, width=6, bg='blue', fg='white', text='Login',activebackground='light blue',command=login).grid(row=6, column=1,columnspan=3)
    Button(ver, width=6, bg='red', fg='white', text='Sign up',activebackground='pink',command=cust_signup).grid(row=6, column=0)
    
    Label(ver, text='-' * 80).grid(row=7, column=0, columnspan=3)
    
    Label(ver, text="FOR EMPLOYEE LOGIN",background='green').grid(row=8, column=0, columnspan=3)
    Label(ver, text=" ").grid(row=9, column=0)
    Button(ver, width=6, bg='light blue', fg='black', text='Login',command=login).grid(row=10, column=0,columnspan=3)
    ver.mainloop()
main_win()
