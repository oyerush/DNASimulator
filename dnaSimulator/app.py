import os
import subprocess
import time

from PySide2 import QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import sys
import platform

import dnaSimulator_ui
from simulator import *


class dnaSimulator(QMainWindow, dnaSimulator_ui.Ui_dnaSimulator):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.inputDNAPath = ""

        # initialize general errors
        self.general_errors = {
            'd': '',
            'ld': '',
            'i': '',
            's': ''
        }

        # initialize per-base errors
        self.per_base_errors = {
            'A': {'s': '', 'i': '', 'pi': '', 'd': '', 'ld': ''},
            'C': {'s': '', 'i': '', 'pi': '', 'd': '', 'ld': ''},
            'G': {'s': '', 'i': '', 'pi': '', 'd': 'test', 'ld': ''},
            'T': {'s': '', 'i': '', 'pi': '', 'd': '', 'ld': ''}
        }

        self.progressBar.setVisible(False)

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

        # connect the lineEdits of per base errors
        self.A_substitution_lineEdit.textChanged.connect(self.set_A_substitution)
        self.C_substitution_lineEdit.textChanged.connect(self.set_C_substitution)
        self.G_substitution_lineEdit.textChanged.connect(self.set_G_substitution)
        self.T_substitution_lineEdit.textChanged.connect(self.set_T_substitution)

        self.A_insertion_lineEdit.textChanged.connect(self.set_A_insertion)
        self.C_insertion_lineEdit.textChanged.connect(self.set_C_insertion)
        self.G_insertion_lineEdit.textChanged.connect(self.set_G_insertion)
        self.T_insertion_lineEdit.textChanged.connect(self.set_T_insertion)

        self.A_pre_insertion_lineEdit.textChanged.connect(self.set_A_pre_insertion)
        self.C_pre_insertion_lineEdit.textChanged.connect(self.set_C_pre_insertion)
        self.G_pre_insertion_lineEdit.textChanged.connect(self.set_G_pre_insertion)
        self.T_pre_insertion_lineEdit.textChanged.connect(self.set_T_pre_insertion)

        self.A_one_base_del_lineEdit.textChanged.connect(self.set_A_one_base_del)
        self.C_one_base_del_lineEdit.textChanged.connect(self.set_C_one_base_del)
        self.G_one_base_del_lineEdit.textChanged.connect(self.set_G_one_base_del)
        self.T_one_base_del_lineEdit.textChanged.connect(self.set_T_one_base_del)

        self.A_long_del_lineEdit.textChanged.connect(self.set_A_long_del)
        self.C_long_del_lineEdit.textChanged.connect(self.set_C_long_del)
        self.G_long_del_lineEdit.textChanged.connect(self.set_G_long_del)
        self.T_long_del_lineEdit.textChanged.connect(self.set_T_long_del)

    def set_substitution(self, value):
        self.general_errors['s'] = value

    def set_insertion(self, value):
        self.general_errors['i'] = value

    def set_one_base_del(self, value):
        self.general_errors['d'] = value

    def set_long_del(self, value):
        self.general_errors['ld'] = value

    def set_A_substitution(self, value):
        self.per_base_errors['A']['s'] = value

    def set_C_substitution(self, value):
        self.per_base_errors['C']['s'] = value

    def set_G_substitution(self, value):
        self.per_base_errors['G']['s'] = value

    def set_T_substitution(self, value):
        self.per_base_errors['T']['s'] = value

    def set_A_insertion(self, value):
        self.per_base_errors['A']['i'] = value

    def set_C_insertion(self, value):
        self.per_base_errors['C']['i'] = value

    def set_G_insertion(self, value):
        self.per_base_errors['G']['i'] = value

    def set_T_insertion(self, value):
        self.per_base_errors['T']['i'] = value

    def set_A_pre_insertion(self, value):
        self.per_base_errors['A']['pi'] = value

    def set_C_pre_insertion(self, value):
        self.per_base_errors['C']['pi'] = value

    def set_G_pre_insertion(self, value):
        self.per_base_errors['G']['pi'] = value

    def set_T_pre_insertion(self, value):
        self.per_base_errors['T']['pi'] = value

    def set_A_one_base_del(self, value):
        self.per_base_errors['A']['d'] = value

    def set_C_one_base_del(self, value):
        self.per_base_errors['C']['d'] = value

    def set_G_one_base_del(self, value):
        self.per_base_errors['G']['d'] = value

    def set_T_one_base_del(self, value):
        self.per_base_errors['T']['d'] = value

    def set_A_long_del(self, value):
        self.per_base_errors['A']['ld'] = value

    def set_C_long_del(self, value):
        self.per_base_errors['C']['ld'] = value

    def set_G_long_del(self, value):
        self.per_base_errors['G']['ld'] = value

    def set_T_long_del(self, value):
        self.per_base_errors['T']['ld'] = value

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

    def set_per_base_substitution(self, a, c, g, t):
        self.A_substitution_lineEdit.setText(a)
        self.C_substitution_lineEdit.setText(c)
        self.G_substitution_lineEdit.setText(g)
        self.T_substitution_lineEdit.setText(t)

    def set_per_base_insertion(self, a, c, g, t):
        self.A_insertion_lineEdit.setText(a)
        self.C_insertion_lineEdit.setText(c)
        self.G_insertion_lineEdit.setText(g)
        self.T_insertion_lineEdit.setText(t)

    def set_per_base_pre_insertion(self, a, c, g, t):
        self.A_pre_insertion_lineEdit.setText(a)
        self.C_pre_insertion_lineEdit.setText(c)
        self.G_pre_insertion_lineEdit.setText(g)
        self.T_pre_insertion_lineEdit.setText(t)

    def set_per_base_del(self, a, c, g, t):
        self.A_one_base_del_lineEdit.setText(a)
        self.C_one_base_del_lineEdit.setText(c)
        self.G_one_base_del_lineEdit.setText(g)
        self.T_one_base_del_lineEdit.setText(t)

    def set_per_base_long_del(self, a, c, g, t):
        self.A_long_del_lineEdit.setText(a)
        self.C_long_del_lineEdit.setText(c)
        self.G_long_del_lineEdit.setText(g)
        self.T_long_del_lineEdit.setText(t)

    def set_EZ17_values(self):
        # general errors
        self.substitution_lineEdit.setText('1.32E-03')
        self.insertion_lineEdit.setText('5.81E-04')
        self.one_base_del_lineEdit.setText('9.58E-04')
        self.long_del_lineEdit.setText('2.33E-04')

        # per base errors
        self.set_per_base_substitution('0.00135', '0.00135', '0.00126', '0.00132')
        self.set_per_base_insertion('0.00057', '0.00059', '0.00059', '0.00058')
        self.set_per_base_pre_insertion('0.00059', '0.00058', '0.00057', '0.00058')
        self.set_per_base_del('0.00099', '0.00098', '0.00094', '0.00096')
        self.set_per_base_long_del('0.00024', '0.00023', '0.00023', '0.00023')

    def set_O17_values(self):
        # general errors
        self.substitution_lineEdit.setText('7.09E-03')
        self.insertion_lineEdit.setText('4.14E-03')
        self.one_base_del_lineEdit.setText('2.77E-03')
        self.long_del_lineEdit.setText('4.79E-04')

        # per base errors
        self.set_per_base_substitution('0.00724', '0.00701', '0.00706', '0.00704')
        self.set_per_base_insertion('0.00411', '0.00415', '0.00415', '0.00413')
        self.set_per_base_pre_insertion('0.00429', '0.00415', '0.00403', '0.00408')
        self.set_per_base_del('0.00289', '0.00279', '0.00276', '0.0028')
        self.set_per_base_long_del('0.00048', '0.00048', '0.00047', '0.00049')

    def set_G15_values(self):
        # general errors
        self.substitution_lineEdit.setText('5.84E-03')
        self.insertion_lineEdit.setText('8.57E-04')
        self.one_base_del_lineEdit.setText('5.37E-03')
        self.long_del_lineEdit.setText('3.48E-04')

        # per base errors
        self.set_per_base_substitution('0.00605', '0.00563', '0.00577', '0.00591')
        self.set_per_base_insertion('0.0009', '0.00083', '0.00085', '0.00084')
        self.set_per_base_pre_insertion('0.00092', '0.00081', '0.00087', '0.00084')
        self.set_per_base_del('0.00543', '0.00513', '0.00539', '0.00559')
        self.set_per_base_long_del('0.00036', '0.00034', '0.00034', '0.00036')

    def set_Y16_values(self):
        # general errors
        self.substitution_lineEdit.setText('1.21E-01')
        self.insertion_lineEdit.setText('3.67E-01')
        self.one_base_del_lineEdit.setText('4.33E-02')
        self.long_del_lineEdit.setText('1.87E-02')

        # per base errors
        self.set_per_base_substitution('0.119', '0.133', '0.112', '0.119')
        self.set_per_base_insertion('0.331', '0.406', '0.361', '0.367')
        self.set_per_base_pre_insertion('0.332', '0.408', '0.341', '0.382')
        self.set_per_base_del('0.044', '0.048', '0.040', '0.041')
        self.set_per_base_long_del('0.019', '0.021', '0.017', '0.018')

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

    def report_func(self, total_lines, curr_line):
        percent = int(curr_line * 100 // total_lines)
        self.progressBar.setValue(percent+1)
        # print('total: ' + str(total_lines) + 'curr: ' + str(curr_line))
        if percent+1 == 99:
            self.label_progress.setText('Running reconstruction, please wait!')

    def runErrorSimulator(self):
        self.inputDNAPath = self.file_path_lineEdit.text()
        while True:
            if not os.path.isfile(self.inputDNAPath):
                print('The chosen input file doesn\'t exist')
                self.show_error_dialog('no_such_file')
                self.file_path_lineEdit.clear()
                break
            else:
                error_sim = Simulator(self.general_errors, self.per_base_errors, self.inputDNAPath)
                self.progressBar.setVisible(True)
                self.label_progress.setText('Injecting errors, please wait!')
                error_sim.simulate_errors(self.report_func)
                # os.system('hyb.exe')
                self.progressBar.setValue(0)
                if platform.system() == "Linux" or platform == "linux2":
                    # linux
                    pass
                elif platform.system() == "Darwin":
                    # OS X
                    subprocess.run('./reconstruction_algs/DNA')
                elif platform.system() == "Windows":
                    # Windows...
                    # os.system('hyb.exe')
                    subprocess.run('reconstruction_algs/hyb.exe')
                self.label_progress.setText('We are done :)')
                self.progressBar.setValue(100)
                self.progressBar.setVisible(False)
                break



if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    dnaSimulator = dnaSimulator()
    dnaSimulator.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
