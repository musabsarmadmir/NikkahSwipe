import ttkbootstrap as ttk
import random
import sys
import os
import pyinputplus as pyinp
import csv
import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
class GUi:
    def __init__(self) -> None:
        self.font=("Roboto",14)
        self.bg="#FFC0CB"
        self.entry_bg="#FAF9F6"
        self.flag=False
        self._h=[]
        self.files=os.listdir("wall")
        self.done=0
        self.counter=0
        self.d1=0
        self.showuser_n=[]
        self.showuser=[]
        self.selected_user=[]
        self.finaluser=[]  
        self.r=[]
        self.ui9=0
        self.r=[]
        self.win1=0
        self.t1=[]
        self.startingWindow()
    #USer Interface Login and Signup Gui awith code
    def Login_gui(self):
        self.window.destroy()
        self._n1=self.Window()
        self.entryemail_l=tk.Entry(self._n1,font=self.font,bg=self.entry_bg)
        self.entryemail_l.place(x=80,y=200)
        self.entrypassword_l=tk.Entry(self._n1,font=self.font,bg=self.entry_bg)
        self.entrypassword_l.place(x=80,y=250)
        self.no=tk.Button(self._n1,text="Login",font=self.font,bg=self.entry_bg,command=self.login)
        self.no.place(x=150,y=300)
        
    def Signup_gui(self):
        
        self.window.destroy()
        self._n1=self.Window()
        self.crete_Label("Name",self._n1)
        self.entryname_Name=tk.Entry(self._n1,font=self.font,bg=self.entry_bg)
        self.entryname_Name.pack(padx=10,pady=10)
        self.crete_Label("Phone",self._n1)
        self.entryname_phone=tk.Entry(self._n1,font=self.font,bg=self.entry_bg)
        self.entryname_phone.pack(padx=10,pady=10)
        self.crete_Label("Password",self._n1)
        self.entryname_pass=tk.Entry(self._n1,font=self.font,bg=self.entry_bg,show="*")
        self.entryname_pass.pack(padx=10,pady=10)
        
        self.s_Button("Submit", self.user_new_form, self._n1, 100, 490)
    
        
  
    def age(self):
        self.A_ge=self.entry_age.get()
        self.age_1=int(self.A_ge)
        if self.age_1 >= 18:
            self.Emailcheck_ui() 
        else:
            messagebox.showerror("Exiting", "You are under age")
            sys.exit()
    def adminlogin(self):
        self.window.destroy()
        self.mainwinddow()                  
    def age_verify(self):
        self.window.destroy()
        self._age = self.Window()
        
        self.com_Label("Enter AGE", self._age, 140, 140)
        self.entry_age = tk.Entry(self._age, font=self.font, bg=self.entry_bg)
        self.entry_age.place(x=70, y=190)
    
        self.s_Button("Submit", self.age, self._age, 145, 240)
        
    def user_new_form(self):
        ##signup form for new user
        self.user_data=[]  
        self.name=self.entryname_Name.get()
        
        self.phone=self.entryname_phone.get()
        
        self.password=self.entryname_pass.get()
        
        
        self.user_data+=[self.name,self.phone,self.password,self.A_ge,self.mail]
        #self.user_data[self.username]=self.name,self.__phone,self.__mail,"p",self.__pass,self.age
            #self.userpersonaldata[self.__mail]=self.name,self.__phone,self.__mail,self.age
        with open("Userdata.csv", "a",newline="") as csvfile:
            self.csv_writer=csv.writer(csvfile)
            self.csv_writer.writerow(self.user_data)
        self.hobbies_gui()
    def Emailcheck_ui(self):
        self.window.destroy()
        self._nmail=self.Window()
        self.crete_Label("Enter Your email", self._nmail)
        self.entryname_mail=tk.Entry(self._nmail,font=self.font,bg=self.entry_bg)
        self.entryname_mail.pack(padx=10,pady=10)
        self.Button('Submit', self.emailcheck, self._nmail) 
        
    def emailcheck(self):
        self.mail = str(self.entryname_mail.get())
        self.user_not = True
        with open('Usersmail.csv', 'r') as csvfile:
            csv_reader =list( csv.reader(csvfile))
            print(csv_reader)
            
            while self.user_not :
                
                for row in csv_reader:
                    if row[0] == self.mail:
                        if self.flag==False:
                            error = messagebox.showwarning(title="Error", message="User Already Exist", 
                                detail="Press yes to go to login  or no to exit?", type="yesno")
                            if error == "no":
                                print("Bye")
                                sys.exit()
                            elif error == "yes":
                                self.Login_gui()
                            self.flag=True
                        break
                    elif row[0]!=self.mail:                   
                        with open('Usersmail.csv',"a",newline="") as csvfile:
                            csv_reader = csv.writer(csvfile)
                            csv_reader.writerow([self.mail])
                        self.user_not=False
                        self.Signup_gui()
        
    def profile_makeing(self):
        
        self.user_profile_data=[]
        self.gender=self.entry_gender.get()
        self.city=self.entry_City.get()
               
        self.user_profile_data+=[self.city,[self._h],self.gender,self.name,self.mail]
        with open("User_personal_data.csv", "a",newline="") as csvfile:
                self.csv_writer=csv.writer(csvfile)
                self.csv_writer.writerow(self.user_profile_data)
        self.window.destroy()
        self.mainwinddow()
    def hobbies(self):
        
        self.hobby_1=str(self.entry_hobby_1.get())
        
        self.hobby_2=str(self.entry_hobby_2.get())
        
        self.hobby_3=str(self.entry_hobby_3.get())
           
        self._h+=[self.hobby_1]+[self.hobby_2]+[self.hobby_3]
        self.profile_makeing_gui()
    def profile_makeing_gui(self):
        self.window.destroy()
        self._nh1=self.Window()
        self.crete_Label("City",self._nh1)
        self.entry_City=tk.Entry(self._nh1,font=self.font,bg=self.entry_bg)
        self.entry_City.pack(padx=10,pady=10)
        self.crete_Label("Gender",self._nh1)
        self.entry_gender=tk.Entry(self._nh1,font=self.font,bg=self.entry_bg)
        self.entry_gender.pack(padx=10,pady=10)
        self.Button('Submit', self.profile_makeing, self._nh1)
       
    def hobbies_gui(self):
        self.window.destroy()
        self._nh2=self.Window()
        self.crete_Label("Hobby 1",self._nh2)
        self.entry_hobby_1=tk.Entry(self._nh2,font=self.font,bg=self.entry_bg)
        self.entry_hobby_1.pack(padx=10,pady=10)
        self.crete_Label("Hobby 2",self._nh2)
        self.entry_hobby_2=tk.Entry(self._nh2,font=self.font,bg=self.entry_bg)
        self.entry_hobby_2.pack(padx=10,pady=10)
        self.crete_Label("Hobby 3",self._nh2)
        self.entry_hobby_3=tk.Entry(self._nh2,font=self.font,bg=self.entry_bg)
        self.entry_hobby_3.pack(padx=10,pady=10)
        self.Button('Submit', self.hobbies, self._nh2)
        
    def Window(self):
        self.window=ttk.Window(themename="journal")
        self.window.title("Nikkah App")
        self.window.geometry("400x600")
        self.window.configure(bg=self.bg)
        self.label=tk.Label(self.window,text="Nikkah App",font=self.font,bg=self.bg)
        self.label.pack()      
    def s_win(self):
        self.window.destroy()
        self.w=self.Window()
        self.d_Button("Login", self.Login_gui, self.window, "l")
        self.d_Button("signup", self.age_verify, self.window, "s")
        
    def startingWindow(self):
        self.Window()
        self.crete_Label("Back Button under construction.",self.window)
        self.crete_Label("Choose Wisely",self.window)
        
        self.d_Button("Login", self.Login_gui, self.window, "l")
        self.d_Button("signup", self.age_verify, self.window, "s")
        self.window.mainloop() 
    def login(self):
        self.mail_user_input=str(self.entryemail_l.get())
        self.user_password_input=(self.entrypassword_l.get())
        if self.mail_user_input == "admin" and self.user_password_input == "admin":
            self.adminlogin()
        else:
            self.login_auth()        
    def login_auth(self):     
       with open('Userdata.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
    
        for row in csv_reader :
            if row[4] == self.mail_user_input and row[2] == self.user_password_input:
                print("User Login Sucess")
                self.window.destroy()
                self.mainwinddow()
                break
            else:
                if self.flag==False:
                    error = messagebox.showwarning(title="Error", message="User does not Exist", 
                        detail="Press yes Signup or no to retry?", type="yesno")
                    if error == "no":
                        self.Login_gui()
                    elif error == "yes":
                        self.age_verify()
                    self.flag=True
                    break                
    #Mainwindow
    def mainwinddow(self):
        if self.win1<1:
            self.win1+=1
            
            self.m_win=self.Window()
            tk.Label(self.m_win,text="""Hello From 
                Nikkah Swipe""",font=("roboto",20)).place(x=0,y=250)
            self.d_Button("Find Match", self.swipe, self.m_win,  "C")
            self.d_Button("Message", self.mess, self.m_win, "BL")
            self.d_Button("User", self.user_l, self.m_win, "BR")
            
        elif self.win1>=1:
            self.window.destroy()
            self.m_win=self.Window()
            tk.Label(self.m_win,text=""" Hello From 
                Nikkah Swipe""",font=("roboto",20)).place(x=0,y=250)
            self.d_Button("Find Match", self.swipe, self.m_win,  "C")
            self.d_Button("Message", self.mess, self.m_win, "BL")
            self.d_Button("User", self.user_l, self.m_win, "BR")
            self.win1+=1
        self.window.mainloop()
    ###Swiping    ad
    def swipe(self):
        self.image_arry=[]
        self.window.destroy()
        self.winswipe=self.Window()
        for self.file in self.files:
            img=Image.open(os.path.join("wall",self.file))
            resize=img.resize((200,200))
            photo = ImageTk.PhotoImage(resize)
            self.image_arry.append(photo)
        with open("randomdat.csv","r",encoding="latin-1") as f:
            read_csv=csv.reader(f)
            for row in read_csv:
                self.showuser_n.append(row[0]+row[1])
                self.showuser.append(row[4]+row[5]+row[6])
        self.img_label = tk.Label(self.winswipe, image=self.image_arry[self.counter],width=200, height=200)
        self.img_label.configure (image=self.image_arry[self.counter])  # keep a reference to the image
        self.img_label.place(x=100, y=150)
        self.name_label = tk.Label(self.winswipe, text=self.showuser_n[self.counter],width=15, height=2)
        self.name_label.place(x=150, y=360)
        self.detl_label = tk.Label(self.winswipe, text="Age And City",width=10, height=2)
        self.detl_label.place(x=150, y=390)
        self.detail_label = tk.Label(self.winswipe, text=self.showuser[self.counter],width=20, height=2)
        self.detail_label.place(x=150, y=430)
        self.d_Button("R.swipe", self.rightswipe, self.winswipe, "CR")
        self.d_Button("l.swipe", self.ime_counter, self.winswipe, "CL")
        self.d_Button("home", self.mainwinddow, self.winswipe, "C")
        self.d_Button("User", self.user_l, self.winswipe, "BR")
        self.d_Button("Mess", self.mess, self.winswipe, "BL")     
    def ime_counter(self):
        self.counter += 1
        self.img_label.config(image=self.image_arry[self.counter % len(self.image_arry)])
        self.name_label.config(text=self.showuser_n[self.counter % len(self.showuser_n)])
        self.detail_label.config(text=self.showuser[self.counter % len(self.showuser)])  
    def rightswipe(self):
        self.counter += 1
        self.selected_user.append(self.showuser_n[self.counter])
        
        
        self.img_label.config(image=self.image_arry[self.counter % len(self.image_arry)])
        self.name_label.config(text=self.showuser_n[self.counter % len(self.showuser_n)])
        self.detail_label.config(text=self.showuser[self.counter % len(self.showuser)])  
    def random_user(self):
        for x in range(len(self.selected_user)):
            self.finauser=random.choice(self.selected_user)
            with open("Selected.csv", "a",newline="",encoding='utf-8') as csvfile:
                self.csv_writer=csv.writer(csvfile)
                self.csv_writer.writerow([self.finauser])
    def u(self):
        self.random_user()
        with open('Selected.csv', 'r') as csvfile:
            csv_reader = list(csv.reader(csvfile))
            self.finaluser=list(csv_reader)
    ##User Button
    def user_l(self):
        
        self.uy = 100
        self.window.destroy()
        self._u1 = self.Window()
        self.d_Button("Home", self.mainwinddow, self._u1, "C")
        self.d_Button("Mess", self.mess, self._u1, "BL")
        with open ("Userdata.csv","r") as csvfile:
            csv_r = csv.reader(csvfile)
            
            for x in csv_r:
               
                
                    self.com_Label("Name ",self._u1,50,80)
                    self.user_Label(x[0],self._u1,190,80)
                    self.com_Label("Phone",self._u1,50,120)
                    self.user_Label(x[1],self._u1,190,120)
                    self.com_Label("Email",self._u1,50,160)
                    self.user_Label(x[4],self._u1,190,160)
                    self.com_Label("Age",self._u1,50,200)
                    self.user_Label(x[3],self._u1,190,200)
        with open("User_personal_data.csv","r") as csvfile:
            csv_r = csv.reader(csvfile)
            for x in csv_r:
            
                self.com_Label("Hobbies",self._u1,50,270)
                self.user_Label(x[1],self._u1,190,270)
                self.com_Label("City",self._u1,50,320)
                self.user_Label(x[0],self._u1,190,320)
                self.com_Label("Gender",self._u1,50,360)
                self.user_Label(x[2],self._u1,190,360)
                self.com_Label("""Currently , 
                                You Cannot Change Your Data.""",self._u1,0,400)
                    
    
                
    def mess(self):
        self.v=0
        self.u()
        self.window.destroy()
        self.mess_window=self.Window()
        mess=tk.Label(self.mess_window,text="User who have matched with you ",font=("roboto",14),bg=self.bg)
        mess.place(x=0,y=50)
        self.posx=100
        self.posy=160
        self.d_Button("Home", self.mainwinddow, self.mess_window, "C")
        self.d_Button("User", self.user_l, self.mess_window, "BR")
        self.d_Button("Mess", self.mess, self.mess_window, "BL")
        for x in self.finaluser[:12]:
            if self.v < 6:
                self.s_Button(x, self.send, self.mess_window, 30, self.posx)
                self.posx += 40
            else:
                self.s_Button(x, self.send, self.mess_window, 200, self.posy)
                self.posy += 40
            self.v += 1
            if self.v == 6:
                  # Replace with the initial value of self.posx
                self.posy = 160  # Replace with the initial value of self.posy
    def send_text(self):
        self.firsttex=120
        text = self.userentry.get()
        self.t1.append(text)
        for x in self.t1:
            self.user_Label(x, self.textwin_1, 350, self.firsttex)
            self.firsttex+=30

    def send(self):
        self.window.destroy()
        self.textwin_1 = self.Window()
        self.userentry = tk.Entry(self.textwin_1, font=self.font, bg=self.entry_bg)
        self.userentry.place(x=100, y=560)
        self.utton = tk.Button(text="send", command=self.send_text)  # remove placement parameter
        self.utton.place(x=330, y=555)
        self.d_Button("exit", self.mess, self.textwin_1, "BL")       
    ##main Buttons
    def Button(self,text,command,placement):
        self.b=tk.Button(placement,text=text,font=self.font,bg=self.entry_bg,command=command)
        self.b.pack()
    def d_Button(self,text,command,placement,b_place):
        self.b=tk.Button(placement,text=text,font=self.font,bg=self.entry_bg,command=command)
        
        if b_place == "C":
            self.b.pack(side=tk.BOTTOM, anchor=tk.S)
        elif b_place == "BL":
            self.b.place(x=10, y=560)
        elif b_place == "BR":
            self.b.place(x=330, y=560)
        elif b_place == "CL":
            self.b.pack(side=tk.LEFT, anchor=tk.E)
        elif b_place == "CR":
            self.b.pack(side=tk.RIGHT, anchor=tk.W)
        elif b_place == "l":
            self.b.place(x=140, y=250)
        elif b_place == "s":
            self.b.place(x=140, y=300)
    def s_Button(self,text,command,placement,x1,y1):
        self.b=tk.Button(placement,text=text,font=self.font,bg=self.entry_bg,command=command)
        self.b.place(x=x1,y=y1)
    def crete_Label(self,text,placement):
        self.label_1=tk.Label(placement,text=text,font=self.font,bg=self.entry_bg)
        self.label_1.pack(padx=10,pady=10)
    def user_Label(self,text,placement,x,y):
        self.user_1=tk.Label(placement,text=text,font=self.font,bg="cyan")
        self.user_1.place(x=x,y=y) 
    def com_Label(self,text,placement,x,y):
        self.com_1=tk.Label(placement,text=text,font=self.font,bg="white")
        self.com_1.place(x=x,y=y)         
use=GUi()
