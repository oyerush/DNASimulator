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
        dnaSimulator.resize(843, 759)
        self.centralwidget = QWidget(dnaSimulator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loadInputLabel = QLabel(self.centralwidget)
        self.loadInputLabel.setObjectName(u"loadInputLabel")
        self.loadInputLabel.setGeometry(QRect(30, 16, 101, 31))
        self.browse_PushButton = QPushButton(self.centralwidget)
        self.browse_PushButton.setObjectName(u"browse_PushButton")
        self.browse_PushButton.setGeometry(QRect(680, 20, 93, 25))
        self.browse_PushButton.setIconSize(QSize(16, 16))
        self.filePath_textEdit = QPlainTextEdit(self.centralwidget)
        self.filePath_textEdit.setObjectName(u"filePath_textEdit")
        self.filePath_textEdit.setGeometry(QRect(130, 20, 531, 28))
        self.synthesis_groupBox = QGroupBox(self.centralwidget)
        self.synthesis_groupBox.setObjectName(u"synthesis_groupBox")
        self.synthesis_groupBox.setGeometry(QRect(20, 80, 500, 60))
        self.layoutWidget = QWidget(self.synthesis_groupBox)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 20, 453, 22))
        self.synthesis_horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.synthesis_horizontalLayout.setSpacing(12)
        self.synthesis_horizontalLayout.setObjectName(u"synthesis_horizontalLayout")
        self.synthesis_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.twist_bioscience_radioButton = QRadioButton(self.layoutWidget)
        self.twist_bioscience_radioButton.setObjectName(u"twist_bioscience_radioButton")

        self.synthesis_horizontalLayout.addWidget(self.twist_bioscience_radioButton)

        self.customArray_radioButton = QRadioButton(self.layoutWidget)
        self.customArray_radioButton.setObjectName(u"customArray_radioButton")

        self.synthesis_horizontalLayout.addWidget(self.customArray_radioButton)

        self.IDT_radioButton = QRadioButton(self.layoutWidget)
        self.IDT_radioButton.setObjectName(u"IDT_radioButton")

        self.synthesis_horizontalLayout.addWidget(self.IDT_radioButton)

        self.sequencing_groupBox = QGroupBox(self.centralwidget)
        self.sequencing_groupBox.setObjectName(u"sequencing_groupBox")
        self.sequencing_groupBox.setGeometry(QRect(20, 160, 500, 60))
        self.layoutWidget1 = QWidget(self.sequencing_groupBox)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 20, 311, 22))
        self.sequencing_horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.sequencing_horizontalLayout.setSpacing(12)
        self.sequencing_horizontalLayout.setObjectName(u"sequencing_horizontalLayout")
        self.sequencing_horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.MinION_radioButton = QRadioButton(self.layoutWidget1)
        self.MinION_radioButton.setObjectName(u"MinION_radioButton")

        self.sequencing_horizontalLayout.addWidget(self.MinION_radioButton)

        self.Ilumina_NextSeq_radioButton = QRadioButton(self.layoutWidget1)
        self.Ilumina_NextSeq_radioButton.setObjectName(u"Ilumina_NextSeq_radioButton")

        self.sequencing_horizontalLayout.addWidget(self.Ilumina_NextSeq_radioButton)

        self.Ilumina_miSeq_radioButton = QRadioButton(self.layoutWidget1)
        self.Ilumina_miSeq_radioButton.setObjectName(u"Ilumina_miSeq_radioButton")

        self.sequencing_horizontalLayout.addWidget(self.Ilumina_miSeq_radioButton)

        self.error_statistics_groupBox = QGroupBox(self.centralwidget)
        self.error_statistics_groupBox.setObjectName(u"error_statistics_groupBox")
        self.error_statistics_groupBox.setGeometry(QRect(20, 240, 500, 60))
        self.horizontalLayoutWidget = QWidget(self.error_statistics_groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 20, 481, 31))
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

        self.clustering_correction_code_groupBox = QGroupBox(self.centralwidget)
        self.clustering_correction_code_groupBox.setObjectName(u"clustering_correction_code_groupBox")
        self.clustering_correction_code_groupBox.setGeometry(QRect(20, 320, 500, 60))
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

        dnaSimulator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(dnaSimulator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 843, 21))
        dnaSimulator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(dnaSimulator)
        self.statusbar.setObjectName(u"statusbar")
        dnaSimulator.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.filePath_textEdit, self.browse_PushButton)
        QWidget.setTabOrder(self.browse_PushButton, self.twist_bioscience_radioButton)
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
        self.browse_PushButton.setText(QCoreApplication.translate("dnaSimulator", u"Browse", None))
        self.filePath_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"File path", None))
        self.synthesis_groupBox.setTitle(QCoreApplication.translate("dnaSimulator", u"Synthesis Technology:", None))
        self.twist_bioscience_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"Twist Bioscience", None))
        self.customArray_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"CustomArray", None))
        self.IDT_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"Integrated DNA Technology (IDT)", None))
        self.sequencing_groupBox.setTitle(QCoreApplication.translate("dnaSimulator", u"Sequencing Technology:", None))
        self.MinION_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"MinION", None))
        self.Ilumina_NextSeq_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"Ilumina NextSeq", None))
        self.Ilumina_miSeq_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"Ilumina miSeq", None))
        self.error_statistics_groupBox.setTitle(QCoreApplication.translate("dnaSimulator", u"Error Statistics:", None))
        self.substitution_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"Substitution", None))
        self.insertion_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"Insertion", None))
        self.one_base_deletion_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"1-base Deletion", None))
        self.long_deletion_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"Long Deletion", None))
        self.clustering_correction_code_groupBox.setTitle(QCoreApplication.translate("dnaSimulator", u"Use clustering correction code:", None))
        self.clustering_correction_yes_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"yes", None))
        self.clustering_correction_no_radioButton.setText(QCoreApplication.translate("dnaSimulator", u"no", None))
    # retranslateUi

