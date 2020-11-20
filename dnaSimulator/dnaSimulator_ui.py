# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dnaSimulator.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_dnaSimulator(object):
    def setupUi(self, dnaSimulator):
        if not dnaSimulator.objectName():
            dnaSimulator.setObjectName(u"dnaSimulator")
        dnaSimulator.resize(620, 562)
        self.centralwidget = QWidget(dnaSimulator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.file_input_horizontalLayout = QHBoxLayout()
        self.file_input_horizontalLayout.setObjectName(u"file_input_horizontalLayout")
        self.load_Input_Label = QLabel(self.centralwidget)
        self.load_Input_Label.setObjectName(u"load_Input_Label")

        self.file_input_horizontalLayout.addWidget(self.load_Input_Label)

        self.file_path_lineEdit = QLineEdit(self.centralwidget)
        self.file_path_lineEdit.setObjectName(u"file_path_lineEdit")

        self.file_input_horizontalLayout.addWidget(self.file_path_lineEdit)

        self.browse_PushButton = QPushButton(self.centralwidget)
        self.browse_PushButton.setObjectName(u"browse_PushButton")
        self.browse_PushButton.setIconSize(QSize(16, 16))

        self.file_input_horizontalLayout.addWidget(self.browse_PushButton)


        self.verticalLayout_3.addLayout(self.file_input_horizontalLayout)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.sequencing_tech_verticalLayout = QVBoxLayout()
        self.sequencing_tech_verticalLayout.setObjectName(u"sequencing_tech_verticalLayout")
        self.sequencing_tech_label = QLabel(self.centralwidget)
        self.sequencing_tech_label.setObjectName(u"sequencing_tech_label")
        font = QFont()
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.sequencing_tech_label.setFont(font)

        self.sequencing_tech_verticalLayout.addWidget(self.sequencing_tech_label)

        self.tech_radio_buttons_horizontalLayout = QHBoxLayout()
        self.tech_radio_buttons_horizontalLayout.setSpacing(15)
        self.tech_radio_buttons_horizontalLayout.setObjectName(u"tech_radio_buttons_horizontalLayout")
        self.MinION_radioButton = QRadioButton(self.centralwidget)
        self.MinION_radioButton.setObjectName(u"MinION_radioButton")

        self.tech_radio_buttons_horizontalLayout.addWidget(self.MinION_radioButton)

        self.Ilumina_NextSeq_radioButton = QRadioButton(self.centralwidget)
        self.Ilumina_NextSeq_radioButton.setObjectName(u"Ilumina_NextSeq_radioButton")

        self.tech_radio_buttons_horizontalLayout.addWidget(self.Ilumina_NextSeq_radioButton)

        self.Ilumina_miSeq_radioButton = QRadioButton(self.centralwidget)
        self.Ilumina_miSeq_radioButton.setObjectName(u"Ilumina_miSeq_radioButton")

        self.tech_radio_buttons_horizontalLayout.addWidget(self.Ilumina_miSeq_radioButton)

        self.tech_radio_buttons_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.tech_radio_buttons_horizontalLayout.addItem(self.tech_radio_buttons_horizontalSpacer)


        self.sequencing_tech_verticalLayout.addLayout(self.tech_radio_buttons_horizontalLayout)


        self.verticalLayout_3.addLayout(self.sequencing_tech_verticalLayout)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_2)

        self.synthesis_tech_verticalLayout = QVBoxLayout()
        self.synthesis_tech_verticalLayout.setObjectName(u"synthesis_tech_verticalLayout")
        self.synthesis_tech_radio_buttons_label = QLabel(self.centralwidget)
        self.synthesis_tech_radio_buttons_label.setObjectName(u"synthesis_tech_radio_buttons_label")
        self.synthesis_tech_radio_buttons_label.setFont(font)

        self.synthesis_tech_verticalLayout.addWidget(self.synthesis_tech_radio_buttons_label)

        self.synthesis_tech_radio_buttons_horizontalLayout = QHBoxLayout()
        self.synthesis_tech_radio_buttons_horizontalLayout.setSpacing(15)
        self.synthesis_tech_radio_buttons_horizontalLayout.setObjectName(u"synthesis_tech_radio_buttons_horizontalLayout")
        self.twist_bioscience_radioButton = QRadioButton(self.centralwidget)
        self.twist_bioscience_radioButton.setObjectName(u"twist_bioscience_radioButton")

        self.synthesis_tech_radio_buttons_horizontalLayout.addWidget(self.twist_bioscience_radioButton)

        self.customArray_radioButton = QRadioButton(self.centralwidget)
        self.customArray_radioButton.setObjectName(u"customArray_radioButton")

        self.synthesis_tech_radio_buttons_horizontalLayout.addWidget(self.customArray_radioButton)

        self.IDT_radioButton = QRadioButton(self.centralwidget)
        self.IDT_radioButton.setObjectName(u"IDT_radioButton")

        self.synthesis_tech_radio_buttons_horizontalLayout.addWidget(self.IDT_radioButton)

        self.synthesis_tech_radio_buttons_horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.synthesis_tech_radio_buttons_horizontalLayout.addItem(self.synthesis_tech_radio_buttons_horizontalSpacer)


        self.synthesis_tech_verticalLayout.addLayout(self.synthesis_tech_radio_buttons_horizontalLayout)


        self.verticalLayout_3.addLayout(self.synthesis_tech_verticalLayout)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)

        self.error_stats_verticalLayout = QVBoxLayout()
        self.error_stats_verticalLayout.setObjectName(u"error_stats_verticalLayout")
        self.error_stats_label = QLabel(self.centralwidget)
        self.error_stats_label.setObjectName(u"error_stats_label")
        self.error_stats_label.setFont(font)

        self.error_stats_verticalLayout.addWidget(self.error_stats_label)

        self.error_stats_inputs_horizontalLayout = QHBoxLayout()
        self.error_stats_inputs_horizontalLayout.setObjectName(u"error_stats_inputs_horizontalLayout")
        self.substitution_lineEdit = QLineEdit(self.centralwidget)
        self.substitution_lineEdit.setObjectName(u"substitution_lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.substitution_lineEdit.sizePolicy().hasHeightForWidth())
        self.substitution_lineEdit.setSizePolicy(sizePolicy)

        self.error_stats_inputs_horizontalLayout.addWidget(self.substitution_lineEdit)

        self.insertion_lineEdit = QLineEdit(self.centralwidget)
        self.insertion_lineEdit.setObjectName(u"insertion_lineEdit")

        self.error_stats_inputs_horizontalLayout.addWidget(self.insertion_lineEdit)

        self.one_base_del_lineEdit = QLineEdit(self.centralwidget)
        self.one_base_del_lineEdit.setObjectName(u"one_base_del_lineEdit")

        self.error_stats_inputs_horizontalLayout.addWidget(self.one_base_del_lineEdit)

        self.long_del_lineEdit = QLineEdit(self.centralwidget)
        self.long_del_lineEdit.setObjectName(u"long_del_lineEdit")

        self.error_stats_inputs_horizontalLayout.addWidget(self.long_del_lineEdit)

        self.set_current_values_PushButton = QPushButton(self.centralwidget)
        self.set_current_values_PushButton.setObjectName(u"set_current_values_PushButton")
        self.set_current_values_PushButton.setIconSize(QSize(16, 16))

        self.error_stats_inputs_horizontalLayout.addWidget(self.set_current_values_PushButton)


        self.error_stats_verticalLayout.addLayout(self.error_stats_inputs_horizontalLayout)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.HLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.error_stats_verticalLayout.addWidget(self.line_4)


        self.verticalLayout_3.addLayout(self.error_stats_verticalLayout)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.G_substitution_lineEdit = QLineEdit(self.centralwidget)
        self.G_substitution_lineEdit.setObjectName(u"G_substitution_lineEdit")

        self.gridLayout.addWidget(self.G_substitution_lineEdit, 1, 3, 1, 1)

        self.G_pre_insertion_lineEdit = QLineEdit(self.centralwidget)
        self.G_pre_insertion_lineEdit.setObjectName(u"G_pre_insertion_lineEdit")

        self.gridLayout.addWidget(self.G_pre_insertion_lineEdit, 3, 3, 1, 1)

        self.G_base_label = QLabel(self.centralwidget)
        self.G_base_label.setObjectName(u"G_base_label")
        self.G_base_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.G_base_label, 6, 3, 1, 1)

        self.T_substitution_lineEdit = QLineEdit(self.centralwidget)
        self.T_substitution_lineEdit.setObjectName(u"T_substitution_lineEdit")

        self.gridLayout.addWidget(self.T_substitution_lineEdit, 1, 5, 1, 1)

        self.empty_label = QLabel(self.centralwidget)
        self.empty_label.setObjectName(u"empty_label")

        self.gridLayout.addWidget(self.empty_label, 6, 0, 1, 1)

        self.A_substitution_lineEdit = QLineEdit(self.centralwidget)
        self.A_substitution_lineEdit.setObjectName(u"A_substitution_lineEdit")

        self.gridLayout.addWidget(self.A_substitution_lineEdit, 1, 1, 1, 1)

        self.G_long_del_lineEdit = QLineEdit(self.centralwidget)
        self.G_long_del_lineEdit.setObjectName(u"G_long_del_lineEdit")

        self.gridLayout.addWidget(self.G_long_del_lineEdit, 5, 3, 1, 1)

        self.long_del_label = QLabel(self.centralwidget)
        self.long_del_label.setObjectName(u"long_del_label")

        self.gridLayout.addWidget(self.long_del_label, 5, 0, 1, 1)

        self.A_long_del_lineEdit = QLineEdit(self.centralwidget)
        self.A_long_del_lineEdit.setObjectName(u"A_long_del_lineEdit")

        self.gridLayout.addWidget(self.A_long_del_lineEdit, 5, 1, 1, 1)

        self.one_base_del_label = QLabel(self.centralwidget)
        self.one_base_del_label.setObjectName(u"one_base_del_label")

        self.gridLayout.addWidget(self.one_base_del_label, 4, 0, 1, 1)

        self.C_one_base_del_lineEdit = QLineEdit(self.centralwidget)
        self.C_one_base_del_lineEdit.setObjectName(u"C_one_base_del_lineEdit")

        self.gridLayout.addWidget(self.C_one_base_del_lineEdit, 4, 2, 1, 1)

        self.T_pre_insertion_lineEdit = QLineEdit(self.centralwidget)
        self.T_pre_insertion_lineEdit.setObjectName(u"T_pre_insertion_lineEdit")

        self.gridLayout.addWidget(self.T_pre_insertion_lineEdit, 3, 5, 1, 1)

        self.C_pre_insertion_lineEdit = QLineEdit(self.centralwidget)
        self.C_pre_insertion_lineEdit.setObjectName(u"C_pre_insertion_lineEdit")

        self.gridLayout.addWidget(self.C_pre_insertion_lineEdit, 3, 2, 1, 1)

        self.A_pre_insertion_lineEdit = QLineEdit(self.centralwidget)
        self.A_pre_insertion_lineEdit.setObjectName(u"A_pre_insertion_lineEdit")

        self.gridLayout.addWidget(self.A_pre_insertion_lineEdit, 3, 1, 1, 1)

        self.pre_insertion_label = QLabel(self.centralwidget)
        self.pre_insertion_label.setObjectName(u"pre_insertion_label")

        self.gridLayout.addWidget(self.pre_insertion_label, 3, 0, 1, 1)

        self.C_substitution_lineEdit = QLineEdit(self.centralwidget)
        self.C_substitution_lineEdit.setObjectName(u"C_substitution_lineEdit")

        self.gridLayout.addWidget(self.C_substitution_lineEdit, 1, 2, 1, 1)

        self.C_insertion_lineEdit = QLineEdit(self.centralwidget)
        self.C_insertion_lineEdit.setObjectName(u"C_insertion_lineEdit")

        self.gridLayout.addWidget(self.C_insertion_lineEdit, 2, 2, 1, 1)

        self.G_insertion_lineEdit = QLineEdit(self.centralwidget)
        self.G_insertion_lineEdit.setObjectName(u"G_insertion_lineEdit")

        self.gridLayout.addWidget(self.G_insertion_lineEdit, 2, 3, 1, 1)

        self.T_long_del_lineEdit = QLineEdit(self.centralwidget)
        self.T_long_del_lineEdit.setObjectName(u"T_long_del_lineEdit")

        self.gridLayout.addWidget(self.T_long_del_lineEdit, 5, 5, 1, 1)

        self.Substitution_label = QLabel(self.centralwidget)
        self.Substitution_label.setObjectName(u"Substitution_label")

        self.gridLayout.addWidget(self.Substitution_label, 1, 0, 1, 1)

        self.A_one_base_del_lineEdit = QLineEdit(self.centralwidget)
        self.A_one_base_del_lineEdit.setObjectName(u"A_one_base_del_lineEdit")

        self.gridLayout.addWidget(self.A_one_base_del_lineEdit, 4, 1, 1, 1)

        self.T_base_label = QLabel(self.centralwidget)
        self.T_base_label.setObjectName(u"T_base_label")
        self.T_base_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.T_base_label, 6, 5, 1, 1)

        self.error_stats_base_label = QLabel(self.centralwidget)
        self.error_stats_base_label.setObjectName(u"error_stats_base_label")
        self.error_stats_base_label.setFont(font)

        self.gridLayout.addWidget(self.error_stats_base_label, 0, 0, 1, 1)

        self.C_long_del_lineEdit = QLineEdit(self.centralwidget)
        self.C_long_del_lineEdit.setObjectName(u"C_long_del_lineEdit")

        self.gridLayout.addWidget(self.C_long_del_lineEdit, 5, 2, 1, 1)

        self.T_insertion_lineEdit = QLineEdit(self.centralwidget)
        self.T_insertion_lineEdit.setObjectName(u"T_insertion_lineEdit")

        self.gridLayout.addWidget(self.T_insertion_lineEdit, 2, 5, 1, 1)

        self.A_base_label = QLabel(self.centralwidget)
        self.A_base_label.setObjectName(u"A_base_label")
        self.A_base_label.setAutoFillBackground(False)
        self.A_base_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.A_base_label, 6, 1, 1, 1)

        self.T_one_base_del_lineEdit = QLineEdit(self.centralwidget)
        self.T_one_base_del_lineEdit.setObjectName(u"T_one_base_del_lineEdit")

        self.gridLayout.addWidget(self.T_one_base_del_lineEdit, 4, 5, 1, 1)

        self.Insertion_label = QLabel(self.centralwidget)
        self.Insertion_label.setObjectName(u"Insertion_label")

        self.gridLayout.addWidget(self.Insertion_label, 2, 0, 1, 1)

        self.A_insertion_lineEdit = QLineEdit(self.centralwidget)
        self.A_insertion_lineEdit.setObjectName(u"A_insertion_lineEdit")

        self.gridLayout.addWidget(self.A_insertion_lineEdit, 2, 1, 1, 1)

        self.G_one_base_del_lineEdit = QLineEdit(self.centralwidget)
        self.G_one_base_del_lineEdit.setObjectName(u"G_one_base_del_lineEdit")

        self.gridLayout.addWidget(self.G_one_base_del_lineEdit, 4, 3, 1, 1)

        self.C_base_label = QLabel(self.centralwidget)
        self.C_base_label.setObjectName(u"C_base_label")
        self.C_base_label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.C_base_label, 6, 2, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        self.line_5 = QFrame(self.centralwidget)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.HLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_5)

        self.execute_horizontalLayout = QHBoxLayout()
        self.execute_horizontalLayout.setObjectName(u"execute_horizontalLayout")
        self.execute_horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.execute_horizontalSpacer_left = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.execute_horizontalLayout.addItem(self.execute_horizontalSpacer_left)

        self.run_error_simulator_PushButton = QPushButton(self.centralwidget)
        self.run_error_simulator_PushButton.setObjectName(u"run_error_simulator_PushButton")
        sizePolicy1.setHeightForWidth(self.run_error_simulator_PushButton.sizePolicy().hasHeightForWidth())
        self.run_error_simulator_PushButton.setSizePolicy(sizePolicy1)
        self.run_error_simulator_PushButton.setLayoutDirection(Qt.LeftToRight)
        self.run_error_simulator_PushButton.setAutoFillBackground(False)

        self.execute_horizontalLayout.addWidget(self.run_error_simulator_PushButton)

        self.execute_horizontalSpacer_right = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.execute_horizontalLayout.addItem(self.execute_horizontalSpacer_right)


        self.verticalLayout_3.addLayout(self.execute_horizontalLayout)

        dnaSimulator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(dnaSimulator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 620, 21))
        dnaSimulator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(dnaSimulator)
        self.statusbar.setObjectName(u"statusbar")
        dnaSimulator.setStatusBar(self.statusbar)

        self.retranslateUi(dnaSimulator)

        QMetaObject.connectSlotsByName(dnaSimulator)
    # setupUi

    def retranslateUi(self, dnaSimulator):
        dnaSimulator.setWindowTitle(QCoreApplication.translate("dnaSimulator", u"MainWindow", None))
        self.load_Input_Label.setText(QCoreApplication.translate("dnaSimulator", u"Load input file:", None))
        self.file_path_lineEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"File path", None))
        self.browse_PushButton.setText(QCoreApplication.translate("dnaSimulator", u"Browse", None))
        self.sequencing_tech_label.setText(QCoreApplication.translate("dnaSimulator", u"Sequencing Technology:", None))
        self.MinION_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"MinION", None))
        self.Ilumina_NextSeq_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"Ilumina NextSeq", None))
        self.Ilumina_miSeq_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"Ilumina miSeq", None))
        self.synthesis_tech_radio_buttons_label.setText(QCoreApplication.translate("dnaSimulator", u"Synthesis Technology:", None))
        self.twist_bioscience_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"Twist Bioscience", None))
        self.customArray_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"CustomArray", None))
        self.IDT_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"Integrated DNA Technology (IDT)", None))
        self.error_stats_label.setText(QCoreApplication.translate("dnaSimulator", u"Error Statistics:", None))
        self.substitution_lineEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"Substitution", None))
        self.insertion_lineEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"Insertion", None))
        self.one_base_del_lineEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"1-base Deletion", None))
        self.long_del_lineEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"Long Deletion", None))
        self.set_current_values_PushButton.setText(QCoreApplication.translate("dnaSimulator", u"Set Values", None))
        self.G_base_label.setText(QCoreApplication.translate("dnaSimulator", u"G", None))
        self.empty_label.setText("")
        self.long_del_label.setText(QCoreApplication.translate("dnaSimulator", u"Long Deletion", None))
        self.one_base_del_label.setText(QCoreApplication.translate("dnaSimulator", u"1-base Deletion", None))
        self.pre_insertion_label.setText(QCoreApplication.translate("dnaSimulator", u"pre-insertion", None))
        self.Substitution_label.setText(QCoreApplication.translate("dnaSimulator", u"Substitution", None))
        self.T_base_label.setText(QCoreApplication.translate("dnaSimulator", u"T", None))
        self.error_stats_base_label.setText(QCoreApplication.translate("dnaSimulator", u"Error statistics per base:", None))
        self.A_base_label.setText(QCoreApplication.translate("dnaSimulator", u"A", None))
        self.Insertion_label.setText(QCoreApplication.translate("dnaSimulator", u"Insertion", None))
        self.C_base_label.setText(QCoreApplication.translate("dnaSimulator", u"C", None))
        self.run_error_simulator_PushButton.setText(QCoreApplication.translate("dnaSimulator", u"Run error simulator", None))
    # retranslateUi

