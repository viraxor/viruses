import tkinter as tk
from PIL import ImageGrab, ImageTk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.update()
        
        self.time = 1000 # in ms
        
        self.photolabel = tk.Label(self.root, borderwidth=0, highlightthickness=0)
        self.screenshot()
        
        self.root.after(self.time, self.screenshot)
        self.root.mainloop()
        
    def screenshot(self):
        self.root.withdraw()
        
        self.ss = ImageGrab.grab()
        self.tkphoto = ImageTk.PhotoImage(self.ss)
        self.photolabel.config(image=self.tkphoto)
        self.photolabel.grid(row=0, column=0)
        
        self.root.deiconify()
        
        self.root.after(self.time, self.screenshot)
        
if __name__ == "__main__":
    App()
