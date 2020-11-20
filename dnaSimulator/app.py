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
        self.sub_value = 0
        self.insertion_value = 0
        self.one_base_del = 0
        self.log_del = 0
        # self.filePath_textEdit.setPlainText("check check")
        self.browse_PushButton.clicked.connect(self.openFileDialog)
        self.set_current_values_PushButton.clicked.connect(self.setErrorValues)
        self.run_error_simulator_PushButton.clicked.connect(self.runErrorSimulator)

    def openFileDialog(self):
        self.inputDNAPath, _ = QFileDialog.getOpenFileName(self, "Select an input file", './', filter="*.txt")
        self.file_path_lineEdit.setPlainText(self.inputDNAPath)

    def setErrorValues(self):
        self.sub_value = self.substitution_lineEdit.toPlainText()
        self.insertion_value = self.insertion_lineEdit.toPlainText()
        self.one_base_del = self.one_base_del_lineEdit.toPlainText()
        self.log_del = self.long_del_lineEdit.toPlainText()
        # print(self.sub_value + ', ' + self.insertion_value + ', ' + self.one_base_del + ', ' + self.log_del)

    def runErrorSimulator(self):
        pass


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    dnaSimulator = dnaSimulator()
    dnaSimulator.show()
    # Run the main Qt loop
    sys.exit(app.exec_())