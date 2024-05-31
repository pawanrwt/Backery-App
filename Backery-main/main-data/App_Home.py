import customtkinter as ctk
from PIL import Image
import App_LoginPanel as lo

class Start(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.background_image = Image.open("start.png")
        self.background_image = self.background_image.resize((2000, 2000), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(2000, 2000))
        self.background_label = ctk.CTkLabel(self, image=self.background_photo, text="")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.l_title = ctk.CTkLabel(self, text="_ _WELCOME_ _", font=("sans", 20))
        self.b_start = ctk.CTkButton(self, height=40, width=200, text="Start", command=self.start_action, fg_color="green",bg_color="green", font=("sans", 15))
        self.b_settings = ctk.CTkButton(self, height=40, width=200, text="🔙", command=self.back, fg_color="blue",bg_color="green", font=("sans", 30))

    def start_action(self):
        print("Start click")
        self.destroy()
        des = HomePanel(self.master)
        des.show()

    def back(self):
        print("Exit")
        exit(0)

    def show(self):
        self.pack(fill="both", expand=True, padx=10, pady=10)
        self.l_title.place(relx=0.5, rely=0.45, anchor="center")
        self.b_start.place(relx=0.5, rely=0.52, anchor="center")
        self.b_settings.place(relx=0.5, rely=0.59, anchor="center") 

class HomePanel(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master=master, **kwargs)
        self.background_image = Image.open("home.png")
        self.background_image = self.background_image.resize((1500, 1000), Image.Resampling.LANCZOS)
        self.background_photo = ctk.CTkImage(light_image=self.background_image, size=(1500, 1000))
        self.background_label = ctk.CTkLabel(self, image=self.background_photo, text="")
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.sign_up = ctk.CTkButton(self, text="Sign up", fg_color="Green", bg_color="green" ,command=self.signing, height=40, width=200, font=("sans", 20))
        self.login = ctk.CTkButton(self, text="Login", fg_color="blue",bg_color="blue" , command=self.logining, height=40, width=200, font=("sans", 20))
        self.back = ctk.CTkButton(self, text="🔙", width=60, height=50, fg_color="darkblue",bg_color="darkblue" ,font=("sans", 40), command=self.back_action)

    def show(self):
        self.pack(fill="both", expand=True, pady=10, padx=10)
        self.sign_up.place(relx=0.5, rely=0.5, anchor="center")
        self.login.place(relx=0.5, rely=0.58, anchor="center")
        self.back.place(relx=0.994, rely=0.02, anchor="ne") 
    def signing(self):
        self.destroy()
        go = lo.SignUp(self.master)
        go.show()

    def logining(self):
        self.destroy()
        go = lo.Login(self.master)
        go.show()

    def back_action(self):
        Start.back(self)


