import tkinter as tk
from tkinter import filedialog
from python_ags4 import AGS4
from pandasgui import show

def make_ags():
    tables, headings = AGS4.AGS4_to_dataframe(fileLocation)
    print(fileLocation)

def writeNewFile():
    newFileName = filedialog.asksaveasfilename(filetypes=[('AGS Files', '*.ags')])
    updated_tables = gui.get_dataframes()
    AGS4.dataframe_to_AGS4(updated_tables, headings, newFileName)

root = tk.Tk()
root.withdraw()
fileLocation = filedialog.askopenfilename(filetypes=[('AGS Files', '*.ags')])
tables, headings = AGS4.AGS4_to_dataframe(fileLocation)
gui = show(**tables)

make_ags()
writeNewFile()