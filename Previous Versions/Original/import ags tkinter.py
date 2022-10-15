import tkinter as tk
from tkinter import filedialog
from python_ags4 import AGS4
from pandasgui import show

root = tk.Tk()
root.withdraw()

fileLocation = filedialog.askopenfilename(filetypes=[('AGS Files', '*.ags')])

def make_ags():
    tables, headings = AGS4.AGS4_to_dataframe(fileLocation)
    print(fileLocation)
make_ags()

def open_gui():
    tables, headings = AGS4.AGS4_to_dataframe(fileLocation)
    gui = show(**tables)
open_gui()


