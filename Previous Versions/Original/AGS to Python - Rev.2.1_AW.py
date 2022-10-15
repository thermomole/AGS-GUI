import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from python_ags4 import AGS4
from pandasgui import show
    
class Application(ttk.Frame):

    def __init__(self, master):
        ttk.Frame.__init__(self, master)
        self.pack()
        master.geometry('300x200')
        master.title("AGS tools")
        self.greeting = tk.Label(text="Open an AGS file and choose what to do...")
        self.greeting.pack(pady=8)
        
        self.button_open = ttk.Button(self, text="Open File...", command=self.get_ags_file_location)
        self.button_open.pack(pady=8)

        self.button_showinfo = ttk.Button(self, text="View Data", command=self.start_pandasgui)
        self.button_showinfo.pack(pady=8)
        self.button_showinfo["state"] = "disabled"
        
        self.button_ags_checker = ttk.Button(self, text="Check AGS for errors", command=self.check_ags)
        self.button_ags_checker.pack(pady=8)
        self.button_ags_checker["state"] = "disabled"
        
        self.button_save_ags = ttk.Button(self, text="Save AGS file", command=self.save_ags)
        self.button_save_ags.pack(pady=8)
        self.button_save_ags["state"] = "disabled"
        
        # This holds the file location
        self.file_location = ''
        self.tables = None
        self.headings = None
        self.gui = None
        
    def get_ags_file_location(self):
        self.file_location = filedialog.askopenfilename(filetypes=[('AGS Files', '*.ags')])
        
        # do nothing if no file was selected
        if self.file_location == '':
            return
        
        print(f"Opening {self.file_location}...")
        self.tables, self.headings = AGS4.AGS4_to_dataframe(self.file_location)
        
        #Now a file is opened, enable buttons:
        self.button_showinfo["state"] = "enabled"
        self.button_ags_checker["state"] = "enabled"
        
        
    def start_pandasgui(self):
        #save ags button can be enabled once the pandasgui is created
        self.button_save_ags["state"] = "enabled"
        self.gui = show(**self.tables)
        
        
    def check_ags(self):
        
        try:
            errors = AGS4.check_file(self.file_location)
        except ValueError as e:
            print(f'AGS Checker ended unexpectedly: {e}')
            return
            
        if not errors:
            print("No errors found. Yay.")
            return
        
        for rule, items in errors.items():
            for error in items:
                print(f"Error in line: {error['line']}, group: {error['group']}, description: {error['desc']}")
            
        
    def save_ags(self):
        self._disable_buttons
        newFileName = filedialog.asksaveasfilename(filetypes=[('AGS Files', '*.ags')])
        updated_tables = self.gui.get_dataframes()
        AGS4.dataframe_to_AGS4(updated_tables, self.headings, newFileName)
        print('Done.')
        self._enable_buttons
        
    def _disable_buttons(self):
        self.button_open["state"] = "disabled"
        self.button_showinfo["state"] = "disabled"
        self.button_ags_checker["state"] = "disabled"
        self.button_save_ags["state"] = "disabled"
        
    def _enable_buttons(self):
        self.button_open["state"] = "enabled"
        self.button_showinfo["state"] = "enabled"
        self.button_ags_checker["state"] = "enabled"
        self.button_save_ags["state"] = "enabled"

root = tk.Tk()
app = Application(root)
root.mainloop()