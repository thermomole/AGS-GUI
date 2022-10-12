import tkinter as tk
from tkinter import *
from tkinter import filedialog, Listbox, ttk, scrolledtext
from python_ags4 import AGS4
from pandasgui import show
import pandas as pd
import customtkinter as ct

class Application(ct.CTkFrame):

    ct.set_appearance_mode("system")
    ct.set_default_color_theme("dark-blue")

    def __init__(self, master):
        ct.CTkFrame.__init__(self, master, corner_radius=15, fg_color="#f0f0f0")

        root.iconphoto(False, tk.PhotoImage(file='images/geo.png'))
        master.geometry('375x300')
        master.title("AGS Tool")
        
        self.button_open = ct.CTkButton(self, text="Open File...", command=self.get_ags_file_location, fg_color="#2b4768", 
        corner_radius=10, hover_color="#6bb7dd", text_color="#FFFFFF", text_color_disabled="#999999", text_font=("Tahoma",9))
        self.button_open.pack(pady=8, padx=8)

        self.button_showinfo = ct.CTkButton(self, text="View Data", command=self.start_pandasgui, 
        corner_radius=10, fg_color="#2b4768", hover_color="#6bb7dd", text_color="#FFFFFF", text_color_disabled="#999999", text_font=("Tahoma",9))
        self.button_showinfo.pack(pady=8)
        self.button_showinfo.configure(state=tk.DISABLED)

        self.button_count_results = ct.CTkButton(self, text="Count Lab Results", command=self.count_lab_results, 
        corner_radius=10, fg_color="#2b4768", hover_color="#6bb7dd", text_color="#FFFFFF", text_color_disabled="#999999", text_font=("Tahoma",9))
        self.button_count_results.pack(pady=8)
        self.button_count_results.configure(state=tk.DISABLED)
        
        self.button_ags_checker = ct.CTkButton(self, text="Check AGS for errors", command=self.check_ags, 
        corner_radius=10, fg_color="#2b4768", hover_color="#6bb7dd", text_color="#FFFFFF", text_color_disabled="#999999", text_font=("Tahoma",9))
        self.button_ags_checker.pack(pady=8)
        self.button_ags_checker.configure(state=tk.DISABLED)
        
        self.button_save_ags = ct.CTkButton(self, text="Save AGS file", command=self.save_ags, 
        corner_radius=10, fg_color="#2b4768", hover_color="#6bb7dd", text_color="#FFFFFF", text_color_disabled="#999999", text_font=("Tahoma",9))
        self.button_save_ags.pack(pady=8)
        self.button_save_ags.configure(state=tk.DISABLED)
    
        self.text = tk.StringVar()
        self.text.set("Open an AGS file and choose what to do...")
        self.greeting = ct.CTkLabel(textvariable=self.text, text_font=("Tahoma",9))
        self.greeting.pack(pady=10)

        self.pack(padx=12,pady=2)

        '''This holds the file location'''
        self.file_location = ''
        self.temp_file_name = ''
        self.tables = None
        self.headings = None
        self.gui = None
        self.box = False
        self.dict_fix = False    
        self.result_list = []
        self.error_list = []
        self.export = False

    def get_ags_file_location(self):
        app.master.geometry('375x300')
        self.text.set("Open an AGS file and choose what to do...")
        if self.box == True:
            self.listbox.pack_forget()
            self.button_export_results.pack_forget()
            self.box = False
        if self.dict_fix == True:
            self.button_fix_dict.pack_forget()
            self.dict_fix = False
        if self.export == True:
            self.button_export_error.pack_forget()
            self.export = False

        self.file_location = filedialog.askopenfilename(filetypes=[('AGS Files', '*.ags')])
        
        '''do nothing if no file was selected'''
        if self.file_location == '':
            self.text.set('''No AGS file selected!
Please select an AGS with "Open File..."''')
            print("No AGS file selected! Please select an AGS with 'Open File...'")
            self.button_ags_checker.configure(state=tk.DISABLED)
            return

        self.text.set("AGS file loaded successfully.")
        print(f"Opening {self.file_location}...")
        self.tables, self.headings = AGS4.AGS4_to_dataframe(self.file_location)
        print(f"...done.")

        '''Now a file is opened, enable buttons:'''
        self.button_showinfo.configure(state=tk.NORMAL)
        self.button_ags_checker.configure(state=tk.NORMAL)
        self.button_count_results.configure(state=tk.NORMAL)


    def count_lab_results(self):
        if self.dict_fix == True:
            self.button_fix_dict.pack_forget()
            self.dict_fix = False

        if self.export == True:
            self.button_export_error.pack_forget()
            self.export = False

        table_name = [
            'TRIG',
            'LNMC',
            'LDEN',
            'GRAT',
            'CONG',
            'LDYN',
            'LLPL',
            'LPDN',
            'LPEN',
            'LRES',
            'LTCH',
            'LVAN',
            'RELD',
            'SHBG',
            'TREG',
            'DSSG',
            'IRSG',
            'PTST',
            'GCHM',
            'RESG',
            ]

        all_results = []
        error_tables = []

        for x in table_name:
            table = x

            try:
                location = list(self.tables[x]['LOCA_ID'])
                samp_id = list(self.tables[x]['SAMP_ID'])
                samp_ref = list(self.tables[x]['SPEC_REF'])
                samp_depth = list(self.tables[x]['SPEC_DPTH'])
                test_type = ""
                if x.__contains__('GCHM'):
                    test_type = list(self.tables[x]['GCHM_CODE'])
                    test_type.pop(0)
                    test_type.pop(0)
                    test_type_df = pd.DataFrame.from_dict(test_type)
                elif x.__contains__('TRIG'):
                    test_type = list(self.tables[x]['TRIG_COND'])
                    test_type.pop(0)
                    test_type.pop(0)
                    test_type_df = pd.DataFrame.from_dict(test_type)
                elif x.__contains__('CONG'):
                    test_type = list(self.tables[x]['CONG_TYPE'])
                    test_type.pop(0)
                    test_type.pop(0)
                    test_type_df = pd.DataFrame.from_dict(test_type)
                elif x.__contains__('TREG'):
                    test_type = list(self.tables[x]['TREG_TYPE'])
                    test_type.pop(0)
                    test_type.pop(0)
                    test_type_df = pd.DataFrame.from_dict(test_type)
                elif x.__contains__('GRAT'):
                    test_type = list(self.tables[x]['GRAT_TYPE'])
                    samp_with_table = list(zip(location,samp_id,samp_ref,samp_depth,test_type))
                    samp_with_table.pop(0)
                    samp_with_table.pop(0)
                    result_table = pd.DataFrame.from_dict(samp_with_table)
                    result_table.drop_duplicates(inplace=True)
                    result_table.columns = ['POINT','ID','REF','DEPTH','TYPE']
                    tt = result_table['TYPE'].to_list()
                    test_type_df = pd.DataFrame.from_dict(tt)

                if not test_type == "":
                    num_test = test_type_df.value_counts()
                    test_counts = pd.DataFrame(num_test)
                    head = []
                    val = []
                    for y in test_counts.index.tolist():
                        head.append(y[0])
                    for z in test_counts.values.tolist():
                        val.append(z)
                    count = list(zip(head,val))
                else:
                    count = str(len(samp_id) - 2)
                type_list = []
                type_list.append(str(table))
                type_list.append(count)
                all_results.append(type_list)
                print(str(table) + " - " + str(type_list))

            except Exception as e:
                error_tables.append(str(e))

        print("Table(s) not found: " + str(error_tables))

        result_list = pd.DataFrame.from_dict(all_results, orient='columns')
        self.result_list = result_list

        if self.box == False:
            self.listbox = scrolledtext.ScrolledText(self, height=10, font=("Tahoma",9))
            result_list.index.name = ' '
            app.master.geometry('430x475')
            self.listbox.tag_configure('tl', justify='left')
            self.listbox.insert('end', result_list, 'tl')
            self.listbox.delete(1.0,3.0)
            self.listbox.pack(padx=20)
            self.box = True

            self.button_export_results = ct.CTkButton(self, text="Export Results List", command=self.export_results, 
            corner_radius=10, fg_color="#2b4768", hover_color="#6bb7dd", text_color="#FFFFFF", text_color_disabled="#999999", text_font=("Tahoma",9))
            self.button_export_results.pack(pady=(8,8))

            self.text.set("Results list ready to export.")
        else:
            app.master.geometry('430x475')
            self.listbox.pack(padx=20)
            pass
        
    def export_results(self):
        self.path_directory = filedialog.asksaveasfilename(filetypes=[('CSV Files', '*.csv')],defaultextension="*.csv")
        if not self.path_directory:
            return
        self.result_list.to_csv(self.path_directory, index=False, index_label=False, header=None)
        print("File saved in: " + str(self.path_directory))

    def start_pandasgui(self):
        '''save ags button can be enabled once the pandasgui is created'''
        app.master.geometry('375x300')
        self.text.set("Pandas GUI is opening, please wait...")
        if self.box == True:
            self.listbox.pack_forget()
            self.button_export_results.pack_forget()
            self.box = False
        if self.export == True:
            self.button_export_error.pack_forget()
            self.export = False
        root.update()
        
        self.button_save_ags.configure(state=tk.NORMAL)
        self.gui = show(**self.tables)
        self.text.set("You can now save the edited AGS.")
        root.update()
        
    def check_ags(self):
        app.master.geometry('375x300')
        if self.dict_fix == True:
            self.button_fix_dict.pack_forget()
            self.dict_fix = False
        if self.dict_fix == True and not self.temp_file_name == '':
            self.button_fix_dict.pack_forget()
            self.dict_fix = False
        if self.box == True:
            self.listbox.pack_forget()
            self.button_export_results.pack_forget()
            self.box = False
        if self.export == True:
            self.button_export_error.pack_forget()
            self.export = False
        self.text.set("Checking AGS for errors...")
        root.update()

        #self.tables['DICT']['DICT_STAT'].replace(to_replace="REQUIRED",value="KEY", inplace=True)

        try:
            if not self.file_location == '' and self.temp_file_name == '':
                errors = AGS4.check_file(self.file_location)
            elif not self.temp_file_name == '':
                errors = AGS4.check_file(self.temp_file_name)
            else:
                if self.file_location == '':
                    self.text.set('''No AGS file selected!
Please select an AGS with "Open File..."''')
                    print("No AGS file selected! Please select an AGS with 'Open File...'")
                    self.button_ags_checker.configure(state=tk.DISABLED)
                elif self.temp_file_name == '':
                    self.text.set('''No AGS file selected!
Please select an AGS with "Open File..."''')
                    print("No AGS file selected! Please select an AGS with 'Open File...'")
                    self.button_ags_checker.configure(state=tk.DISABLED)
                else:
                    errors = AGS4.check_file(self.file_location)
                    
        except ValueError as e:
            print(f'AGS Checker ended unexpectedly: {e}')
            app.master.geometry('375x400')
            self.text.set('''Something went wrong.
Make sure there are "key" fields in the dictionary!
Save a new AGS file with a fixed dictionary 
by pressing "Fix DICT errors".''')
            self.button_fix_dict = ct.CTkButton(self, text="Fix DICT errors", command=self.fix_dict, 
            corner_radius=10, fg_color="#2b4768", hover_color="#6bb7dd", text_color="#FFFFFF", text_color_disabled="#999999", text_font=("Tahoma",9))
            self.button_fix_dict.pack(pady=(8,8))
            self.dict_fix = True
            return
        
        if not errors:
            print("No errors found. Yay.")
            self.text.set("AGS file contains no errors!")
            root.update()
            return
        
        for rule, items in errors.items():
            if rule == 'Metadata':
                print('Metadata')
                for msg in items:
                    print(f"{msg['line']}: {msg['desc']}")
                continue
                    
            for error in items:
                self.text.set("Error(s) found, check output or click 'Export Error Log'.")
                root.update()
                print(f"Error in line: {error['line']}, group: {error['group']}, description: {error['desc']}")
                self.error_list.append(f"Error in line: {error['line']}, group: {error['group']}, description: {error['desc']}")

        if errors:
            app.master.geometry('375x340')
            self.button_export_error = ct.CTkButton(self, text="Export Error Log", command=self.export_errors, 
            corner_radius=10, fg_color="#2b4768", hover_color="#6bb7dd", text_color="#FFFFFF", text_color_disabled="#999999", text_font=("Tahoma",9))
            self.button_export_error.pack(pady=(8,8))
            self.export = True


    def export_errors(self):
        self.log_path = filedialog.asksaveasfilename(filetypes=[('Text Files', '*.txt')],defaultextension="*.txt")
        if self.log_path == '':
            return
        with open(self.log_path, "w") as f:
            for item in self.error_list:
                f.write("%s\n" % item)

    def fix_dict(self):
        self.tables['DICT']['DICT_STAT'].replace(to_replace="REQUIRED",value="KEY", inplace=True)
        self._disable_buttons
        self.temp_file_name = filedialog.asksaveasfilename(filetypes=[('AGS Files', '*.ags')],defaultextension="*.ags")
        if self.temp_file_name == "":
            self.dict_fix = False
            self.button_fix_dict.pack_forget()
            app.master.geometry('375x300')
            self.text.set("Open an AGS file and choose what to do...")
            root.update()
            self.check_ags()
            return
        AGS4.dataframe_to_AGS4(self.tables, self.headings, self.temp_file_name)
        print('Done.')
        self._enable_buttons
        self.dict_fix = False
        self.button_fix_dict.pack_forget()
        app.master.geometry('375x300')
        self.text.set("Try checking the file for errors again.")
        root.update()


    def save_ags(self):
        self._disable_buttons
        newFileName = filedialog.asksaveasfilename(filetypes=[('AGS Files', '*.ags')],defaultextension="*.ags")
        if not newFileName:
            return
        updated_tables = self.gui.get_dataframes()
        AGS4.dataframe_to_AGS4(updated_tables, self.headings, newFileName)
        self.tables, self.headings = AGS4.AGS4_to_dataframe(newFileName)
        print('Done.')
        self._enable_buttons
        
    def _disable_buttons(self):
        self.button_open.configure(state=tk.DISABLED)
        self.button_showinfo.configure(state=tk.DISABLED)
        self.button_ags_checker.configure(state=tk.DISABLED)
        self.button_save_ags.configure(state=tk.DISABLED)
        
    def _enable_buttons(self):
        self.button_open.configure(state=tk.NORMAL)
        self.button_showinfo.configure(state=tk.NORMAL)
        self.button_ags_checker.configure(state=tk.NORMAL)
        self.button_save_ags.configure(state=tk.NORMAL)

root = ct.CTk()
app = Application(root)
root.mainloop()
