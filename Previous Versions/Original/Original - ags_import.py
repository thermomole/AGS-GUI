from python_ags4 import AGS4
tables, headings = AGS4.AGS4_to_dataframe(R'C:\Users\DataEntry1\OneDrive - Geoquip Marine Operations AG\Desktop\AGS\AGS.AGS')

#to export
#AGS4.dataframe_to_AGS4(tables, headings, R'C:\Users\DataEntry1\OneDrive - Geoquip Marine Operations AG\Desktop\AGS\AGSout.AGS')

#opens GUI
from pandasgui import show
tables, headings = AGS4.AGS4_to_dataframe(R'C:\Users\DataEntry1\OneDrive - Geoquip Marine Operations AG\Desktop\AGS\AGS.AGS')
gui = show(**tables)