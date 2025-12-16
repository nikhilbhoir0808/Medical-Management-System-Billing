
from re import L
from  tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
import tkinter as tk
import mysql.connector
from tkinter import messagebox
import random
import os

class BillingSystem:
        def __init__(self,root):
                self.root=root
                self.root.title("Pharmacy Managment System")
                self.root.geometry("1550x800+0+0")
#VAriables******************************************
                self.cname=StringVar()
                self.phone=StringVar()
                self.email=StringVar()
                self.billno=StringVar()
                self.price=IntVar()
                self.qty=IntVar()  
                self.MedicineName=StringVar()     
                self.total=IntVar()    
                x=random.randint(1000,9999)
                self.billno.set(str(x))

                global l
                l=[]
#***********************************************************              
                lbltitle=Label(self.root,text="MEDICAL MANAGEMENT SYSTEM",bd=15,relief=RIDGE,
                        bg='white',fg="darkblue",font=("times new roman",50,"bold"),padx=2,pady=4)
                lbltitle.pack(side=TOP,fill=X)

                img1=Image.open("D:\Project\logo.jpg")
                img1=img1.resize((80,80),Image.ANTIALIAS)
                self.photoimg1=ImageTk.PhotoImage(img1)
                b1=Button(self.root,image=self.photoimg1,borderwidth=0)
                b1.place(x=60,y=15)

#********************************Main Frame*************************************
                DataFrame=Frame(self.root,bd=15,relief=RIDGE,padx=20)
                DataFrame.place(x=0,y=120,width=1530,height=670)         

#**********************************LEft Farme ************************************
                DataFrameLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Medicine Information",
                                          fg="Darkblue",font=("Arial",12,"bold"))
                DataFrameLeft.place(x=0,y=5,width=450,height=150)

                iblCust=Label(DataFrameLeft,text=("Customer Name:"),font=("arial",12,"bold"))
                iblCust.grid(row=0,column=0,sticky=W,padx=5,pady=2)       
                iblCust=ttk.Entry(DataFrameLeft,textvariable=self.cname,width=24,font=("arial",13,"bold"))
                iblCust.grid(row=0,column=1,sticky=W,padx=5,pady=2)

                iblPhone=Label(DataFrameLeft,text=("Phone:"),font=("arial",12,"bold"),bd=6)
                iblPhone.grid(row=1,column=0,sticky=W,padx=5,pady=2)       
                iblPhone=ttk.Entry(DataFrameLeft,textvariable=self.phone,width=24,font=("arial",13,"bold"))
                iblPhone.grid(row=1,column=1,sticky=W,padx=5,pady=2)

                iblMail=Label(DataFrameLeft,text=("Email:"),font=("arial",12,"bold"),bd=6)
                iblMail.grid(row=2,column=0,sticky=W,padx=5,pady=2)       
                iblMail=ttk.Entry(DataFrameLeft,textvariable=self.email,width=24,font=("arial",13,"bold"))
                iblMail.grid(row=2,column=1,sticky=W,padx=5,pady=2)



#*****************************Middle Frame***************************************
                DataFrameMiddle=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,text="Product Details",
                                        fg="Darkblue",font=("Arial",12,"bold"))
                DataFrameMiddle.place(x=457,y=5,width=650,height=150)

                iblCust=Label(DataFrameMiddle,text=("Bill No:"),font=("arial",12,"bold"))
                iblCust.grid(row=0,column=0,sticky=W,padx=5,pady=2)       
                iblCust=ttk.Entry(DataFrameMiddle,textvariable=self.billno,width=22,font=("arial",13,"bold"))
                iblCust.grid(row=0,column=1,sticky=W,padx=5,pady=2)
                
                iblMedname=Label(DataFrameMiddle,text=("Medicine Name :"),font=("arial",12,"bold"),padx=2,pady=6)
                iblMedname.grid(row=1,column=0,sticky=W)
                
                conn=mysql.connector.connect(host="localhost",username="root",password="Omsawant@123",database="medical")
                my_cursor=conn.cursor()
                my_cursor.execute("select MedName from med")
                med=my_cursor.fetchall()

                search_comboMedname=ttk.Combobox(DataFrameMiddle,textvariable=self.MedicineName,width=20,font=("arial",13,"bold"),state="readonly")
                search_comboMedname["values"]=med
                search_comboMedname.current(0)
                search_comboMedname.grid(row=1,column=1)

                iblTb=Label(DataFrameMiddle,text=("Tablets Price:"),font=("arial",12,"bold"),padx=2,pady=6)
                iblTb.grid(row=2,column=0,sticky=W)
                iblTb=Entry(DataFrameMiddle,textvariable=self.price,bd=2,relief=RIDGE,width=22,font=("arial",13,"bold"))
                iblTb.grid(row=2,column=1)


                iblTb=Label(DataFrameMiddle,text=("Quantity:"),font=("arial",12,"bold"),padx=4,pady=6)
                iblTb.grid(row=0,column=3,sticky=W)
                iblTb=Entry(DataFrameMiddle,textvariable=self.qty,bd=2,relief=RIDGE,width=19,font=("arial",13,"bold"))
                iblTb.grid(row=0,column=4)

