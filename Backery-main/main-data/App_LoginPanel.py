import customtkinter as ctk
import App_Home as h
from PIL import Image
import App_backed as bs
import App_FillDetails as fd
import App_menu as am

class SignUp(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master=master,**kwargs)
        self.background_image = Image.open("login_signup.png")
        self.background_image = self.background_image.resize((1300, 1000), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(1300, 1000))
        self.background_label = ctk.CTkLabel(self, image=self.background_photo, text="")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.t1 = ctk.CTkLabel(self, text="User Name", width=80,fg_color="transparent",font=("sans",14,'bold'))
        self.user = ctk.CTkEntry(self)
        self.t2 = ctk.CTkLabel(self, text="Password",width=80, fg_color=None,font=("sans",14,'bold'))
        self.pas = ctk.CTkEntry(self)
        self.popup=ctk.CTkLabel(self,font=("sans",12),text_color="red",width=20,height=6)
        self.create = ctk.CTkButton(self, text="Create Account", fg_color="Green", command=self.account)
        self.back = ctk.CTkButton(self, text="Go back", fg_color="Green", command=self.goback)

    def getdata(self):
        uname=self.user.get()
        pas=self.pas.get()
        with open ('store.txt','w+') as f:
            f.write(uname)
        store=bs.Code(self.master)
        s=store.Insertion(uname,pas)
        return s
        
    def show(self):
        self.pack(fill="both", expand=True, padx=15, pady=15)
        self.t1.place(x=580,y=270)
        self.user.place(x=680,y=270,)
        self.t2.place(x=580,y=320)
        self.pas.place(x=680,y=320)
        self.create.place(x=650,y=400)
        self.back.place(x=650,y=440,)

    def goback(self):
        self.destroy()
        home=h.HomePanel(self.master)
        home.show()

    def account(self):
        pas=self.pas.get()
        if len(pas)<8:
            self.popup.configure(text="*Password must contain more than 8 characters.",font=("sans",15))
            self.popup.place(x=580,y=370,)
        else:
            print("Sign up click")
            g=self.getdata()
            if (g==False):
                self.popup.configure(text="*Please enter password",font=("sans",15))
                self.popup.place(x=640,y=370,)
            elif(g=="False2"):
                self.popup.configure(text="*Please enter valid user name",font=("sans",15))
                self.popup.place(x=630,y=370,)
            elif(g==10):
                self.popup.configure(text="*Username already exists",font=("sans",15))
                self.popup.place(x=640,y=370,)
            else:
                self.destroy()
                go=fd.Details(self.master)
                go.show("save")

class Login(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master=master,**kwargs)
        self.background_image = Image.open("login_signup.png")
        self.background_image = self.background_image.resize((1300, 1000), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(1300, 1000))
        self.background_label = ctk.CTkLabel(self, image=self.background_photo, text="")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.t1 = ctk.CTkLabel(self, text="User Name",width=80,fg_color="transparent",font=("sans",14,'bold'))
        self.user = ctk.CTkEntry(self)
        self.t2 = ctk.CTkLabel(self, text="Password", width=80,fg_color=None,font=("sans",14,'bold'))
        self.pas = ctk.CTkEntry(self)
        self.popup=ctk.CTkLabel(self,font=("sans",12),text_color="red",width=20,height=6)
        self.log = ctk.CTkButton(self, text="Login", fg_color="blue", command=self.account)
        self.back = ctk.CTkButton(self, text="Back", fg_color="black", command=self.goback)

    def show(self):
        self.pack(fill="both", expand=True, padx=15, pady=15)
        self.t1.place(x=580,y=270)
        self.user.place(x=680,y=270,)
        self.t2.place(x=580,y=320)
        self.pas.place(x=680,y=320)
        self.log.place(x=650,y=420)
        self.back.place(x=650,y=460,)

    def getdata(self):
        uname=self.user.get()
        pas=self.pas.get()
        with open('store.txt','w+') as f:
            f.write(uname)
        ch=bs.Code(self.master)
        check=ch.Check(uname,pas)
        return check

    def goback(self):
        self.destroy()
        home=h.HomePanel(self.master)
        home.show()
        
    def account(self):
        print("Login clicked")
        ch=self.getdata()
        if (ch==False):
            self.popup.configure(text="*Password is wrong try again",font=("sans",15))
            self.popup.place(x=630,y=385,)
        elif(ch=="False2"):
            self.popup.configure(text="*User name not found,\n Please Enter valid user name",font=("sans",15))
            self.popup.place(x=630,y=370,)
        elif(ch=="server"):
            self.popup.configure(text="*Server Error",font=("sans",15))
            self.popup.place(x=668,y=370,)

        else:
            self.destroy()
            menu=am.AppMenu(self.master)
            menu.show()
            print("Login Successfully")

