from tkinter import *
from PIL import ImageTk,Image
import mysql.connector as S
from tkinter import messagebox
db=S.connect(host="localhost",user="root",password="maango")
print(db)
c=db.cursor()
c.execute("use FP")
db.commit()
root=Tk()

root.title("Financial Profile")
root.iconbitmap("")
root.configure(bg="#2874f0")
root.eval('tk::PlaceWindow . center')

def Dispallow():
        top1=Toplevel()
        top1.title("Receival Display")
        top1.configure(bg="#2874f0")
        label1=Label(top1,text="Enter RId : ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        label1.grid(row=0,column=0)
        e1=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        e1.grid(row=0,column=1)
      
        def submit():
                b=e1.get()
                
                c.execute("select * from allowance where RId= %s",(b,))
                a=c.fetchone()
                lis=[1]
                
                for i in a:
                        lis.append(i)
                        
                label1=Label(top1,text="Sender :  "+lis[1],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label1.grid(row=2,column=0,columnspan=2)
                label2=Label(top1,text="Date of Receival :  "+lis[2],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label2.grid(row=3,column=0,columnspan=2)
                label3=Label(top1,text="Reason for Sending:  "+lis[3],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label3.grid(row=4,column=0,columnspan=2)
                label4=Label(top1,text="Remarks :  "+lis[4],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label4.grid(row=5,column=0,columnspan=2)
                label5=Label(top1,text="Received Amount :  "+lis[5],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label5.grid(row=6,column=0,columnspan=2)
        submit=Button(top1,text="Display the Receival ",padx=25,pady=15,borderwidth=5,command=submit,bg="#2874f0",fg="white")
        submit.grid(row=1,column=0,columnspan=5)
       
                
def Delallow():
        top1=Toplevel()
        top1.title("Receival Deletion")
        top1.configure(bg="#2874f0")
        label1=Label(top1,text="Enter RId : ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        label1.grid(row=0,column=0)
        e1=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        e1.grid(row=0,column=1)
        def submit():
                   b=e1.get()
                   c.execute("delete from allowance where RId=%s",(b,))
                   db.commit()
                   messagebox.showinfo("Status","Data deleted successfully")
                   top1.destroy()
        submit=Button(top1,text="Delete",padx=25,pady=15,borderwidth=5,command=submit,bg="#2874f0",fg="white")
        submit.grid(row=1,column=0,columnspan=5)
      
        
def Addallow():
        top1=Toplevel()
        top1.title("Receival Filing")
        top1.configure(bg="#2874f0")
        label1=Label(top1,text="            Sender             ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e3=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label1.grid(row=0,column=0)
        e3.grid(row=0,column=1)
        label5=Label(top1,text="   Received Amount            ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e7=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label5.grid(row=1,column=0)
        e7.grid(row=1,column=1)
        label6=Label(top1,text="   Receival-Id             ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e8=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label6.grid(row=5,column=0)
        e8.grid(row=5,column=1)
        label2=Label(top1,text="  Date of receival      ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e4=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label2.grid(row=2,column=0)
        e4.grid(row=2,column=1)
        label3=Label(top1,text="Reason for sending ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e5=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label3.grid(row=3,column=0)
        e5.grid(row=3,column=1)
        label4=Label(top1,text="          Remarks            ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e6=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label4.grid(row=4,column=0)
        e6.grid(row=4,column=1)
        
        
        def submit():
                
                 s3=e3.get()
                 s4=e4.get()
                 s5=e5.get()
                 s6=e6.get()
                 s7=e7.get()
                 s8=e8.get()
          
                 lis=[s3,s4,s5,s6,s7,s8]
                 c.execute(" Insert into allowance(sender,DoR,RfS,Remarks,SA,RId) values (%s,%s,%s,%s,%s,%s)" , lis)
                 db.commit()
                 messagebox.showinfo("Status","Data entered successfully")
                 top1.destroy()

        
        submit=Button(top1,text="Submit",padx=25,pady=15,borderwidth=8,command=submit,bg="#2874f0",fg="white")
        submit.grid(row=6,column=0,columnspan=3)
     
       
def Addtrans():
        top1=Toplevel()
        top1.title("Transaction Filing")
        top1.configure(bg="#2874f0")
        label1=Label(top1,text="            Transacted Amount :              ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e1=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label1.grid(row=0,column=0)
        e1.grid(row=0,column=1)
        label2=Label(top1,text="             Spenditure details :                ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e2=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label2.grid(row=1,column=0)
        e2.grid(row=1,column=1)
        label3=Label(top1,text="              Transaction date   :                ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e3=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label3.grid(row=2,column=0)
        e3.grid(row=2,column=1)
        label4=Label(top1,text="              Balance remaining :              ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e4=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label4.grid(row=3,column=0)
        e4.grid(row=3,column=1)
        label5=Label(top1,text="               Transaction Id :                       ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e5=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label5.grid(row=4,column=0)
        e5.grid(row=4,column=1)
     
        
        
        def submit():
                
                 s1=e1.get()
                 s2=e2.get()
                 s3=e3.get()
                 s4=e4.get()
                 s5=e5.get()
          
               
                 c.execute("insert into transactions(TA,SpendF,DoS,LB,TId) values (%s,%s,%s,%s,%s)" , (s1,s2,s3,s4,s5))
                 db.commit()
                 messagebox.showinfo("Status","Data entered successfully")
                 top1.destroy()

        
        submit=Button(top1,text="Submit",padx=25,pady=15,borderwidth=8,command=submit,bg="#2874f0",fg="white")
        submit.grid(row=5,column=0,columnspan=3)
def Deltrans():
        top1=Toplevel()
        top1.title("Transaction Deletion")
        top1.configure(bg="#2874f0")
        label1=Label(top1,text="Enter TId : ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        label1.grid(row=0,column=0)
        e1=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        e1.grid(row=0,column=1)
        def submit():
                   b=e1.get()
                   c.execute("delete from transactions where TId=%s",(b,))
                   db.commit()
                   messagebox.showinfo("Status","Data deleted successfully")
                   top1.destroy()
        submit=Button(top1,text="Delete",padx=25,pady=15,borderwidth=8,command=submit,bg="#2874f0",fg="white")
        submit.grid(row=1,column=0,columnspan=5)
def Disptrans():
        top1=Toplevel()
        top1.title("Transaction Display")
        top1.configure(bg="#2874f0")
        label1=Label(top1,text="Enter TId : ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        label1.grid(row=0,column=0)
        e1=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        e1.grid(row=0,column=1)
      
        def submit():
                b=e1.get()
                
                c.execute("select * from transactions where TId= %s",(b,))
                a=c.fetchone()
                lis=[1]
                
                for i in a:
                        lis.append(i)
                        
                label1=Label(top1,text="Transacted Amount :  "+lis[1],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label1.grid(row=2,column=0,columnspan=2)
                label2=Label(top1,text="Transaction Details :  "+lis[2],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label2.grid(row=3,column=0,columnspan=2)
                label3=Label(top1,text="Date of Transaction :  "+lis[3],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label3.grid(row=4,column=0,columnspan=2)
                label4=Label(top1,text="Balance Remaining :  "+lis[4],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label4.grid(row=5,column=0,columnspan=2)

        submit=Button(top1,text="Display the Transaction ",padx=25,pady=15,borderwidth=8,command=submit,bg="#2874f0",fg="white")
        submit.grid(row=1,column=0,columnspan=5)
def AddSav():
        top1=Toplevel()
        top1.title("Savings Filing")
        top1.configure(bg="#2874f0")
        label1=Label(top1,text="            Saving start-date  :              ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e1=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label1.grid(row=0,column=0)
        e1.grid(row=0,column=1)
        label2=Label(top1,text="             Saving starting amount :                ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e2=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label2.grid(row=1,column=0)
        e2.grid(row=1,column=1)
        label3=Label(top1,text="              Last addition date   :                ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e3=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label3.grid(row=2,column=0)
        e3.grid(row=2,column=1)
        label4=Label(top1,text="              Last added amount :              ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e4=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label4.grid(row=3,column=0)
        e4.grid(row=3,column=1)
        label5=Label(top1,text="               Total at present :                       ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e5=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label5.grid(row=4,column=0)
        e5.grid(row=4,column=1)
        label6=Label(top1,text="               Enter  SId :                       ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        e6=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        label6.grid(row=5,column=0)
        e6.grid(row=5,column=1)
     
     
        
        
        def submit():
                
                 s1=e1.get()
                 s2=e2.get()
                 s3=e3.get()
                 s4=e4.get()
                 s5=e5.get()
                 s6=e6.get()
          
               
                 c.execute("insert into savings(startdate,startamt,lastadddate, lastaddamt,totals,SId) values (%s,%s,%s,%s,%s,%s)" , (s1,s2,s3,s4,s5,s6))
                 db.commit()
                 messagebox.showinfo("Status","Data entered successfully")
                 top1.destroy()

        
        submit=Button(top1,text="Submit",padx=25,pady=15,borderwidth=8,command=submit,bg="#2874f0",fg="white")
        submit.grid(row=6,column=0,columnspan=3)
def Delsav():
        top1=Toplevel()
        top1.title("Savings Deletion")
        top1.configure(bg="#2874f0")
        label1=Label(top1,text="Enter SId : ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        label1.grid(row=0,column=0)
        e1=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        e1.grid(row=0,column=1)
        def submit():
                   b=e1.get()
                   c.execute("delete from savings where SId=%s",(b,))
                   db.commit()
                   messagebox.showinfo("Status","Data deleted successfully")
                   top1.destroy()
        submit=Button(top1,text="Delete",padx=25,pady=15,borderwidth=8,command=submit,bg="#2874f0",fg="white")
        submit.grid(row=1,column=0,columnspan=5)
def Dispsav():
        top1=Toplevel()
        top1.title("Savings Display")
        top1.configure(bg="#2874f0")
        label1=Label(top1,text="Enter SId : ",padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
        label1.grid(row=0,column=0)
        e1=Entry(top1,width=35,borderwidth=5,bg="#2874f0",fg="white")
        e1.grid(row=0,column=1)
      
        def submit():
                b=e1.get()
                
                c.execute("select * from savings where SId= %s",(b,))
                a=c.fetchone()
                lis=[1]
                
                for i in a:
                        lis.append(i)
                        
                label1=Label(top1,text="Start of savings :  "+lis[1],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label1.grid(row=2,column=0,columnspan=2)
                label2=Label(top1,text="Starting amount :  "+lis[2],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label2.grid(row=3,column=0,columnspan=2)
                label3=Label(top1,text="Last addition date :  "+lis[3],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label3.grid(row=4,column=0,columnspan=2)
                label4=Label(top1,text="Last added amount  :  "+lis[4],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label4.grid(row=5,column=0,columnspan=2)
                label5=Label(top1,text="Total savings at present  :  "+lis[5],padx=20,pady=10,borderwidth=5,bg="#2874f0",fg="white")
                label5.grid(row=6,column=0,columnspan=2)


        submit=Button(top1,text="Display the Saving",padx=25,pady=15,borderwidth=8,command=submit,bg="#2874f0",fg="white")
        submit.grid(row=1,column=0,columnspan=5)
def Savings():
        top=Toplevel()
    
        top.title("Savings")
        top.configure(bg="#2874f0")
        b6=Button(top,text="    Add a Saving  ",padx=10,pady=8,borderwidth=8,command=AddSav,bg="#2874f0",fg="white")
        b6.grid(row=0,column=0)
        b7=Button(top,text="Display a Saving",padx=10,pady=8,borderwidth=8,command=Dispsav,bg="#2874f0",fg="white")
        b7.grid(row=1,column=0)
        b8=Button(top,text="  Delete a Saving",padx=10,pady=8,borderwidth=8,command=Delsav,bg="#2874f0",fg="white")
        b8.grid(row=2,column=0)
        
def Transactions():
        top=Toplevel()
    
        top.title("Transactions")
        top.configure(bg="#2874f0")
        b6=Button(top,text="    Add a Transaction  ",padx=10,pady=8,borderwidth=8,command=Addtrans,bg="#2874f0",fg="white")
        b6.grid(row=0,column=0)
        b7=Button(top,text="Display a Transaction",padx=10,pady=8,borderwidth=8,command=Disptrans,bg="#2874f0",fg="white")
        b7.grid(row=1,column=0)
        b8=Button(top,text="  Delete a Transaction",padx=10,pady=8,borderwidth=8,command=Deltrans,bg="#2874f0",fg="white")
        b8.grid(row=2,column=0)
        
def Allowance() :
        top=Toplevel()
    
        top.title("Allowances")
        top.configure(bg="#2874f0")
        b6=Button(top,text="    Add a Receival   ",padx=10,pady=8,borderwidth=8,command=Addallow,bg="#2874f0",fg="white")
        b6.grid(row=0,column=0)
        b7=Button(top,text="Display a Receival",padx=10,pady=8,borderwidth=8,command=Dispallow,bg="#2874f0",fg="white")
        b7.grid(row=1,column=0)
        b8=Button(top,text="  Delete a Receival ",padx=10,pady=8,borderwidth=8,command=Delallow,bg="#2874f0",fg="white")
        b8.grid(row=2,column=0)

        
def main():
        
        
        b2=Button(text="Allowances   ",padx=25,pady=10,command=Allowance,bg="#2874f0",fg="white",borderwidth=8)
        b3=Button(text="Transactions",padx=25,pady=10,command=Transactions,bg="#2874f0",fg="white",borderwidth=8)
        b4=Button(text="     Savings    ",padx=25,pady=10,command=Savings,bg="#2874f0",fg="white",borderwidth=8)
        b5=Button(text="         Exit         ",padx=25,pady=10,bg="#2874f0",fg="white",borderwidth=8)
        b2.grid(row=0,column=0)
        b3.grid(row=0,column=1)
        b4.grid(row=0,column=2)
        b5.grid(row=0,column=3)
        
        
def Confirmation():
        s1=e1.get()
        s2=e2.get()
        a=0
        if (s1=="Semicile17" and s2== "Rohit7081205"):
                a=1
                root.destroy()
                main()
                
        else:
                a=0
                messagebox.showwarning("Warning","Wrong Username or Password")
                e2.delete(0,END)
                e1.delete(0,END)

e1=Entry(width=30,borderwidth=5,bg="#2874f0",fg="white",show="*")
e2=Entry(width=30,borderwidth=5,show="*",bg="#2874f0",fg="white")
l1=Label(text="Username : ",bg="#2874f0",fg="white")
l2=Label(text="Password : ",bg="#2874f0",fg="white")

b1=Button(root,text="Enter",padx=10,pady=5,borderwidth=3,bg="#2874f0",fg="white",command=Confirmation)
b1.grid(row=2,column=0,columnspan=3)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)











root.mainloop()

      










