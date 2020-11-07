from PySide2 import QtGui
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys

import dnaSimulator_ui



class dnaSimulator(QMainWindow, dnaSimulator_ui.Ui_dnaSimulator):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.inputDNAPath = ""
        # self.filePath_textEdit.setPlainText("check check")
        self.browse_PushButton.clicked.connect(self.openFileDialog)

    def openFileDialog(self):
        self.inputDNAPath = QFileDialog.getOpenFileName()
        self.filePath_textEdit.setPlainText(self.inputDNAPath[0])


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    dnaSimulator = dnaSimulator()
    dnaSimulator.show()
    # Run the main Qt loop
    sys.exit(app.exec_())