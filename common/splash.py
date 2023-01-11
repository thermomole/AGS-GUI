import tkinter as tk
from PIL import ImageTk, Image 
import customtkinter as ct

# after_cancel tasks: https://stackoverflow.com/questions/63628566/how-to-handle-invalid-command-name-error-while-executing-after-script-in-tk

splash = ct.CTk()

splash.wm_overrideredirect(True)
splash.lift()
splash.config(bg = '#141a23')
splash.wm_attributes("-transparentcolor", "#141a23")
splash_logo = Image.open('images/GQ_AGS.PNG')
splash_img = ImageTk.PhotoImage(splash_logo)
splash_label = tk.Label(image=splash_img,bg="#141a23")
splash_label.image = splash_img
splash_label.place(x=0,y=0)
splash.resizable(False,False)

screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

if screen_height == 1440:
    wid = int(screen_width / 2.5)
    hei = int(screen_height / 2.35)
elif screen_height == 2160:
    wid = int(screen_width / 2)
    hei = int(screen_height / 1.9)
elif screen_height == 1080:
    wid = int(screen_width / 2.75)
    hei = int(screen_height / 2.6)
else:
    wid = int(screen_width / 4)
    hei = int(screen_height / 4)

splash.geometry(f"485x225+{wid}+{hei}")

def splash_init():
    splash.after(4000,lambda:del_splash())
    splash.attributes("-topmost", True)
    splash.mainloop()
    
def del_splash():
    for after_id in splash.tk.eval('after info').split():
        splash.after_cancel(after_id)

    splash.destroy()

splash_init()
