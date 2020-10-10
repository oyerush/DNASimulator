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
        dnaSimulator.resize(856, 620)
        self.centralwidget = QWidget(dnaSimulator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.loadInputLabel = QLabel(self.centralwidget)
        self.loadInputLabel.setObjectName(u"loadInputLabel")
        self.loadInputLabel.setGeometry(QRect(20, 20, 101, 31))
        self.browsePushButton = QPushButton(self.centralwidget)
        self.browsePushButton.setObjectName(u"browsePushButton")
        self.browsePushButton.setGeometry(QRect(680, 20, 93, 28))
        self.browsePushButton.setIconSize(QSize(16, 16))
        self.filePath_textEdit = QPlainTextEdit(self.centralwidget)
        self.filePath_textEdit.setObjectName(u"filePath_textEdit")
        self.filePath_textEdit.setGeometry(QRect(130, 20, 531, 28))
        self.synthesis_groupBox = QGroupBox(self.centralwidget)
        self.synthesis_groupBox.setObjectName(u"synthesis_groupBox")
        self.synthesis_groupBox.setGeometry(QRect(10, 80, 391, 60))
        self.widget = QWidget(self.synthesis_groupBox)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 30, 260, 19))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")

        self.horizontalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.horizontalLayout.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.widget)
        self.radioButton_3.setObjectName(u"radioButton_3")

        self.horizontalLayout.addWidget(self.radioButton_3)

        self.sequencing_groupBox = QGroupBox(self.centralwidget)
        self.sequencing_groupBox.setObjectName(u"sequencing_groupBox")
        self.sequencing_groupBox.setGeometry(QRect(10, 150, 391, 60))
        self.widget1 = QWidget(self.sequencing_groupBox)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(10, 20, 172, 19))
        self.horizontalLayout_2 = QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.radioButton_4 = QRadioButton(self.widget1)
        self.radioButton_4.setObjectName(u"radioButton_4")

        self.horizontalLayout_2.addWidget(self.radioButton_4)

        self.radioButton_5 = QRadioButton(self.widget1)
        self.radioButton_5.setObjectName(u"radioButton_5")

        self.horizontalLayout_2.addWidget(self.radioButton_5)

        self.priorities_groupBox = QGroupBox(self.centralwidget)
        self.priorities_groupBox.setObjectName(u"priorities_groupBox")
        self.priorities_groupBox.setGeometry(QRect(10, 220, 391, 60))
        self.substitution_textEdit = QTextEdit(self.priorities_groupBox)
        self.substitution_textEdit.setObjectName(u"substitution_textEdit")
        self.substitution_textEdit.setGeometry(QRect(230, 20, 90, 28))
        self.deletion_textEdit = QTextEdit(self.priorities_groupBox)
        self.deletion_textEdit.setObjectName(u"deletion_textEdit")
        self.deletion_textEdit.setGeometry(QRect(10, 20, 90, 28))
        self.insertion_textEdit = QTextEdit(self.priorities_groupBox)
        self.insertion_textEdit.setObjectName(u"insertion_textEdit")
        self.insertion_textEdit.setGeometry(QRect(120, 20, 90, 28))
        dnaSimulator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(dnaSimulator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 856, 21))
        dnaSimulator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(dnaSimulator)
        self.statusbar.setObjectName(u"statusbar")
        dnaSimulator.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.filePath_textEdit, self.browsePushButton)
        QWidget.setTabOrder(self.browsePushButton, self.radioButton)
        QWidget.setTabOrder(self.radioButton, self.radioButton_2)
        QWidget.setTabOrder(self.radioButton_2, self.radioButton_3)
        QWidget.setTabOrder(self.radioButton_3, self.radioButton_4)
        QWidget.setTabOrder(self.radioButton_4, self.radioButton_5)
        QWidget.setTabOrder(self.radioButton_5, self.deletion_textEdit)
        QWidget.setTabOrder(self.deletion_textEdit, self.insertion_textEdit)
        QWidget.setTabOrder(self.insertion_textEdit, self.substitution_textEdit)

        self.retranslateUi(dnaSimulator)

        QMetaObject.connectSlotsByName(dnaSimulator)
    # setupUi

    def retranslateUi(self, dnaSimulator):
        dnaSimulator.setWindowTitle(QCoreApplication.translate("dnaSimulator", u"DNA Simulator", None))
        self.loadInputLabel.setText(QCoreApplication.translate("dnaSimulator", u"Load input file:", None))
        self.browsePushButton.setText(QCoreApplication.translate("dnaSimulator", u"Browse", None))
        self.filePath_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"File path", None))
        self.synthesis_groupBox.setTitle(QCoreApplication.translate("dnaSimulator", u"Synthesis:", None))
        self.radioButton.setText(QCoreApplication.translate("dnaSimulator", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("dnaSimulator", u"RadioButton", None))
        self.radioButton_3.setText(QCoreApplication.translate("dnaSimulator", u"RadioButton", None))
        self.sequencing_groupBox.setTitle(QCoreApplication.translate("dnaSimulator", u"Sequencing:", None))
        self.radioButton_4.setText(QCoreApplication.translate("dnaSimulator", u"RadioButton", None))
        self.radioButton_5.setText(QCoreApplication.translate("dnaSimulator", u"RadioButton", None))
        self.priorities_groupBox.setTitle(QCoreApplication.translate("dnaSimulator", u"Priorities:", None))
        self.substitution_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"Substitution rate", None))
        self.deletion_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"Deletion rate", None))
        self.insertion_textEdit.setPlaceholderText(QCoreApplication.translate("dnaSimulator", u"Insertion rate", None))
    # retranslateUi

