import customtkinter as ctk
from tkcalendar import DateEntry
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import App_backed as bs
import App_LoginPanel as lo
import App_Home as h
import App_menu as am

class Details(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.background_image = Image.open("menu.png")
        self.background_image = self.background_image.resize((1300, 1000), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(1300, 1000))
        self.background_label = ctk.CTkLabel(self, image=self.background_photo, text="")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.name_label = ctk.CTkLabel(self, text="Name",width=90,font=("sans",20,'bold'),fg_color="white")
        self.age_label = ctk.CTkLabel(self, text="Age",width=90,font=("sans",20,'bold'),fg_color="white")
        self.gen = ctk.CTkLabel(self, text="Gender",width=90,font=("sans",20,'bold'),fg_color="white")
        self.dob_label = ctk.CTkLabel(self, text="DOB",width=90,font=("sans",20,'bold'),fg_color="white")
        self.email_label = ctk.CTkLabel(self, text="Email",width=90,font=("sans",20,'bold'),fg_color="white")
        self.ph_label = ctk.CTkLabel(self, text="Phone No.",width=90,font=("sans",20,'bold'),fg_color="white")
        self.add_label=ctk.CTkLabel(self,text="Address ",width=90,font=("sans",20,'bold'),fg_color="white")
        self.select_label = ctk.CTkLabel(self, text="Select your",width=90,font=("sans",20,'bold'),fg_color="white")

        #Entries
        self.ename = ctk.CTkEntry(self, width=200)
        self.eage = ctk.CTkLabel(self, text="", bg_color="white", width=200)
        self.eemail = ctk.CTkEntry(self, width=200)
        self.eph = ctk.CTkEntry(self, width=200)
        self.address=ctk.CTkEntry(self,width=200)
        self.choice = ctk.StringVar(value="")
        self.choose = ctk.CTkOptionMenu(self, bg_color="transparent", variable=self.choice, values=['Sweet', 'Crunchy', 'Spicy', 'Creamy', 'Cheesy', 'Fruity'], font=("sans",18,'bold'),width=200)
        self.edob = DateEntry(self, width=30, background='darkblue', foreground='white', borderwidth=2)
        self.edob.bind("<<DateEntrySelected>>", self.calculate_age)
        self.gender_var = ctk.StringVar(value=None)
        self.male_radio = ctk.CTkRadioButton(self, text="Male", variable=self.gender_var, value="male", hover_color="Green")
        self.female_radio = ctk.CTkRadioButton(self, text="Female", variable=self.gender_var, value="female", hover_color="Green")
        self.popup = ctk.CTkLabel(self, text="", text_color="red")
        self.back = ctk.CTkButton(self, text="Back", fg_color="black", command=self.backaction)
        self.save = ctk.CTkButton(self, text="Save", fg_color="Green", command=self.saveaction,font=("sans",18,'bold'))
        self.back_menu = ctk.CTkButton(self, text="Back", fg_color="black", command=self.backmenu_action,font=("sans",18,'bold'))
        self.updateB = ctk.CTkButton(self, text="Update", fg_color="Green", command=self.update,font=("sans",18,'bold'))

    def calculate_age(self, event):
        selected_date = self.edob.get_date()
        age = None
        if selected_date:
            selected_date_str = selected_date.strftime('%Y-%m-%d')
            dob = datetime.strptime(selected_date_str, '%Y-%m-%d')
            today = datetime.today()
            age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
            self.eage.configure(text=age)
            return int(age)

    def show(self,text):
        self.check=text
        self.pack(fill="both", expand=True, padx=33, pady=10)

        self.name_label.place(x=600, y=100)
        self.ename.place(x=710, y=100)
        
        self.gen.place(x=600, y=150)
        self.male_radio.place(x=710, y=150)
        self.female_radio.place(x=810, y=150)
        
        self.dob_label.place(x=600, y=200)
        self.edob.place(x=710, y=200)

        self.age_label.place(x=600, y=250)
        self.eage.place(x=710, y=250)
        
        self.email_label.place(x=600, y=300)
        self.eemail.place(x=710, y=300)
        
        self.ph_label.place(x=600, y=350)
        self.eph.place(x=710, y=350)

        self.add_label.place(x=600,y=400)
        self.address.place(x=710,y=400)
        
        self.select_label.place(x=600, y=450)
        self.choose.place(x=710, y=450)

        if text=="save":
            self.back.place(x=610,y=550)
            self.save.place(x=780,y=550)
        elif text=="update":
            self.back_menu.place(x=610,y=550)
            self.updateB.place(x=780,y=550)


    def getdata(self):
        uname = self.ename.get()
        gen = self.gender_var.get()
        dob = self.edob.get_date()
        age = self.calculate_age(self)
        email = self.eemail.get()
        phone = self.eph.get()
        add=self.address.get()
        ch = self.choice.get()
        if self.check=="save":
            store = bs.Code(self.master)
            what = store.user_details(uname, gen, dob, age, email, phone, ch,add)
            return what
        elif self.check=="update":
            store = bs.Code(self.master)
            what = store.editing(uname, gen, dob, age, email, phone, ch,add)
            return what

    def saveaction(self):
        
        if (len(self.ename.get())>18):
            self.popup.configure(text="*Please ensure that your name is no longer than 18 characters.")
            self.popup.place(x=600, y=500)
        elif self.eph.get() and len(self.eph.get()) !=10:            
            self.popup.configure(text="*Please enter valid mobile number")
            self.popup.place(x=660, y=500)
        else:
            check = self.getdata()
            if check == False:
                self.popup.configure(text="*Please fill all details")
                self.popup.place(x=670, y=500)
            elif check == 10:
                self.popup.configure(text="*Server Error")
                self.popup.place(x=690, y=500)
            else:
                print("Your details has saved")
                self.destroy()
                m=am.AppMenu(self.master)
                m.show()

    def getdata_2(self):
        uname = self.ename.get()
        gen = self.gender_var.get()
        dob = self.edob.get_date()
        age = self.calculate_age(self)
        email = self.eemail.get()
        phone = self.eph.get()
        add=self.address.get()
        ch = self.choice.get()
        store = bs.Code(self.master)
        what = store.editing(uname, gen, dob, age, email, phone, ch,add)
        return what
    
    def update(self):
        if (len(self.ename.get())>18):
            self.popup.configure(text="*Please ensure that your name is no longer than 18 characters.")
            self.popup.place(x=600, y=500)
        elif self.eph.get() and len(self.eph.get()) !=10:
                
            self.popup.configure(text="*Please enter valid mobile number")
            self.popup.place(x=670, y=500)
        else:
            check = self.getdata_2()
            if check == False:
                self.popup.configure(text="*Server Error")
                self.popup.place(x=710, y=500)
            else:
                print("Your deatils has updated")
                self.destroy()
                m=am.Profile(self.master)
                m.show()
            
    def backaction(self):
        with open('store.txt', 'r+') as f:
            uname = f.read()
        re = bs.Code(self.master)
        re.delsignup(uname)
        self.destroy()
        back = h.HomePanel(self.master)
        back.show()

    def backmenu_action(self):
        self.destroy()
        b=am.Profile(self.master)
        b.show()
