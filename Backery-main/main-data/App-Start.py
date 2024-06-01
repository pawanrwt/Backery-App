import customtkinter as ctk
import App_Home as h
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        #self.state("zoomed")
        self.attributes('-fullscreen',True)
        self.title("BACKRY SYSTEM")
        self.hp = h.Start(self.master)
    def show(self):
        self.hp.show()
        self.mainloop()
if __name__ == "__main__":
    print("App Loading")
    app = App()
    app.show()
