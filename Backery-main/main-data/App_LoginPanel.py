import customtkinter as ctk
import App_Home as h
from PIL import Image
import App_backed as bs
import App_FillDetails as fd
import App_menu as am

class SignUp(ctk.CTkFrame):
    def __init__(self, master,**kwargs):
        super().__init__(master=master,**kwargs)
        sw=self.winfo_screenwidth()
        sh=self.winfo_screenheight()
        self.background_image = Image.open("login_signup.png")
        self.background_image = self.background_image.resize((sw, sh), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(sw, sh))
        self.background_label = ctk.CTkLabel(self, image=self.background_photo, text="")
        
        self.t1 = ctk.CTkLabel(self, text="User Name", width=80,fg_color="transparent",font=("sans",14,'bold'))
        self.user = ctk.CTkEntry(self)
        self.t2 = ctk.CTkLabel(self, text="Password",width=80, fg_color=None,font=("sans",14,'bold'))
        self.pas = ctk.CTkEntry(self)
        self.popup=ctk.CTkLabel(self,font=("sans",12),text_color="red",width=20,height=6)
        self.create = ctk.CTkButton(self, text="Create Account", bg_color="green",fg_color="Green", command=self.account)
        self.back = ctk.CTkButton(self, text="Go back", bg_color="black",fg_color="black", command=self.goback)

    def getdata(self):
        uname=self.user.get()
        pas=self.pas.get()
        with open ('store.txt','w+') as f:
            f.write(uname)
        store=bs.Code(self.master)
        s=store.Insertion(uname,pas)
        return s
        
    def show(self):
        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.background_label.place(x=0, y=0,relwidth=1, relheight=1)
        self.t1.place(relx=0.44, rely=0.45, anchor="center")
        self.user.place(relx=0.53, rely=0.45, anchor="center")
        self.t2.place(relx=0.44, rely=0.5, anchor="center")
        self.pas.place(relx=0.53, rely=0.5, anchor="center")
        self.create.place(relx=0.49, rely=0.6, anchor="center")
        self.back.place(relx=0.49, rely=0.65, anchor="center")

    def goback(self):
        self.destroy()
        home=h.HomePanel(self.master)
        home.show()

    def account(self):
        pas=self.pas.get()
        if len(pas)<8 and pas:
            self.popup.configure(text="*Password must contain more than 8 characters.",font=("sans",15))
            self.popup.place(relx=0.49, rely=0.55, anchor="center")
        else:
            print("Sign up click")
            g=self.getdata()
            if (g==False):
                self.popup.configure(text="*Please enter password",font=("sans",15))
                self.popup.place(relx=0.49, rely=0.55, anchor="center")
            elif(g=="False2"):
                self.popup.configure(text="*Please enter valid user name",font=("sans",15))
                self.popup.place(relx=0.49, rely=0.55, anchor="center")
            elif(g==10):
                self.popup.configure(text="*Username already exists",font=("sans",15))
                self.popup.place(relx=0.49, rely=0.55, anchor="center")
            else:
                self.destroy()
                go=fd.Details(self.master)
                go.show("save")

class Login(ctk.CTkFrame):
    def __init__(self,master,**kwargs):
        super().__init__(master=master,**kwargs)
        sw=self.winfo_screenwidth()
        sh=self.winfo_screenheight()
        self.background_image = Image.open("login_signup.png")
        self.background_image = self.background_image.resize((sw, sh), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(sw, sh))
        self.background_label = ctk.CTkLabel(self, image=self.background_photo, text="")
        
        self.t1 = ctk.CTkLabel(self, text="User Name",width=80,fg_color="transparent",font=("sans",14,'bold'))
        self.user = ctk.CTkEntry(self)
        self.t2 = ctk.CTkLabel(self, text="Password", width=80,fg_color=None,font=("sans",14,'bold'))
        self.pas = ctk.CTkEntry(self)
        self.popup=ctk.CTkLabel(self,font=("sans",12),text_color="red",width=20,height=6)
        self.log = ctk.CTkButton(self, text="Login", fg_color="blue", bg_color="blue",command=self.account)
        self.back = ctk.CTkButton(self, text="Back", fg_color="black", bg_color="black",command=self.goback)

    def show(self):
        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.background_label.place(x=0, y=0,relwidth=1, relheight=1)
        self.t1.place(relx=0.44, rely=0.45, anchor="center")
        self.user.place(relx=0.53, rely=0.45, anchor="center")
        self.t2.place(relx=0.44, rely=0.5, anchor="center")
        self.pas.place(relx=0.53, rely=0.5, anchor="center")
        self.log.place(relx=0.49, rely=0.62, anchor="center")
        self.back.place(relx=0.49, rely=0.67, anchor="center")

    def getdata(self):
        uname=self.user.get()
        pas=self.pas.get()
        if len(uname)>0 and len(pas)>0:
            with open('store.txt','w+') as f:
                f.write(uname)
            ch=bs.Code(self.master)
            check=ch.Check(uname,pas)
            return check
        else:
            return "false"

    def goback(self):
        self.destroy()
        home=h.HomePanel(self.master)
        home.show()
        
    def account(self):
        print("Login clicked")
        ch=self.getdata()
        if (ch=="false"):
            self.popup.configure(text="*Please enter username and password",font=("sans",15))
            self.popup.place(relx=0.49, rely=0.56, anchor="center")
        elif (ch==False):
            self.popup.configure(text="*Password is wrong try again",font=("sans",15))
            self.popup.place(relx=0.49, rely=0.56, anchor="center")
        elif(ch=="False2"):
            self.popup.configure(text="*User name not found,\n Please Enter valid user name",font=("sans",15))
            self.popup.place(relx=0.49, rely=0.56, anchor="center")
        elif(ch=="server"):
            self.popup.configure(text="*Server Error",font=("sans",15))
            self.popup.place(relx=0.49, rely=0.56, anchor="center")
        else:
            self.destroy()
            menu=am.AppMenu(self.master)
            menu.show()
            print("Login Successfully")

