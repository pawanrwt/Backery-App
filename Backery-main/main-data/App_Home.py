import customtkinter as ctk
from PIL import Image
import App_LoginPanel as lo

class Start(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.background_image = Image.open("start.png")
        self.background_image = self.background_image.resize((1300, 900), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(1300, 900))
        self.background_label = ctk.CTkLabel(self, image=self.background_photo, text="")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.l_title = ctk.CTkLabel(self, text="_ _WELCOME_ _", font=("sans", 20))
        self.b_start = ctk.CTkButton(self, height=40, width=200, text="Start", command=self.start_action, fg_color="green", font=("sans", 15))
        self.b_settings = ctk.CTkButton(self, height=40, width=200, text="🔙", command=self.back, fg_color="blue", font=("sans", 30))

    def start_action(self):
        print("Start click")
        self.destroy()
        des=HomePanel(self.master)
        des.show()

    def back(self):
        print("Exit")
        exit(0)

    def show(self):
        self.pack(fill="both", expand=True,pady=15)
        self.l_title.pack(pady=(360,10))
        self.b_start.pack(pady=10)
        self.b_settings.pack(pady=10)

class HomePanel(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        
        self.background_image = Image.open("home.png")
        self.background_image = self.background_image.resize((1300, 1000), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(1300, 1000))
        self.background_label = ctk.CTkLabel(self, image=self.background_photo, text="")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.sign_up = ctk.CTkButton(self, text="Sign up", fg_color="Green", command=self.signing,height=40, width=200,font=("sans",20))
        self.login = ctk.CTkButton(self, text="Login", fg_color="blue",command=self.logining,height=40, width=200,font=("sans",20))
        self.back = ctk.CTkButton(self, text="🔙", width=7,height=1,fg_color="black",bg_color="red",font=("sans",30),command=self.back_action,border_width=10)

    def show(self):
        self.pack(fill="both", expand=True, pady=30, padx=30)
        self.back.grid(row=0, column=0, padx=(1200,10), pady=20,)
        self.sign_up.grid(row=1, column=0,  pady=(180, 10))
        self.login.grid(row=2, column=0, pady=10)

    def signing(self):
        self.destroy()
        go=lo.SignUp(self.master)
        go.show()

    def logining(self):
        self.destroy()
        go=lo.Login(self.master)
        go.show()
        
    def back_action(self):
        Start(self).back()

