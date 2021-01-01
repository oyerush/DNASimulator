import os
import subprocess
import time

from PySide2 import QtGui, QtWidgets
# from PySide2.QtCore import *
from PyQt5.QtCore import *
from PySide2.QtGui import *
# from PySide2.QtWidgets import *
from PyQt5.QtWidgets import *
import sys
import platform

import dnaSimulator_ui2
# from SpinBoxCustom import SpinBoxCustom
from simulator import *


class dnaSimulator(QMainWindow, dnaSimulator_ui2.Ui_dnaSimulator):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        # set the title
        self.setWindowTitle('DNA Simulator')

        self.inputDNAPath = ""
        # self.reconstruction_input_path =

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

        self.reconstruction_algo = ''

        self.progressBar.setVisible(False)

        # connect push buttons to an event
        self.browse_PushButton.clicked.connect(self.openFileDialog)
        # self.set_current_values_PushButton.clicked.connect(self.setErrorValues)
        self.run_error_simulator_PushButton.clicked.connect(self.runErrorSimulator)
        self.reconstruction_run_pushButton.clicked.connect(self.run_reconstruction_algo)

        # connect radio buttons to an event
        self.Ilumina_miSeq_radioButton.toggled.connect(self.ilumina_miSeq_chosen)
        self.Ilumina_NextSeq_radioButton.toggled.connect(self.ilumina_NextSeq_chosen)
        self.MinION_radioButton.toggled.connect(self.MinIon_chosen)
        self.twist_bioscience_radioButton.toggled.connect(self.twist_bioscience_chosen)
        self.customArray_radioButton.toggled.connect(self.customArray_chosen)
        self.IDT_radioButton.toggled.connect(self.IDT_chosen)

        self.substitution_doubleSpinBox.textChanged.connect(self.set_substitution)
        self.insertion_doubleSpinBox.textChanged.connect(self.set_insertion)
        self.one_base_del_doubleSpinBox.textChanged.connect(self.set_one_base_del)
        self.long_del_doubleSpinBox.textChanged.connect(self.set_long_del)

        # connect the lineEdits of per base errors
        self.A_substitution_doubleSpinBox.textChanged.connect(self.set_A_substitution)
        self.C_substitution_doubleSpinBox.textChanged.connect(self.set_C_substitution)
        self.G_substitution_doubleSpinBox.textChanged.connect(self.set_G_substitution)
        self.T_substitution_doubleSpinBox.textChanged.connect(self.set_T_substitution)

        self.A_insertion_doubleSpinBox.textChanged.connect(self.set_A_insertion)
        self.C_insertion_doubleSpinBox.textChanged.connect(self.set_C_insertion)
        self.G_insertion_doubleSpinBox.textChanged.connect(self.set_G_insertion)
        self.T_insertion_doubleSpinBox.textChanged.connect(self.set_T_insertion)

        self.A_pre_insertion_doubleSpinBox.textChanged.connect(self.set_A_pre_insertion)
        self.C_pre_insertion_doubleSpinBox.textChanged.connect(self.set_C_pre_insertion)
        self.G_pre_insertion_doubleSpinBox.textChanged.connect(self.set_G_pre_insertion)
        self.T_pre_insertion_doubleSpinBox.textChanged.connect(self.set_T_pre_insertion)

        self.A_one_base_del_doubleSpinBox.textChanged.connect(self.set_A_one_base_del)
        self.C_one_base_del_doubleSpinBox.textChanged.connect(self.set_C_one_base_del)
        self.G_one_base_del_doubleSpinBox.textChanged.connect(self.set_G_one_base_del)
        self.T_one_base_del_doubleSpinBox.textChanged.connect(self.set_T_one_base_del)

        self.A_long_del_doubleSpinBox.textChanged.connect(self.set_A_long_del)
        self.C_long_del_doubleSpinBox.textChanged.connect(self.set_C_long_del)
        self.G_long_del_doubleSpinBox.textChanged.connect(self.set_G_long_del)
        self.T_long_del_doubleSpinBox.textChanged.connect(self.set_T_long_del)

        self.reconstruction_listWidget.addItem('Hybrid Reconstruction Algorithm')
        self.reconstruction_listWidget.addItem('Divider BMA Reconstruction Algorithm')
        self.reconstruction_listWidget.addItem('BMA Look Ahead Reconstruction Algorithm')
        self.reconstruction_listWidget.addItem('Iterative Reconstruction Algorithm')
        self.reconstruction_listWidget.addItem('Not a real algo')

        self.reconstruction_listWidget.currentItemChanged.connect(self.set_reconstruction_algo)


    def set_reconstruction_algo(self):
        self.reconstruction_algo = self.reconstruction_listWidget.currentItem().text()
        print(self.reconstruction_algo)

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
        self.A_substitution_doubleSpinBox.setValue(a)
        self.C_substitution_doubleSpinBox.setValue(c)
        self.G_substitution_doubleSpinBox.setValue(g)
        self.T_substitution_doubleSpinBox.setValue(t)

    def set_per_base_insertion(self, a, c, g, t):
        self.A_insertion_doubleSpinBox.setValue(a)
        self.C_insertion_doubleSpinBox.setValue(c)
        self.G_insertion_doubleSpinBox.setValue(g)
        self.T_insertion_doubleSpinBox.setValue(t)

    def set_per_base_pre_insertion(self, a, c, g, t):
        self.A_pre_insertion_doubleSpinBox.setValue(a)
        self.C_pre_insertion_doubleSpinBox.setValue(c)
        self.G_pre_insertion_doubleSpinBox.setValue(g)
        self.T_pre_insertion_doubleSpinBox.setValue(t)

    def set_per_base_del(self, a, c, g, t):
        self.A_one_base_del_doubleSpinBox.setValue(a)
        self.C_one_base_del_doubleSpinBox.setValue(c)
        self.G_one_base_del_doubleSpinBox.setValue(g)
        self.T_one_base_del_doubleSpinBox.setValue(t)

    def set_per_base_long_del(self, a, c, g, t):
        self.A_long_del_doubleSpinBox.setValue(a)
        self.C_long_del_doubleSpinBox.setValue(c)
        self.G_long_del_doubleSpinBox.setValue(g)
        self.T_long_del_doubleSpinBox.setValue(t)

    def set_EZ17_values(self):
        # general errors
        self.substitution_doubleSpinBox.setValue(1.32e-03)
        self.insertion_doubleSpinBox.setValue(5.81e-04)
        self.one_base_del_doubleSpinBox.setValue(9.58e-04)
        self.long_del_doubleSpinBox.setValue(2.33e-04)

        # per base errors
        self.set_per_base_substitution(0.00135, 0.00135, 0.00126, 0.00132)
        self.set_per_base_insertion(0.00057, 0.00059, 0.00059, 0.00058)
        self.set_per_base_pre_insertion(0.00059, 0.00058, 0.00057, 0.00058)
        self.set_per_base_del(0.00099, 0.00098, 0.00094, 0.00096)
        self.set_per_base_long_del(0.00024, 0.00023, 0.00023, 0.00023)

    def set_O17_values(self):
        # general errors
        self.substitution_doubleSpinBox.setValue(7.09e-03)
        self.insertion_doubleSpinBox.setValue(4.14e-03)
        self.one_base_del_doubleSpinBox.setValue(2.77e-03)
        self.long_del_doubleSpinBox.setValue(4.79e-04)

        # per base errors
        self.set_per_base_substitution(0.00724, 0.00701, 0.00706, 0.00704)
        self.set_per_base_insertion(0.00411, 0.00415, 0.00415, 0.00413)
        self.set_per_base_pre_insertion(0.00429, 0.00415, 0.00403, 0.00408)
        self.set_per_base_del(0.00289, 0.00279, 0.00276, 0.0028)
        self.set_per_base_long_del(0.00048, 0.00048, 0.00047, 0.00049)

    def set_G15_values(self):
        # general errors
        self.substitution_doubleSpinBox.setValue(5.84e-03)
        self.insertion_doubleSpinBox.setValue(8.57e-04)
        self.one_base_del_doubleSpinBox.setValue(5.37e-03)
        self.long_del_doubleSpinBox.setValue(3.48e-04)

        # per base errors
        self.set_per_base_substitution(0.00605, 0.00563, 0.00577, 0.00591)
        self.set_per_base_insertion(0.0009, 0.00083, 0.00085, 0.00084)
        self.set_per_base_pre_insertion(0.00092, 0.00081, 0.00087, 0.00084)
        self.set_per_base_del(0.00543, 0.00513, 0.00539, 0.00559)
        self.set_per_base_long_del(0.00036, 0.00034, 0.00034, 0.00036)

    def set_Y16_values(self):
        # general errors
        self.substitution_doubleSpinBox.setValue(1.21e-01)
        self.insertion_doubleSpinBox.setValue(3.67e-01)
        self.one_base_del_doubleSpinBox.setValue(4.33e-02)
        self.long_del_doubleSpinBox.setValue(1.87e-02)

        # per base errors
        self.set_per_base_substitution(0.119, 0.133, 0.112, 0.119)
        self.set_per_base_insertion(0.331, 0.406, 0.361, 0.367)
        self.set_per_base_pre_insertion(0.332, 0.408, 0.341, 0.382)
        self.set_per_base_del(0.044, 0.048, 0.040, 0.041)
        self.set_per_base_long_del(0.019, 0.021, 0.017, 0.018)

    def openFileDialog(self):
        self.inputDNAPath, _ = QFileDialog.getOpenFileName(self, "Select an input file", './', filter="*.txt")
        self.file_path_lineEdit.setText(self.inputDNAPath)

    def show_error_dialog(self, error_type):
        if error_type == 'no_such_file':
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
                self.file_path_lineEdit.clear()
                break
            else:
                self.worker = SimulateErrorsWorker(self.general_errors, self.per_base_errors, self.inputDNAPath)
                self.worker.start()
                self.label_progress.setText('Injecting errors, please wait!')
                self.worker.finished.connect(self.evt_worker_finished)
                self.worker.update_progress.connect(self.evt_update_progress)
                # self.worker.update_error_sim_finished.connect(self.evt_update_error_finished)
                self.progressBar.setVisible(True)

                break

    def evt_worker_finished(self):
        self.label_progress.setText('We are done :)')
        self.progressBar.setValue(100)
        self.progressBar.setVisible(False)

    def evt_update_progress(self, val):
        self.progressBar.setValue(val + 1)

    # def evt_update_error_finished(self, val):
    #     if val == 'error_sim_finished':
    #         self.label_progress.setText('Running reconstruction, please wait!')
    #         self.progressBar.setValue(0)

    def msg_box_with_error(self, error_msg):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(error_msg)
        msg.setWindowTitle("Error!")
        msg.setStandardButtons(QMessageBox.Ok)
        retval = msg.exec_()

    def run_reconstruction_algo(self):
        if not os.path.isfile('output/evyat.txt'):
            self.msg_box_with_error('Please run the error simulator first, or provide the evyat.txt input file')
            self.label_progress.setText('')
            return

        self.label_progress.setText('Running reconstruction, please wait!')
        if self.reconstruction_algo == 'Hybrid Reconstruction Algorithm':
            if platform.system() == "Linux" or platform == "linux2":
                # linux
                pass
            elif platform.system() == "Darwin":
                # OS X
                subprocess.run('./reconstruction_algs/DNA', cwd='output/')
            elif platform.system() == "Windows":
                # Windows...
                self.label_progress.setText('Hell knows how long it\'s gonna take, until Omer will feed us with some '
                                            'info')
                subprocess.run('reconstruction_algs/Hybrid.exe', cwd='output/')
        elif self.reconstruction_algo == 'Divider BMA Reconstruction Algorithm':
            if platform.system() == "Linux" or platform == "linux2":
                # linux
                pass
            elif platform.system() == "Darwin":
                # OS X
                # subprocess.run('./reconstruction_algs/DNA')
                pass
            elif platform.system() == "Windows":
                # Windows...
                self.label_progress.setText('Hell knows how long it\'s gonna take, until Omer will feed us with some '
                                            'info')
                subprocess.run('reconstruction_algs/DivBMA.exe', cwd='output/')
        elif self.reconstruction_algo == 'BMA Look Ahead Reconstruction Algorithm':
            if platform.system() == "Linux" or platform == "linux2":
                # linux
                pass
            elif platform.system() == "Darwin":
                # OS X
                # subprocess.run('./reconstruction_algs/DNA')
                pass
            elif platform.system() == "Windows":
                # Windows...
                self.label_progress.setText('Hell knows how long it\'s gonna take, until Omer will feed us with some '
                                            'info')
                subprocess.run('reconstruction_algs/BMALookahead.exe', cwd='output/')
        elif self.reconstruction_algo == 'Iterative Reconstruction Algorithm':
            if platform.system() == "Linux" or platform == "linux2":
                # linux
                pass
            elif platform.system() == "Darwin":
                # OS X
                # subprocess.run('./reconstruction_algs/DNA')
                pass
            elif platform.system() == "Windows":
                # Windows...
                self.label_progress.setText('Hell knows how long it\'s gonna take, until Omer will feed us with some '
                                            'info')
                subprocess.run('reconstruction_algs/Iterative.exe', cwd='output/')
        else:
            self.msg_box_with_error('Please choose a reconstruction algorithm')
            self.label_progress.setText('')
            return

        if not os.path.isfile('output/output.txt'):
            self.msg_box_with_error('Reconstruction doesn\'t have an output. Try running it again')
            return
        else:
            text = open('output/output.txt').read()
            self.reconstruction_output_textEdit.setText(text)
        self.label_progress.setText('We are done :)')


class SimulateErrorsWorker(QThread):
    update_progress = pyqtSignal(int)
    update_error_sim_finished = pyqtSignal(str)

    def __init__(self, general_errors, per_base_errors, input_dna_path):
        super(SimulateErrorsWorker, self).__init__()
        self.general_errors = general_errors
        self.per_base_errors = per_base_errors
        self.inputDNAPath = input_dna_path

    def report_func(self, total_lines, curr_line):
        percent = int(curr_line * 100 // total_lines)
        self.update_progress.emit(percent)

    def run(self):
        error_sim = Simulator(self.general_errors, self.per_base_errors, self.inputDNAPath)
        error_sim.simulate_errors(self.report_func)
        # self.update_error_sim_finished.emit('error_sim_finished')



if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    dnaSimulator = dnaSimulator()
    dnaSimulator.show()
    # Run the main Qt loop
    sys.exit(app.exec_())
