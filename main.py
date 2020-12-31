# This Python file uses the following encoding: utf-8
import sys
import os


from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import QFile
#from PyQt5.QtUiTools import QUiLoader
from PyQt5 import uic loadUi

class test(QWidget):
    def __init__(self):
        super(test, self).__init__()
        self.load_ui()
        self.hello()

    def load_ui(self):
        #loader = QUiLoader()
        loader = loadUi()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        loader.load(ui_file, self)
        ui_file.close()

    def hello(self):
        print("Window start")

if __name__ == "__main__":
    app = QApplication([])
    widget = test()
    widget.show()
    print("Hello world")
    sys.exit(app.exec_())

