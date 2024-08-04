from tkinter import *
from tkinter import messagebox
from database import register
import re

class Register:
    def __init__(self):
        self.root = Tk()

        self.root.geometry('500x400')
        self.root.title("Registration form")
        # self.root.resizable(False , False)

        self.frame1 = Frame(self.root,bg= '#328ba8',height=600 , width=600)
        self.frame1.place(x=0 , y= 0)

        self.title = Label(self.frame1 , text="Registeration form",bg = '#328ba8', font=('arial' , 25 , 'bold' ) )
        self.title.place(x=30 , y= 10)

        self.name = Label(self.frame1 , text="Name",bg = '#328ba8', font=('arial' , 10 , 'bold' ) )
        self.name.place(x= 30 , y= 100)

        self.name_entry = Entry(self.frame1 , text="Name", font=('arial' , 10 , 'bold' ) , width = '30')
        self.name_entry.place(x= 120 , y= 100)
        # first - name ends here 

        # Email  
        self.email = Label(self.frame1 , text="Email",bg = '#328ba8', font=('arial' , 10 , 'bold' ) )
        self.email.place(x= 30 , y= 140)

        self.email_entry = Entry(self.frame1 , text="Email", font=('arial' , 10 , 'bold' ) , width = '30')
        self.email_entry.place(x= 120 , y= 140)
        # email ends here
        # mobile number starts
        self.number = Label(self.frame1 , text="Mobile no.",bg = '#328ba8', font=('arial' , 10 , 'bold' ) )
        self.number.place(x= 30 , y= 180)

        self.number_entry = Entry(self.frame1 , text="Number", font=('arial' , 10 , 'bold' ) , width = '30' )
        self.number_entry.place(x= 120 , y= 180)
        # MObile no. ends

        # Password
        self.pwd = Label(self.frame1 , text="Password",bg = '#328ba8', font=('arial' , 10 , 'bold' ) )
        self.pwd.place(x= 30 , y= 260)

        self.pwd_entry = Entry(self.frame1 , text="Password", font=('arial' , 10 , 'bold' ) , width = '30' , show="*" )
        self.pwd_entry.place(x= 120 , y= 260)

        # DOB

        self.DOB = Label(self.frame1 , text="DOB",bg = '#328ba8', font=('arial' , 10 , 'bold' ) )
        self.DOB.place(x= 30 , y= 220)

        self.DOB_entry = Entry(self.frame1 , text="DOB", font=('arial' , 10 , 'bold' ) , width = '30')
        self.DOB_entry.place(x= 120 , y= 220)

        # submit button 
        self.btn= Button(self.frame1,text="Submit", font=('arial',15,'normal') , command=self.getVal)
        self.btn.place(x=170, y=300)




        self.root.mainloop()

    def getVal(self):
        # print("Hi")
        self.password = self.pwd_entry.get()
        self.naam = self.name_entry.get()
        self.email = self.email_entry.get()
        self.date = self.DOB_entry.get()
        self.no = self.number_entry.get()
        self.check()

    def check(self):
        pass_pattern = '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,}$'
        mon_pattern = '[6-9]{1}\d{9}'
        dob_pattern = '^\d+$'
        em_pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        flag = 0
        if(self.password or self.naam or self.email or self.date or self.no == ""):
            messagebox.showwarning("Warning",'All field must be filled properly')
            return(False)        
        em = re.match(em_pattern , self.email)
        if em:
            flag += 1
        else:
            messagebox.showwarning("email Incorrect" , "Enter valid Email")
        
        num = re.match(mon_pattern , self.no)
        if num and len(self.no) <= 10:
            flag += 1
        else:
            messagebox.showwarning("Incorrect Number" , "Enter valid Number")
        password = re.match(pass_pattern, self.password)
        if password:
           flag += 1
        else:
            messagebox.showwarning("password Incorrect" , "Enter valid Password")
        dob1 = re.match(dob_pattern, self.date)
        if dob1:
            flag += 1
        else:
            messagebox.showwarning( "Incorrect DOB" , "Enter valid Date of birth")
        
        if flag >=4:
            self.data = (self.naam ,self.email, self.password)
            with open ("info.txt" , 'a') as f:
                f.write(str(self.data))
                f.write("\n")  

        res = register(self.data)
        if res:
            messagebox.showinfo("Database","User Registered Sucessfully")
        else:
            messagebox.showerror("Error","Not Registered")


    
if __name__ == "__main__":
    r1 = Register()

