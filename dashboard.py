from tkinter import *
from customtkinter import *
from datetime import datetime
from database import getAllUsers
from PIL import ImageTk, Image
import matplotlib.pyplot as plt
import numpy as np
import sign


 
class dash():
    def __init__(self):
        self.cutom1 = ("Arial" , 13, "bold")
        self.root = Tk()
        self.root.title("Dashboard")
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        self.root.geometry(f"{self.width}x{self.height}")

        self.blue_frame = Frame(self.root , bg="#1ac1eb", width=self.width , height=50)
        self.blue_frame.place(x= 0 , y=0)

        self.sidebar()
        self.coloums()
        self.pie()

        self.logout = CTkButton(master= self.root , text="Logout" , fg_color="#1aeb47" , text_color="Black" , corner_radius= 0 
                                , hover_color="red" , border = 0)
        self.logout.place(x= 1100 , y = 10)
       


        # image code
        im = Image.open("9131529.png") 
        img_new= im.resize((100,100))
        img = ImageTk.PhotoImage(img_new)
        self.label_img = Label(self.root, bg="white" , image = img)
        self.label_img.place(x=80 , y=80)
        
        


        self.root.mainloop()

    def sidebar(self):
        self.frame_side = Frame(self.root , width=300 , height=self.height , bg= "white")
        self.frame_side.place(x=0 , y= 0)

            
        self.name_data = Label(self.frame_side , text="Manan Sood" , bg="white" , font=("Arial" , 13 , "bold"))
        self.name_data.place(x = 70 , y=200)


        # icons
        self.name_data = Button(self.frame_side , border=0 , text="Dashboard" , bg="white" , font=("Arial" , 13 , "bold"))
        self.name_data.place(x = 50 , y=300)
        self.name_data = Button(self.frame_side , border=0 , text="Manage" , bg="white" , font=("Arial" , 13 , "bold"))
        self.name_data.place(x = 50 , y=360)
        self.name_data = Button(self.frame_side , border=0 , text="Settings" , bg="white" , font=("Arial" , 13 , "bold"))
        self.name_data.place(x = 50 , y=420)
        self.name_data = Button(self.frame_side , border=0 , text="Exit" , bg="white" , font=("Arial" , 13 , "bold"))
        self.name_data.place(x = 50 , y=480)

    def coloums(self):
        self.blue_frame = Frame(self.root , bg="Blue", width=280 , height=180)
        self.blue_frame.place(x= 330 , y=420)

        self.blue_label = CTkLabel(master=self.blue_frame, text="Total people" , text_color="white" , text_font=self.cutom1)
        self.blue_label.place(x = 0 , y= 0)

        self.red_frame = Frame(self.root , bg="red", width=280 , height=180)
        self.red_frame.place(x= 630 , y=420)
        self.red_label = CTkLabel(master=self.red_frame , text="Total Days" , text_color="white" , text_font=self.cutom1)
        self.red_label.place(x=0 , y= 0)

        self.yellow_frame = Frame(self.root , bg="#ebcc34", width=280 , height=180)
        self.yellow_frame.place(x= 930 , y=420)
        self.yellow_label = CTkLabel(master=self.yellow_frame , text="Expenditure" , text_color="white" , text_font=self.cutom1)
        self.yellow_label.place(x = 0 , y= 0)

    def pie(self):
        res = getAllUsers()
        for i in res:
            print(i)
            
            
       


d1 = dash()