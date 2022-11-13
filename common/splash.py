import tkinter as tk
from PIL import ImageTk, Image 
import customtkinter as ct

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

splash.geometry(f"510x255+{wid}+{hei}")

splash.wm_overrideredirect(True)
splash.lift()
splash.wm_attributes("-transparentcolor", "black")
splash_logo = Image.open('images/GQ_AGS.PNG')
splash_img = ImageTk.PhotoImage(splash_logo)
splash_label = tk.Label(image=splash_img,bg='black')
splash_label.image = splash_img
splash_label.place(x=0,y=0)

def splash_init():
    global after_id
    after_id = splash.after(4000,lambda:del_splash())
    splash.mainloop()
    
def del_splash():
    global after_id
    splash.after_cancel(after_id)
    after_id = None
    splash.destroy()

splash_init()
