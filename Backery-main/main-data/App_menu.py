import customtkinter as ctk
from PIL import Image
from tkinter import messagebox
import App_backed as bs
import App_excelserver as ca
import App_Home as h
import App_food_menu as fm
import App_FillDetails as fd

class AppMenu(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        
        self.background_image = Image.open("menu.png")
        self.background_image = self.background_image.resize((1500, 1000), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(1500, 1000))
        self.background_label = ctk.CTkLabel(self, image=self.background_photo, text="")
        

        image_path = "profile.png"
        image = Image.open(image_path)
        image = image.resize((100, 100), Image.Resampling.LANCZOS)  
        self.image_ctk = ctk.CTkImage(light_image=image, size=(100, 100))
        self.profile = ctk.CTkButton(self, image=self.image_ctk, text="", command=self.action, hover_color="green", bg_color="lightsteelblue2", fg_color="lightsteelblue2", width=20, height=20, corner_radius=600,)
        self.profile_label=ctk.CTkLabel(self,text="Your Account",width=124,fg_color="lightsteelblue2",text_color="black",font=('sans',15,'bold'),)
        self.menu = ctk.CTkButton(self, text="Food Menu", command=self.menuaction,font=("sans",30,'bold'),width=200,text_color="black",hover_color="green")
        self.oder = ctk.CTkButton(self, text="Your Order", command=self.oderaction,font=("sans",30,'bold'),width=200,text_color="black",hover_color="green")
        self.trackOrder = ctk.CTkButton(self, text="About Order", command=self.trackOrderaction,font=("sans",30,'bold'),width=200,text_color="black",hover_color="green")
        self.logout = ctk.CTkButton(self, text="Logout", command=self.logoutaction,font=("sans",30,'bold'),width=200,text_color="black",hover_color="green")
        self.back = ctk.CTkButton(self, text="Back", command=self.backaction,font=("sans",30,'bold'),width=200,text_color="black",hover_color="green")

    def show(self):
        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.background_label.place(x=0, y=0,)
        self.profile.place(relx=0.994, rely=0.02, anchor="ne")
        self.profile_label.place(relx=0.994, rely=0.16, anchor="ne")
        self.menu.place(relx=0.6, rely=0.23, anchor="center")
        self.oder.place(relx=0.6, rely=0.33, anchor="center")
        self.trackOrder.place(relx=0.6, rely=0.43, anchor="center")
        self.logout.place(relx=0.6, rely=0.53, anchor="center")
        self.back.place(relx=0.6, rely=0.63, anchor="center")

    def action(self):
        print("Go to profile")
        self.destroy()
        p=Profile(self.master)
        p.show()
    
    def menuaction(self):
        print("Menu clicked")
        self.destroy()
        me = fm.Menudata(self.master)
        me.show()
    
    def oderaction(self):
        print("Show Order details")
        self.destroy()
        oder=fm.Order_details(self.master)
        oder.show()
    
    def trackOrderaction(self):
        print("Track your order")
        self.destroy()
        to=fm.About_order(self.master)
        to.show()
    
    def logoutaction(self):
        with open('store.txt','r+') as f:
            user_name=f.read()
        response = messagebox.askyesno("Logout Confirmation", "Are you sure you want to log out? \nIf yes This action will permanently delete your account.")
        try:
            if response:
                d=bs.Code(self.master)
                ca.cancel_all("App-oder_data.xlsx",user_name)
                d.logout(user_name)
                print("Logout successfully")
                self.destroy()
                home=h.Start(self.master)
                home.show()
            else:
                print("You don't want to logout")
        except Exception as e:
            print("Exception in logout : ",e)
    
    def backaction(self):
        self.destroy()
        go = h.Start(self.master)
        go.show()
        print("you want to go Back")

class Profile(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master=master,**kwargs)
        try:
            with open ('store.txt','r+') as f:
                user=f.read()
            d=bs.Code(self.master)
            details=d.records(user)
        
            userName = details[0]
            user_name = details[1]
            Gen = details[2]
            dob = details[3]
            age = details[4]
            emails = details[5]
            mobile = details[6]
            address = details[7]
            fav_dish = details[8]
            print("details : ",details)      
        except Exception as e:
            print("Exception: ",e)

        self.rightframe = ctk.CTkFrame(self)
        self.background_image = Image.open("leftpicfill.png")
        self.background_image = self.background_image.resize((500, 1000), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(700, 1000))
        self.background_label = ctk.CTkLabel(self, image=self.background_photo, text="")
    
        self.uperframe = ctk.CTkFrame(self.rightframe)
        self.lowerframe = ctk.CTkFrame(self.rightframe)
        
        self.logo_path = "profile.png"
        self.opening = Image.open(self.logo_path)
        self.opening = self.opening.resize((100, 100), Image.Resampling.LANCZOS)
        self.logo_ctk = ctk.CTkImage(light_image=self.opening, size=(100, 100))
        self.profile = ctk.CTkLabel(self.uperframe, text="", image=self.logo_ctk, bg_color="transparent", width=20, height=20, corner_radius=50)

        self.Name = ctk.CTkLabel(self.uperframe, text=f"{user_name.upper()}",width=180,font=("sans",30,"bold"),text_color="blue")
        self.backB = ctk.CTkButton(self.uperframe, text="Back", fg_color="black",font=("Sans",18) ,command=self.back )
        self.edit = ctk.CTkButton(self.lowerframe,width=20, text="🖊️Edit",text_color="black" ,font=("sans",20,"bold"),bg_color="transparent",fg_color="lightblue",command=self.edit_info,hover_color="green")
        self.usernames = ctk.CTkLabel(self.lowerframe, text=f"User name : {userName}",font=("sans",20))
        self.age = ctk.CTkLabel(self.lowerframe, text=f"Age : {age}",font=("sans",20))
        self.dob = ctk.CTkLabel(self.lowerframe, text=f"Date of Birth : {dob}",font=("sans",20))
        self.gender = ctk.CTkLabel(self.lowerframe, text=f"Gender : {Gen}",font=("sans",20))
        self.emailing = ctk.CTkLabel(self.lowerframe, text=f"Email : {emails}",font=("sans",20))
        self.mobile_no = ctk.CTkLabel(self.lowerframe, text=f"Mobile No : {mobile}",font=("sans",20))
        self.addre = ctk.CTkLabel(self.lowerframe, text=f"Address : {address}",font=("sans",20))
        self.fav = ctk.CTkLabel(self.lowerframe, text=f"Favourite Dish: {fav_dish}",font=("sans",20))
        
    def show(self):
        self.pack(fill="both",expand=True,padx=10,pady=10)
        self.background_label.pack(padx=0,pady=0,side="left")
        self.rightframe.pack(fill="both", expand=True, side="right",padx=0)
        self.uperframe.pack(fill="x", padx=0, pady=0, side="top")
        self.lowerframe.pack(fill="both", expand=True, padx=0, pady=(15, 0))

        self.profile.grid(row=0, column=0, padx=2, pady=5)
        self.Name.grid(row=0, column=1, padx=5, pady=5)
        self.backB.place(relx=0.994, rely=0.36, anchor="ne")
        self.edit.place(relx=0.910, rely=0.04, anchor="ne")
        self.usernames.grid(row=0,column=0,padx=(80,0),pady=(80,0),sticky="w")
        self.age.grid(row=1,column=0,padx=(80,0),pady=10,sticky="w")
        self.dob.grid(row=2,column=0,padx=(80,0),pady=10,sticky="w")
        self.gender.grid(row=3,column=0,padx=(80,0),pady=10,sticky="w")
        self.emailing.grid(row=4,column=0,padx=(80,0),pady=10,sticky="w")
        self.mobile_no.grid(row=5,column=0,padx=(80,0),pady=10,sticky="w")
        self.addre.grid(row=6,column=0,padx=(80,0),pady=10,sticky="w")
        self.fav.grid(row=7,column=0,padx=(80,0),pady=10,sticky="w")
        
    def edit_info(self):
        self.destroy()
        f=fd.Details(self.master)
        f.show("update")
        print("Profile Button clicked!")
    def back(self):
        self.destroy()
        me=AppMenu(self.master)
        me.show()
        
