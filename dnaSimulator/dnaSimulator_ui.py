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
        dnaSimulator.resize(870, 687)
        self.centralwidget = QWidget(dnaSimulator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(30, 20, 771, 31))
        self.load_input_horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.load_input_horizontalLayout.setObjectName(u"load_input_horizontalLayout")
        self.load_input_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.loadInputLabel = QLabel(self.horizontalLayoutWidget_2)
        self.loadInputLabel.setObjectName(u"loadInputLabel")

        self.load_input_horizontalLayout.addWidget(self.loadInputLabel)

        self.filePath_textEdit = QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.filePath_textEdit.setObjectName(u"filePath_textEdit")

        self.load_input_horizontalLayout.addWidget(self.filePath_textEdit)

        self.browse_PushButton = QPushButton(self.horizontalLayoutWidget_2)
        self.browse_PushButton.setObjectName(u"browse_PushButton")
        self.browse_PushButton.setIconSize(QSize(16, 16))

        self.load_input_horizontalLayout.addWidget(self.browse_PushButton)

        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 70, 771, 331))
        self.algorithms_verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.algorithms_verticalLayout.setObjectName(u"algorithms_verticalLayout")
        self.algorithms_verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.error_statistics_groupBox = QGroupBox(self.verticalLayoutWidget)
        self.error_statistics_groupBox.setObjectName(u"error_statistics_groupBox")
        self.horizontalLayoutWidget = QWidget(self.error_statistics_groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 611, 31))
        self.error_statistics_horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.error_statistics_horizontalLayout.setObjectName(u"error_statistics_horizontalLayout")
        self.error_statistics_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.substitution_textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.substitution_textEdit.setObjectName(u"substitution_textEdit")

        self.error_statistics_horizontalLayout.addWidget(self.substitution_textEdit)

        self.insertion_textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.insertion_textEdit.setObjectName(u"insertion_textEdit")

        self.error_statistics_horizontalLayout.addWidget(self.insertion_textEdit)

        self.one_base_deletion_textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.one_base_deletion_textEdit.setObjectName(u"one_base_deletion_textEdit")

        self.error_statistics_horizontalLayout.addWidget(self.one_base_deletion_textEdit)

        self.long_deletion_textEdit = QTextEdit(self.horizontalLayoutWidget)
        self.long_deletion_textEdit.setObjectName(u"long_deletion_textEdit")

        self.error_statistics_horizontalLayout.addWidget(self.long_deletion_textEdit)

        self.set_current_values_PushButton = QPushButton(self.horizontalLayoutWidget)
        self.set_current_values_PushButton.setObjectName(u"set_current_values_PushButton")
        self.set_current_values_PushButton.setIconSize(QSize(16, 16))

        self.error_statistics_horizontalLayout.addWidget(self.set_current_values_PushButton)


        self.algorithms_verticalLayout.addWidget(self.error_statistics_groupBox)

        self.run_error_simulator_horizontalLayout = QHBoxLayout()
        self.run_error_simulator_horizontalLayout.setObjectName(u"run_error_simulator_horizontalLayout")
        self.run_error_simulator_horizontalLayout.setContentsMargins(250, -1, 250, -1)
        self.run_error_simulator_PushButton = QPushButton(self.verticalLayoutWidget)
        self.run_error_simulator_PushButton.setObjectName(u"run_error_simulator_PushButton")
        self.run_error_simulator_PushButton.setIconSize(QSize(16, 16))

        self.run_error_simulator_horizontalLayout.addWidget(self.run_error_simulator_PushButton)


        self.algorithms_verticalLayout.addLayout(self.run_error_simulator_horizontalLayout)

        self.sequencing_groupBox = QGroupBox(self.verticalLayoutWidget)
        self.sequencing_groupBox.setObjectName(u"sequencing_groupBox")
        self.layoutWidget = QWidget(self.sequencing_groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 311, 22))
        self.sequencing_horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.sequencing_horizontalLayout.setSpacing(12)
        self.sequencing_horizontalLayout.setObjectName(u"sequencing_horizontalLayout")
        self.sequencing_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.MinION_radioButton = QRadioButton(self.layoutWidget)
        self.MinION_radioButton.setObjectName(u"MinION_radioButton")

        self.sequencing_horizontalLayout.addWidget(self.MinION_radioButton)

        self.Ilumina_NextSeq_radioButton = QRadioButton(self.layoutWidget)
        self.Ilumina_NextSeq_radioButton.setObjectName(u"Ilumina_NextSeq_radioButton")

        self.sequencing_horizontalLayout.addWidget(self.Ilumina_NextSeq_radioButton)

        self.Ilumina_miSeq_radioButton = QRadioButton(self.layoutWidget)
        self.Ilumina_miSeq_radioButton.setObjectName(u"Ilumina_miSeq_radioButton")

        self.sequencing_horizontalLayout.addWidget(self.Ilumina_miSeq_radioButton)


        self.algorithms_verticalLayout.addWidget(self.sequencing_groupBox)

        self.synthesis_groupBox = QGroupBox(self.verticalLayoutWidget)
        self.synthesis_groupBox.setObjectName(u"synthesis_groupBox")
        self.layoutWidget1 = QWidget(self.synthesis_groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 453, 22))
        self.synthesis_horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.synthesis_horizontalLayout.setSpacing(12)
        self.synthesis_horizontalLayout.setObjectName(u"synthesis_horizontalLayout")
        self.synthesis_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.twist_bioscience_radioButton = QRadioButton(self.layoutWidget1)
        self.twist_bioscience_radioButton.setObjectName(u"twist_bioscience_radioButton")

        self.synthesis_horizontalLayout.addWidget(self.twist_bioscience_radioButton)

        self.customArray_radioButton = QRadioButton(self.layoutWidget1)
        self.customArray_radioButton.setObjectName(u"customArray_radioButton")

        self.synthesis_horizontalLayout.addWidget(self.customArray_radioButton)

        self.IDT_radioButton = QRadioButton(self.layoutWidget1)
        self.IDT_radioButton.setObjectName(u"IDT_radioButton")

        self.synthesis_horizontalLayout.addWidget(self.IDT_radioButton)


        self.algorithms_verticalLayout.addWidget(self.synthesis_groupBox)

        self.clustering_correction_code_groupBox = QGroupBox(self.verticalLayoutWidget)
        self.clustering_correction_code_groupBox.setObjectName(u"clustering_correction_code_groupBox")
        self.layoutWidget2 = QWidget(self.clustering_correction_code_groupBox)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 20, 93, 22))
        self.clustering_correction_horizontalLayout = QHBoxLayout(self.layoutWidget2)
        self.clustering_correction_horizontalLayout.setSpacing(12)
        self.clustering_correction_horizontalLayout.setObjectName(u"clustering_correction_horizontalLayout")
        self.clustering_correction_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.clustering_correction_yes_radioButton = QRadioButton(self.layoutWidget2)
        self.clustering_correction_yes_radioButton.setObjectName(u"clustering_correction_yes_radioButton")

        self.clustering_correction_horizontalLayout.addWidget(self.clustering_correction_yes_radioButton)

        self.clustering_correction_no_radioButton = QRadioButton(self.layoutWidget2)
        self.clustering_correction_no_radioButton.setObjectName(u"clustering_correction_no_radioButton")

        self.clustering_correction_horizontalLayout.addWidget(self.clustering_correction_no_radioButton)


        self.algorithms_verticalLayout.addWidget(self.clustering_correction_code_groupBox)

        dnaSimulator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(dnaSimulator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 870, 21))
        dnaSimulator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(dnaSimulator)
        self.statusbar.setObjectName(u"statusbar")
        dnaSimulator.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.twist_bioscience_radioButton, self.customArray_radioButton)
        QWidget.setTabOrder(self.customArray_radioButton, self.IDT_radioButton)
        QWidget.setTabOrder(self.IDT_radioButton, self.one_base_deletion_textEdit)
        QWidget.setTabOrder(self.one_base_deletion_textEdit, self.insertion_textEdit)
        QWidget.setTabOrder(self.insertion_textEdit, self.substitution_textEdit)

        self.retranslateUi(dnaSimulator)

        QMetaObject.connectSlotsByName(dnaSimulator)
    # setupUi

    def retranslateUi(self, dnaSimulator):
        dnaSimulator.setWindowTitle(QCoreApplication.translate("dnaSimulator", u"DNA Simulator", None))
        self.loadInputLabel.setText(QCoreApplication.translate("dnaSimulator", u"Load input file:", None))
        self.filePath_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"File path", None))
        self.browse_PushButton.setText(QCoreApplication.translate("dnaSimulator", u"Browse", None))
        self.error_statistics_groupBox.setTitle(QCoreApplication.translate("dnaSimulator", u"Error Statistics:", None))
        self.substitution_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"Substitution", None))
        self.insertion_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"Insertion", None))
        self.one_base_deletion_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"1-base Deletion", None))
        self.long_deletion_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"Long Deletion", None))
        self.set_current_values_PushButton.setText(QCoreApplication.translate("dnaSimulator", u"Set Values", None))
        self.run_error_simulator_PushButton.setText(QCoreApplication.translate("dnaSimulator", u"Run Error Simulator", None))
        self.sequencing_groupBox.setTitle(QCoreApplication.translate("dnaSimulator", u"Sequencing Technology:", None))
        self.MinION_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"MinION", None))
        self.Ilumina_NextSeq_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"Ilumina NextSeq", None))
        self.Ilumina_miSeq_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"Ilumina miSeq", None))
        self.synthesis_groupBox.setTitle(QCoreApplication.translate("dnaSimulator", u"Synthesis Technology:", None))
        self.twist_bioscience_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"Twist Bioscience", None))
        self.customArray_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"CustomArray", None))
        self.IDT_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"Integrated DNA Technology (IDT)", None))
        self.clustering_correction_code_groupBox.setTitle(QCoreApplication.translate("dnaSimulator", u"Use clustering correction code:", None))
        self.clustering_correction_yes_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"yes", None))
        self.clustering_correction_no_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"no", None))
    # retranslateUi