#*******************************Middleframe1************************************************

                DataFrameMiddle1=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=20,
                                        fg="Darkblue",font=("Arial",12,"bold"))
                DataFrameMiddle1.place(x=0,y=170,width=1110,height=400)
               
                
                sc_y=ttk.Scrollbar(DataFrameMiddle1,orient=VERTICAL)
                self.textarea=Text(DataFrameMiddle1,yscrollcommand=sc_y.set,bg="white",font=("arial",13,"bold"),width=65,fg="blue")
                sc_y.pack(side=RIGHT,fill=Y)
                sc_y.config(command=self.textarea.yview)
                self.textarea.pack(fill=Y,expand=1)          

#*******************************BottomButtons**********************************************
                 
                ButtonFrame1=Frame(self.root,bd=15,relief=RIDGE,padx=20)
                ButtonFrame1.place(x=25,y=710,width=1122,height=65)

                btnAddMed=Button(ButtonFrame1,command=self.additem,text=("ADD TO CART"),font=("Arial",12,"bold"),width=12,bg="lime",fg="white",pady=4.3,padx=60)
                btnAddMed.grid(row=0,column=0)

                btnUpdateMed=Button(ButtonFrame1,command=self.gen_bill,text=("GENERATE BILL"),font=("Arial",12,"bold"),width=12,bg="darkred",fg="white",pady=4.3,padx=60)
                btnUpdateMed.grid(row=0,column=1)
 
                btnDeleteMed=Button(ButtonFrame1,command=self.Save,text=("SAVE"),font=("Arial",12,"bold"),width=12,bg="purple",fg="white",pady=4.3,padx=60)
                btnDeleteMed.grid(row=0,column=2)

                btnClearMed=Button(ButtonFrame1,command=self.Exit,text=("EXIT"),font=("Arial",12,"bold"),width=12,bg="orange",fg="white",pady=4.3,padx=60)
                btnClearMed.grid(row=0,column=3)
                self.welcome()

                self.l=[]
                

        def welcome(self):
                self.textarea.delete(1.0,END)
                self.textarea.insert(END,"\t\t\tWelcome to Medical Store")
                self.textarea.insert(END,f"\nBill NO: {self.billno.get()}")
                self.textarea.insert(END,f"\nCustomer Name: {self.cname.get()}")
                self.textarea.insert(END,f"\nPhone Number: {self.phone.get()}")
                self.textarea.insert(END,f"\nEmail: {self.email.get()}")
                self.textarea.insert(END,f"\n==========================================================")
                self.textarea.insert(END,f"\nMedicine Name\t\t\t\tQty\t\t\tPrice")
                self.textarea.insert(END,f"\n==========================================================")

        def additem(self):
                self.n=self.price.get()
                self.m=self.qty.get()*self.n
                l.append(self.m)
                
                if self.MedicineName==" ":
                        messagebox.showerror("Error!","Please select the medicine name")
                else:
                        self.textarea.insert(END,f"\n{self.MedicineName.get()}\t\t\t\t{self.qty.get()}\t\t\t{self.m}")
                        

        def gen_bill(self):
                if self.MedicineName==" ":
                        messagebox.showerror("Error!","Please select the medicine name")
                else:
                        text=self.textarea.get(9.0,(9.0+float(len(l))))
                        self.welcome()
                        self.textarea.insert(END,text)
                        self.textarea.insert(END,f"\nTotal Amount:\t{sum(l)}")

        def Save(self):
                op=messagebox.askyesno("Save Bill","Do you want to save bill")
                if op>0:
                        self.bill_data=self.textarea.get(1.0,END)
                        f1=open("Bills/"+str(self.billno.get())+"txt",'w')
                        f1.write(self.bill_data)
                        op=messagebox.askyesno("Save Bill","Bill has been Save ")
                        f1.close()

        def Exit(self):
                op=messagebox.askyesno("Save Bill","Do you want to Exit")
                if op>0:
                        self.root.destroy()


if __name__ =="__main__":  
    root=Tk()
    obj=BillingSystem(root)
    root.mainloop()
