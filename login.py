from customtkinter import *
from tkinter import *
# from  database import register
import re
from tkinter import messagebox


class Login():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title("-Up")
        self.root.geometry("930x500")
        self.root.resizable(False, False)

        self.root.configure(bg="white")

        # image code 
        img = PhotoImage(file = "login.png")
        self.label = Label(self.root , bg="white" , image = img)
        self.label.place(x=50 , y=50)

        # welcome tage code
        self.Label1 = Label(self.root , text = "Welcome to PG Nest", bg='white' ,  font= ("consolas" , 20 , 'bold'))
        self.Label1.place(x=540 , y=26)

        # input codes 
        # Name entry
        self.label_name = Label(self.root, text= "Your  Name" ,bg="white" , font= ("Serif" , 9 ))
        self.label_name.place(x=520 , y= 100)
        self.Name_entry = Entry(self.root , border=2,   font= ("Serif" , 15 ))
        self.Name_entry.place(x= 520 , y= 130)
 
        # Email entry
        self.label_email = Label(self.root, text= "Your  Email" ,bg="white" , font= ("Serif" , 9 ))
        self.label_email.place(x=520 , y= 240)
       
        self.email_entry = Entry(self.root ,border=2, text = "Email" , font= ("Serif" , 15 ))
        self.email_entry.place(x= 520 , y= 270)

         # number entry
        self.label_number = Label(self.root, text= "Number" ,bg="white" , font= ("Serif" , 9 ))
        self.label_number.place(x=520 , y= 170)
        
        self.number_entry = Entry(self.root ,border=2, text = "number" , font= ("Serif" , 15 ))
        self.number_entry.place(x= 520 , y= 200)


        # password entry
        self.label_pass = Label(self.root, text= "Password" ,bg="white" , font= ("Serif" , 9 ))
        self.label_pass.place(x=520 , y= 310)
        self.pass_entry = Entry(self.root , border=2, text = "password" , font= ("Serif" , 15 ) , show= "*")
        self.pass_entry.place(x= 520 , y= 340)

       
        
        # button 
        self.button = CTkButton(master = self.root ,  text = "Continue" , bg = "blue" , corner_radius= 9 , command=self.getval)
        self.button.place(x= 520 , y= 390)

        # login 
        self.label_login = Label(self.root, text= "Already have an account ?" ,bg="white" , font= ("Serif" , 9 ) )
        self.label_login.place(x= 450 , y= 450)
        
        self.root.mainloop()

    def getval(self):
        self.password = self.pass_entry.get()
        self.naam = self.Name_entry.get()
        self.email = self.email_entry.get()
        # self.date = self.DOB_entry.get()
        self.no = self.number_entry.get()
        self.check()

    def check(self):
        pass_pattern = '^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W).{8,}$'
        mon_pattern = '[6-9]{1}\d{9}'
        # dob_pattern = '^\d+$'
        em_pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        flag = 0
        if(self.password or self.naam or self.email or self.no == ""):
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
       
        
        if flag >=3:
            self.data = (self.naam ,self.email, self.password)
            with open ("info.txt" , 'a') as f:
                f.write(str(self.data))
                f.write("\n")  

        # res = register(self.data)
        # if res:
        #     messagebox.showinfo("Database","User Registered Sucessfully")
        # else:
        #     messagebox.showerror("Error","Not Registered")


           

if __name__ == "__main__" :
    log = Login()


