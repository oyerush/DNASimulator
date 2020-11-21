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
        self.one_base_del_value = 0
        self.log_del_value = 0

        # connect push buttons to an event
        self.browse_PushButton.clicked.connect(self.openFileDialog)
        # self.set_current_values_PushButton.clicked.connect(self.setErrorValues)
        self.run_error_simulator_PushButton.clicked.connect(self.runErrorSimulator)

        # connect radio buttons to an event
        self.Ilumina_miSeq_radioButton.toggled.connect(self.ilumina_miSeq_chosen)
        self.Ilumina_NextSeq_radioButton.toggled.connect(self.ilumina_NextSeq_chosen)
        self.MinION_radioButton.toggled.connect(self.MinIon_chosen)
        self.twist_bioscience_radioButton.toggled.connect(self.twist_bioscience_chosen)
        self.customArray_radioButton.toggled.connect(self.customArray_chosen)
        self.IDT_radioButton.toggled.connect(self.IDT_chosen)

        # connect the lineEdits of general errors
        self.substitution_lineEdit.textChanged.connect(self.set_substitution)
        self.insertion_lineEdit.textChanged.connect(self.set_insertion)
        self.one_base_del_lineEdit.textChanged.connect(self.set_one_base_del)
        self.long_del_lineEdit.textChanged.connect(self.set_long_del)

    def set_substitution(self, sub_value):
        self.sub_value = sub_value

    def set_insertion(self, insertion_value):
        self.insertion_value = insertion_value

    def set_one_base_del(self, one_base_del_value):
        self.one_base_del_value = one_base_del_value

    def set_long_del(self, log_del_value):
        self.log_del_value = log_del_value

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
        # self.IDT_radioButton.setChecked(True)

    def ilumina_NextSeq_chosen(self):
        self.twist_bioscience_radioButton.setEnabled(True)
        # self.twist_bioscience_radioButton.setChecked(True)
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

    def twist_bioscience_chosen(self):
        if self.Ilumina_miSeq_radioButton.isChecked() and self.twist_bioscience_radioButton.isChecked():
            self.set_EZ17_values()
        elif self.Ilumina_NextSeq_radioButton.isChecked() and self.twist_bioscience_radioButton.isChecked():
            self.set_O17_values()

    def customArray_chosen(self):
        if self.Ilumina_miSeq_radioButton.isChecked() and self.customArray_radioButton.isChecked():
            self.set_G15_values()

    def IDT_chosen(self):
        if self.MinION_radioButton.isChecked() and self.IDT_radioButton.isChecked():
            self.set_Y16_values()

    def set_EZ17_values(self):
        self.substitution_lineEdit.setText('1.32E-03')
        self.insertion_lineEdit.setText('5.81E-04')
        self.one_base_del_lineEdit.setText('9.58E-04')
        self.long_del_lineEdit.setText('2.33E-04')

    def set_O17_values(self):
        self.substitution_lineEdit.setText('7.09E-03')
        self.insertion_lineEdit.setText('4.14E-03')
        self.one_base_del_lineEdit.setText('2.77E-03')
        self.long_del_lineEdit.setText('4.79E-04')

    def set_G15_values(self):
        self.substitution_lineEdit.setText('5.84E-03')
        self.insertion_lineEdit.setText('8.57E-04')
        self.one_base_del_lineEdit.setText('5.37E-03')
        self.long_del_lineEdit.setText('3.48E-04')

    def set_Y16_values(self):
        self.substitution_lineEdit.setText('1.21E-01')
        self.insertion_lineEdit.setText('3.67E-01')
        self.one_base_del_lineEdit.setText('4.33E-02')
        self.long_del_lineEdit.setText('1.87E-02')

    def openFileDialog(self):
        self.inputDNAPath, _ = QFileDialog.getOpenFileName(self, "Select an input file", './', filter="*.txt")
        self.file_path_lineEdit.setText(self.inputDNAPath)

    # def setErrorValues(self):
    #     self.sub_value = self.substitution_lineEdit.text()
    #     self.insertion_value = self.insertion_lineEdit.text()
    #     self.one_base_del_value = self.one_base_del_lineEdit.text()
    #     self.log_del_value = self.long_del_lineEdit.text()
    #     # print(self.sub_value + ', ' + self.insertion_value + ', ' + self.one_base_del + ', ' + self.log_del)

    def show_error_dialog(self, error_type):
        if (error_type == 'no_such_file'):
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
