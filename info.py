# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(719, 485)
        Dialog.setStyleSheet(u"background-color: rgb(255, 255, 255)")
        self.linearButton = QPushButton(Dialog)
        self.linearButton.setObjectName(u"linearButton")
        self.linearButton.setGeometry(QRect(600, 210, 101, 31))
        self.linearButton.setStyleSheet(u"background-color: rgb(170, 219, 255);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 127);\n"
"font: bold 10pt;\n"
"font-family: Cascadia Code;\n"
"")
        self.binaryButton = QPushButton(Dialog)
        self.binaryButton.setObjectName(u"binaryButton")
        self.binaryButton.setGeometry(QRect(600, 260, 101, 31))
        self.binaryButton.setStyleSheet(u"background-color: rgb(170, 219, 255);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 127);\n"
"font: bold 10pt;\n"
"font-family: Cascadia Code;\n"
"")
        self.sigmoidButton = QPushButton(Dialog)
        self.sigmoidButton.setObjectName(u"sigmoidButton")
        self.sigmoidButton.setGeometry(QRect(600, 310, 101, 31))
        self.sigmoidButton.setStyleSheet(u"background-color: rgb(170, 219, 255);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 127);\n"
"font: bold 7pt;\n"
"font-family: Cascadia Code;\n"
"")
        self.neuronButton = QPushButton(Dialog)
        self.neuronButton.setObjectName(u"neuronButton")
        self.neuronButton.setGeometry(QRect(600, 160, 101, 31))
        self.neuronButton.setStyleSheet(u"background-color: rgb(170, 219, 255);\n"
"border-radius: 5px;\n"
"color: rgb(0, 0, 127);\n"
"font: bold 10pt;\n"
"font-family: Cascadia Code;\n"
"")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 551, 351))
        self.label.setStyleSheet(u"border-radius: 5px;\n"
"border: 2px solid gray;")
        self.textLabel = QLabel(Dialog)
        self.textLabel.setObjectName(u"textLabel")
        self.textLabel.setGeometry(QRect(20, 370, 551, 91))
        self.textLabel.setStyleSheet(u"border-radius: 5px;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.linearButton.setText(QCoreApplication.translate("Dialog", u"\u041b\u0438\u043d\u0435\u0439\u043d\u0430\u044f", None))
        self.binaryButton.setText(QCoreApplication.translate("Dialog", u"\u041f\u043e\u0440\u043e\u0433\u043e\u0432\u0430\u044f", None))
        self.sigmoidButton.setText(QCoreApplication.translate("Dialog", u"\u0421\u0438\u0433\u043c\u043e\u0438\u0434\u0430\u043b\u044c\u043d\u0430\u044f", None))
        self.neuronButton.setText(QCoreApplication.translate("Dialog", u"\u041d\u0435\u0439\u0440\u043e\u043d", None))
        self.label.setText("")
        self.textLabel.setText("")
    # retranslateUi

