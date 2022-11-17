import tkinter as tk
from PIL import ImageTk, Image 
import customtkinter as ct

# after_cancel tasks: https://stackoverflow.com/questions/63628566/how-to-handle-invalid-command-name-error-while-executing-after-script-in-tk

splash = ct.CTk()

screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

if screen_height == 1440:
    wid = int(screen_width / 2.5)
    hei = int(screen_height / 2.5)
elif screen_height == 2160:
    wid = int(screen_width / 2)
    hei = int(screen_height / 2)
else:
    wid = int(screen_width / 3)
    hei = int(screen_height / 3)

splash.geometry(f"640x320+{wid}+{hei}")

splash.wm_overrideredirect(True)
splash.lift()
splash.config(bg = '#000000')
splash.wm_attributes("-transparentcolor", "black")
splash_logo = Image.open('images/GQ_AGS.PNG')
splash_img = ImageTk.PhotoImage(splash_logo)
splash_label = tk.Label(image=splash_img,bg='black')
splash_label.image = splash_img
splash_label.place(x=0,y=0)

def splash_init():
    splash.after(4000,lambda:del_splash())
    splash.attributes("-topmost", True)
    splash.mainloop()
    
def del_splash():
    for after_id in splash.tk.eval('after info').split():
        splash.after_cancel(after_id)

    splash.destroy()

splash_init()

