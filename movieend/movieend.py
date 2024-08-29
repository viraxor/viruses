import tkinter as tk
from pygame import mixer
from PIL import ImageGrab, ImageTk, ImageDraw, Image
import os

class App():
    def __init__(self):
        self.ss = ImageGrab.grab().convert("RGBA")
        
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.update()
        
        self.photolabel = tk.Label(self.root, borderwidth=0, highlightthickness=0)
        self.tkphoto = ImageTk.PhotoImage(self.ss)
        
        self.photolabel.config(image=self.tkphoto)
        self.photolabel.grid(row=0, column=0)
        
        mixer.init()
        mixer.music.load("./Silent Night.mp3")
        mixer.music.play()
        
        self.draw_circle()
        self.root.mainloop()
        
    def wait_for_music(self):
        if mixer.get_busy() == False:
            mixer.quit()
            os.system("shutdown /s /f /t 0")
        else:
            self.root.after(1, self.process)
        
    def process(self):
        self.circle = Image.new(size=self.ss.size, color=(0, 0, 0, 255), mode="RGBA")
        self.draw = ImageDraw.Draw(self.circle)
        self.draw.ellipse((self.x - self.init_size, self.y - self.init_size, self.x + self.init_size, self.y + self.init_size), fill=(0, 0, 0, 0))
        self.display = Image.alpha_composite(self.ss, self.circle).convert("RGB")
            
        self.tkphoto = ImageTk.PhotoImage(self.display)
        self.photolabel.config(image=self.tkphoto)
        self.photolabel.grid(row=0, column=0)
        
        self.init_size -= 2
        
        if self.init_size > 0:
            self.root.after(1, self.process)
        else:
            self.root.after(1, self.wait_for_music)
        
    def draw_circle(self):
        self.x, self.y = self.ss.size
        self.x /= 2
        self.y /= 2
        self.init_size = round(max(self.x, self.y) * 8/7)
        
        self.root.after(0, self.process)
        
if __name__ == "__main__":
    App()
