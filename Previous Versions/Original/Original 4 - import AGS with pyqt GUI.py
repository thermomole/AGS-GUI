import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon
from python_ags4 import AGS4
from pandasgui import show

fileLocation = None

def make_ags():
    tables, headings = AGS4.AGS4_to_dataframe(fileLocation)
    print(fileLocation)

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Select AGS file'
        self.left = 20
        self.top = 20
        self.width = 640
        self.height = 480
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.openFileNameDialog()
        self.show()
    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"Select AGS file to open", "","AGS Files (*.ags)", options=options)
        if fileName:
            fileLocation = fileName
            print(fileName)
            app.quit
            make_ags()
            def open_gui():
                tables, headings = AGS4.AGS4_to_dataframe(fileName)
                gui = show(**tables)
            #open_gui()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

#list all headings
#for key, value in headings.items() :
    #print(key, ':', value)

#list all tables
#for key, value in tables.items() :
    #print(key, ':', value)

#print field within table
#print(tables["GEOL"]['GEOL_DESC'])

#open window to display all tables and headings in a gINT style user interface
#from pandasgui import show
#tables, headings = AGS4.AGS4_to_dataframe(R'C:\Users\DataEntry1\OneDrive - Geoquip Marine Operations AG\Desktop\AGS\AGS.AGS')
#gui = show(**tables)
