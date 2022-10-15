import tkinter as tk
from tkinter import filedialog
from python_ags4 import AGS4
from pandasgui import show

def make_ags():
    tables, headings = AGS4.AGS4_to_dataframe(fileLocation)
    print(fileLocation)

def writeNewFile():
    newFile = fileLocation.split(".ags")
    newFile[0] += '_'
    newFile[0] += '1'
    newFileName = newFile[0]
    newFileName += '.ags'
    print(newFileName)
    updated_tables = gui.get_dataframes()
    AGS4.dataframe_to_AGS4(updated_tables, headings, newFileName)

root = tk.Tk()
root.withdraw()
fileLocation = filedialog.askopenfilename(filetypes=[('AGS Files', '*.ags')])
tables, headings = AGS4.AGS4_to_dataframe(fileLocation)
gui = show(**tables)

make_ags()
writeNewFile()

#to export
#updated_tables = gui.get_dataframes()
#writeNewFile()
#AGS4.dataframe_to_AGS4(updated_tables, headings, newFileName)

