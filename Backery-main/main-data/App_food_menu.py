import customtkinter as ctk
from tkinter import messagebox
from PIL import Image
import App_backed as bs
import App_excelserver as dl
import random as rd
from datetime import datetime
import App_menu as am
import App_Home as h

class Menudata(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.configure(fg_color="white")
        self.searchFrame = ctk.CTkFrame(self)
        image_path = "profile.png"
        image = Image.open(image_path)
        image = image.resize((100, 100), Image.Resampling.LANCZOS)
        self.image_ctk = ctk.CTkImage(light_image=image, size=(100, 100))
        self.profile = ctk.CTkLabel(self.searchFrame, text="", image=self.image_ctk, bg_color="transparent", width=20, height=20, corner_radius=50)
        self.searching = ctk.CTkEntry(self.searchFrame, fg_color="transparent", width=500)
        self.search = ctk.CTkButton(self.searchFrame, text="🔍 search",font=("Sans",18) , fg_color="green", command=self.searchaction)
        self.backB = ctk.CTkButton(self.searchFrame, text="Back",font=("Sans",18) , fg_color="Black", command=self.back)
        self.scrollFrame = ctk.CTkFrame(self)
        self.scrollable_frame = ctk.CTkScrollableFrame(self.scrollFrame, width=780, height=580)
        self.data = dl.load_data("App-data.xlsx")
        self.popup = None

    def show(self):
        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.searchFrame.pack(fill="x", padx=10, pady=(10, 0))
        self.profile.grid(row=0, column=0, padx=10, pady=20)
        self.searching.grid(row=0, column=1, padx=10, pady=20)
        self.search.grid(row=0, column=2, padx=10, pady=20)
        self.backB.grid(row=0, column=3, padx=10, pady=20)
        self.scrollFrame.pack(fill="both", expand=True, padx=10, pady=0)
        self.scrollable_frame.pack(fill="both", expand=True, padx=15, pady=15)
        self.populate(self.data)

    def populate(self, data):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        if self.popup is not None:
            self.popup.destroy()
            self.popup = None
        r = 0
        c = 0
        if data:
            print(f"item is available on our backery")
            for i, item in enumerate(data):
                image_path, food_name, price = item
                image = Image.open(image_path)
                image = image.resize((120, 120), Image.Resampling.LANCZOS)
                image_ctk = ctk.CTkImage(light_image=image, size=(120, 120))
                image_label = ctk.CTkLabel(self.scrollable_frame, image=image_ctk, text="", width=150, height=150, fg_color="transparent")
                food_button = ctk.CTkButton(self.scrollable_frame, text=food_name, command=lambda img=image_path, name=food_name, prc=price: self.placeorder(img, name, prc))
                price_label = ctk.CTkLabel(self.scrollable_frame, text=f"Rs. {str(price)}", text_color="red", font=("sans", 15))

                if c % 6 == 0 and c != 0:
                    r += 3
                    c = 0
                image_label.grid(row=r, column=c, padx=16, pady=(2, 0))
                food_button.grid(row=r + 1, column=c, padx=0, pady=0, sticky="n")
                price_label.grid(row=r + 2, column=c, padx=0, pady=0)
                c += 1
        else:
            print("Result not found")
            self.popup = ctk.CTkLabel(self.searchFrame, text="*Item not available", fg_color="transparent", bg_color="transparent", text_color="red")
            self.popup.grid(row=0, column=1, padx=10, pady=(100, 10))

    def searchaction(self):
        food = self.searching.get().lower()
        print("Searching :",food)
        filtered_data = [item for item in self.data if food in item[1].lower()]
        self.populate(filtered_data)

    def back(self):
        self.destroy()
        a = am.AppMenu(self.master)
        a.show()

    def placeorder(self, image_path, food_name, price):
        try:
            food_id = 'Food' + str(rd.randint(100, 9999))
            dateoforder = datetime.now().strftime("%Y-%m-%d")
            fetch = bs.Code(self.master)
            user_info = fetch.userinfo()

            if user_info and len(user_info) > 0:
                user_record = user_info[0]
                user_name = user_record[0]
                user_phone = user_record[1]
                user_address = user_record[2]
                response = messagebox.askyesno("Confirmation", f"Are you sure you want to order {food_name}")
                if response:
                    dl.save_order(image_path, food_name, price, food_id, user_name, dateoforder, user_phone, user_address)
                    print(f"{food_name} has ordered")
                else:
                    print("Item has not ordered")
            else:
                print("Error: No user information found.")
        except Exception as e:
            print("Error:", e)

class Order_details(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)

        sh=self.winfo_screenheight()
        self.configure(fg_color="white")
        self.rightframe = ctk.CTkFrame(self, width=50)
        
        self.background_image = Image.open("leftpicfill.png")
        self.background_image = self.background_image.resize((600, sh), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(600, sh))
        self.background_label = ctk.CTkLabel(self,image=self.background_photo, text="")
        
        self.buttonframe = ctk.CTkFrame(self.rightframe)
        self.home_button = ctk.CTkButton(self.buttonframe, text="<Home", font=("sans",20,"bold"),fg_color="green",command=self.home)
        self.backB = ctk.CTkButton(self.buttonframe, text="Back>", font=("sans",20,"bold"),fg_color="Black", command=self.back)
        
        self.scrollFrame = ctk.CTkFrame(self.rightframe)
        self.scrollable_frame = ctk.CTkScrollableFrame(self.scrollFrame, width=780, height=580)
        self.popup=ctk.CTkLabel(self.scrollable_frame,text="*You haven't ordered anything yet.\nExplore delicious options and place your first order now!",text_color="red",font=("sans",20))
        with open ('store.txt','r+') as f:
            uname=f.read()
        self.data = dl.load_order("App-oder_data.xlsx",uname)

    def show(self):
        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.background_label.pack(padx=0,pady=0,side="left")
        self.rightframe.pack(fill="both",expand=True, padx=0, side="right")
        
        self.buttonframe.pack(fill="x", padx=10, pady=0, side="top")
        self.home_button.grid(row=0, column=0, padx=40, pady=15)
        self.backB.place(relx=0.974, rely=0.25, anchor="ne")
        
        self.scrollFrame.pack(fill="both", expand=True, padx=10, pady=0)
        self.scrollable_frame.pack(fill="both", expand=True, padx=15, pady=(15,0))
        if self.data:
            self.populate(self.data)
        else:
            print("No ordered yet")
            self.popup.pack(padx=10,pady=100,anchor="center")

    def populate(self, data):
     
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        
        r=0
        c=0
        if data:
            for i, item in enumerate(data):
                id_food,image_path, food_name, price,orderby,orderdate,mobile,addr = item
                image = Image.open(image_path)
                image = image.resize((200, 200), Image.Resampling.LANCZOS)
                image_ctk = ctk.CTkImage(light_image=image, size=(200, 200))

                food_id = ctk.CTkLabel(self.scrollable_frame, text=f"Food ID :{id_food}",fg_color="transparent",font=("sans",16))
                image_label = ctk.CTkLabel(self.scrollable_frame, image=image_ctk, text="", width=150, height=150, fg_color="transparent")
                food_name = ctk.CTkLabel(self.scrollable_frame ,text=f"Item Name :{food_name}",font=("sans",16),fg_color="transparent")
                price_label = ctk.CTkLabel(self.scrollable_frame, text=f"Price  : Rs. {str(price)}",font=("sans",16),text_color="red")
                user = ctk.CTkLabel(self.scrollable_frame, text=f"Order By :{orderby}",fg_color="transparent",font=("sans",16))
                dateof = ctk.CTkLabel(self.scrollable_frame, text=f"Date  :  {orderdate}",font=("sans",16))
                phone = ctk.CTkLabel(self.scrollable_frame, text=f"Mobile No :{mobile}",fg_color="transparent",font=("sans",16))
                address = ctk.CTkLabel(self.scrollable_frame, text=f"Address  :  {addr}",font=("sans",16))

                image_label.grid(row=r, column=0, padx=0, pady=(25, 5),sticky="w")
                food_id.grid(row=r, column=1, padx=40, pady=(10,150),sticky="w")
                
                food_name.grid(row=r, column=1, padx=40, pady=(40,130),sticky="w")
                price_label.grid(row=r, column=1, padx=40, pady=(70,110),sticky="w")
                user.grid(row=r, column=1, padx=40, pady=(100,90),sticky="w")
                dateof.grid(row=r, column=1, padx=40, pady=(130,70),sticky="w")
                phone.grid(row=r, column=1, padx=40, pady=(160,50),sticky="w")
                address.grid(row=r, column=1, padx=40, pady=(190,30),sticky="w")
                r+=1

    def back(self):
        self.destroy()
        b=am.AppMenu(self.master)
        b.show()
    def home(self): 
        self.destroy()
        ho=h.Start(self.master)
        ho.show()



class About_order(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
       
        sh=self.winfo_screenheight()
        self.rightframe = ctk.CTkFrame(self)
        
        self.background_image = Image.open("leftpicfill.png")
        self.background_image = self.background_image.resize((700, sh), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(700, sh))
        self.background_label = ctk.CTkLabel(self, image=self.background_photo, text="")
        
        self.uperframe = ctk.CTkFrame(self.rightframe)
        self.lowerframe = ctk.CTkFrame(self.rightframe)
        
        self.logo_path = "profile.png"
        self.opening = Image.open(self.logo_path)
        self.opening = self.opening.resize((100, 100), Image.Resampling.LANCZOS)
        self.logo_ctk = ctk.CTkImage(light_image=self.opening, size=(100, 100))
        self.profile = ctk.CTkLabel(self.uperframe, text="", image=self.logo_ctk, bg_color="transparent", width=20, height=20, corner_radius=50)

        self.content = ctk.CTkEntry(self.uperframe, width=180)
        self.search = ctk.CTkButton(self.uperframe, text="🔍 Search",font=("Sans",18) ,fg_color="green", command=self.populate)
        self.backB = ctk.CTkButton(self.uperframe, text="Back", fg_color="black",font=("Sans",18) , command=self.back)
        self.popup=None
    def show(self):
        self.pack(fill="both",expand=True,padx=10,pady=10)
        self.background_label.pack(padx=0,pady=0,side="left")
        self.rightframe.pack(fill="both", expand=True, side="right",padx=0)

        
        self.uperframe.pack(fill="x", padx=0, pady=0, side="top")
        self.lowerframe.pack(fill="both", expand=True, padx=0, pady=(15, 0))

        
        self.profile.grid(row=0, column=0, padx=2, pady=5)
        self.content.grid(row=0, column=1, padx=10, pady=5)
        self.search.grid(row=0, column=2, padx=5, pady=5)
        self.backB.grid(row=0, column=3, padx=2, pady=5)


    def populate(self):
        
        for widget in self.lowerframe.winfo_children():
            widget.destroy()
        food_id = self.content.get()
        with open ('store.txt','r+') as f:
            user_n=f.read()

        items = dl.trackorder("App-oder_data.xlsx", food_id,user_n)

        if items:
            if self.popup is not None:
                self.popup.destroy()
                self.popup=None

            for item in items:
                id_food, image_path, food_name, price, orderby, orderdate, mobile, addr,status = item
                if(status.lower()=='yes'):
                    check="Delivery Status : Item Delivered"
                elif(status.lower()=="no"):
                    check="Delivery Date : "+datetime.now().strftime("%Y-%m-%d")

                if(len(food_name)>=25):
                    food_name=f"{food_name[:25]}...."

                self.image = Image.open(image_path)
                self.image = self.image.resize((200, 200), Image.Resampling.LANCZOS)
                self.image_ctk = ctk.CTkImage(light_image=self.image, size=(200, 200))

                self.food_id_label = ctk.CTkLabel(self.lowerframe, text=f"Food ID: {id_food}", fg_color="transparent", font=("sans", 16))
                self.image_label = ctk.CTkLabel(self.lowerframe, image=self.image_ctk, text="", width=150, height=150, fg_color="transparent")
                self.food_name_label = ctk.CTkLabel(self.lowerframe, text=f"Item Name: {food_name}", font=("sans", 16), fg_color="transparent")
                self.price_label = ctk.CTkLabel(self.lowerframe, text=f"Price: Rs. {str(price)}", font=("sans", 16), text_color="red")
                self.user_label = ctk.CTkLabel(self.lowerframe, text=f"Order By: {orderby}", fg_color="transparent", font=("sans", 16))
                self.date_label = ctk.CTkLabel(self.lowerframe, text=f"Date: {orderdate}", font=("sans", 16))
                self.phone_label = ctk.CTkLabel(self.lowerframe, text=f"Mobile No: {mobile}", fg_color="transparent", font=("sans", 16))
                self.address_label = ctk.CTkLabel(self.lowerframe, text=f"Address: {addr}", font=("sans", 16))
                self.d_status = ctk.CTkLabel(self.lowerframe, text=f"{check}", font=("sans", 16))
                self.cencel_order=ctk.CTkButton(self.lowerframe,text="Cencel Order",font=("Sans",18,'bold'),fg_color="green",command =lambda fid=id_food,uname=orderby:self.cencel(fid,user_n))
                
                # Pack the dynamic components
                self.image_label.grid(row=0, column=0, padx=20, pady=(100,0))
                self.food_id_label.grid(row=0, column=1, padx=50, pady=(0,80),sticky="w")
                self.food_name_label.grid(row=0, column=1, padx=50, pady=(50,82),sticky="w")
                self.price_label.grid(row=0, column=1, padx=50, pady=(100,84),sticky="w")
                self.user_label.grid(row=0, column=1, padx=50, pady=(150,86),sticky="w")
                self.date_label.grid(row=0, column=1, padx=50, pady=(200,88),sticky="w")
                self.phone_label.grid(row=0, column=1, padx=50, pady=(250,90),sticky="w")
                self.address_label.grid(row=0, column=1, padx=50, pady=(300,92),sticky="w")
                self.d_status.grid(row=0,column=1, padx=50, pady=(350,94),sticky="w")
                if status.lower() =="no":
                    self.cencel_order.grid(row=0,column=1,padx=50,pady=(450,98),sticky="w")

        else:
            print("*Item ID is invaild, Try again.")
            if self.popup is not None:
                self.popup.destroy()
            self.popup=ctk.CTkLabel(self.uperframe,text="*Item ID is invaild, Try again.",text_color="red",fg_color="transparent",font=("sans",14,'bold'))
            self.popup.grid(row=0,column=1,padx=0,pady=(60,0),)
        
    def back(self):
        self.destroy()
        b=am.AppMenu(self.master)
        b.show()
    def cencel(self,fid,uname):
        response=messagebox.askyesno("Confirmation",f"Are you sure you want cancel you order {fid}")
        if response:
            check=dl.cancel_order("App-oder_data.xlsx",fid,uname)
            if check is False:
                print("Order did not cancel")
                self.popup=ctk.CTkLabel(self.uperframe,text=f"*Server Error",text_color="red",fg_color="transparent",font=("sans",16,'bold'))
                self.popup.grid(row=0,column=1,padx=(0,70),pady=(60,0),)
            else:
                for widget in self.lowerframe.winfo_children():
                    widget.destroy()
                self.popup=ctk.CTkLabel(self.uperframe,text=f"*Order Cancelled, \nwhere Food ID: {fid}",text_color="red",fg_color="transparent",font=("sans",12,'bold'))
                self.popup.grid(row=0,column=1,padx=0,pady=(60,0),)
                print("*Oder cancelled")
                self.content.delete(0,ctk.END)



