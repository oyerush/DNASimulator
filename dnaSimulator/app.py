import os

from PySide2 import QtGui, QtWidgets
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
        self.browse_PushButton.clicked.connect(self.openFileDialog)
        self.set_current_values_PushButton.clicked.connect(self.setErrorValues)
        self.run_error_simulator_PushButton.clicked.connect(self.runErrorSimulator)
        self.Ilumina_miSeq_radioButton.clicked.connect(self.ilumina_miSeq_chosen)
        self.Ilumina_NextSeq_radioButton.clicked.connect(self.ilumina_NextSeq_chosen)
        self.MinION_radioButton.clicked.connect(self.MinIon_chosen)

    def MinIon_chosen(self):
        self.twist_bioscience_radioButton.setEnabled(False)
        self.twist_bioscience_radioButton.setAutoExclusive(False)
        self.twist_bioscience_radioButton.setChecked(False)
        self.twist_bioscience_radioButton.setAutoExclusive(True)
        self.customArray_radioButton.setEnabled(False)
        self.customArray_radioButton.setAutoExclusive(False)
        self.customArray_radioButton.setChecked(False)
        self.customArray_radioButton.setAutoExclusive(True)
        self.IDT_radioButton.setEnabled(True)
        self.IDT_radioButton.setChecked(True)

    def ilumina_NextSeq_chosen(self):
        self.twist_bioscience_radioButton.setEnabled(True)
        self.twist_bioscience_radioButton.setChecked(True)
        self.customArray_radioButton.setEnabled(False)
        self.customArray_radioButton.setAutoExclusive(False)
        self.customArray_radioButton.setChecked(False)
        self.customArray_radioButton.setAutoExclusive(True)
        self.IDT_radioButton.setEnabled(False)
        self.IDT_radioButton.setAutoExclusive(False)
        self.IDT_radioButton.setChecked(False)
        self.IDT_radioButton.setAutoExclusive(True)

    def ilumina_miSeq_chosen(self):
        self.twist_bioscience_radioButton.setEnabled(True)
        self.customArray_radioButton.setEnabled(True)
        self.IDT_radioButton.setEnabled(False)
        self.IDT_radioButton.setAutoExclusive(False)
        self.IDT_radioButton.setChecked(False)
        self.IDT_radioButton.setAutoExclusive(True)
        self.twist_bioscience_radioButton.setAutoExclusive(False)
        self.twist_bioscience_radioButton.setChecked(False)
        self.twist_bioscience_radioButton.setAutoExclusive(True)

    def openFileDialog(self):
        self.inputDNAPath, _ = QFileDialog.getOpenFileName(self, "Select an input file", './', filter="*.txt")
        self.file_path_lineEdit.setText(self.inputDNAPath)

    def setErrorValues(self):
        self.sub_value = self.substitution_lineEdit.toPlainText()
        self.insertion_value = self.insertion_lineEdit.toPlainText()
        self.one_base_del = self.one_base_del_lineEdit.toPlainText()
        self.log_del = self.long_del_lineEdit.toPlainText()
        # print(self.sub_value + ', ' + self.insertion_value + ', ' + self.one_base_del + ', ' + self.log_del)

    def show_error_dialog(self, error_type):
        if(error_type == 'no_such_file'):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setText("The input file you chosen doesn't exist")
            # msg.setInformativeText("This is additional information")
            msg.setWindowTitle("Error!")
            # msg.setDetailedText("The details are as follows:")
            msg.setStandardButtons(QMessageBox.Ok)
            # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            # msg.buttonClicked.connect(msgbtn)

            retval = msg.exec_()

    def runErrorSimulator(self):
        self.inputDNAPath = self.file_path_lineEdit.text()
        while True:
            if not os.path.isfile(self.inputDNAPath):
                print('The chosen input file doesn\'t exist')
                self.show_error_dialog('no_such_file')
                break
            else:
                break


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    dnaSimulator = dnaSimulator()
    dnaSimulator.show()
    # Run the main Qt loop
    sys.exit(app.exec_())