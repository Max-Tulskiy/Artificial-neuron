# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 609)
        MainWindow.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.clearButton = QPushButton(self.centralwidget)
        self.clearButton.setObjectName(u"clearButton")
        self.clearButton.setGeometry(QRect(640, 140, 131, 28))
        self.clearButton.setStyleSheet(u"background-color: rgb(110, 151, 171);\n"
"border-radius:2%;\n"
"color: rgb(255, 255, 255);\n"
"font: bold 10pt;\n"
"font-family: Cascadia Code;\n"
"border: 1px solid gray;")
        self.solveButton = QPushButton(self.centralwidget)
        self.solveButton.setObjectName(u"solveButton")
        self.solveButton.setGeometry(QRect(640, 100, 131, 28))
        self.solveButton.setStyleSheet(u"background-color: rgb(110, 151, 171);\n"
"border-radius:2%;\n"
"color: rgb(255, 255, 255);\n"
"font: bold 10pt;\n"
"font-family: Cascadia Code;\n"
"border: 1px solid gray;")
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(650, 30, 141, 31))
        self.comboBox.setStyleSheet(u"border-radius: 3px;\n"
"border: 2px solid gray;")
        self.lineEdit_w1 = QLineEdit(self.centralwidget)
        self.lineEdit_w1.setObjectName(u"lineEdit_w1")
        self.lineEdit_w1.setGeometry(QRect(660, 280, 113, 22))
        self.lineEdit_w1.setStyleSheet(u"border-radius: 2%;\n"
"border: 1px solid gray;")
        self.lineEdit_w2 = QLineEdit(self.centralwidget)
        self.lineEdit_w2.setObjectName(u"lineEdit_w2")
        self.lineEdit_w2.setGeometry(QRect(660, 320, 113, 22))
        self.lineEdit_w2.setStyleSheet(u"border-radius: 2%;\n"
"border: 1px solid gray;")
        self.lineEdit_k = QLineEdit(self.centralwidget)
        self.lineEdit_k.setObjectName(u"lineEdit_k")
        self.lineEdit_k.setGeometry(QRect(660, 370, 113, 22))
        self.lineEdit_k.setStyleSheet(u"border-radius: 2%;\n"
"border: 1px solid gray;")
        self.lineEdit_theta = QLineEdit(self.centralwidget)
        self.lineEdit_theta.setObjectName(u"lineEdit_theta")
        self.lineEdit_theta.setGeometry(QRect(660, 410, 113, 22))
        self.lineEdit_theta.setStyleSheet(u"border-radius: 2%;\n"
"border: 1px solid gray;")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(630, 280, 21, 16))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(630, 320, 21, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(630, 370, 21, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(620, 410, 31, 16))
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 531, 511))
        self.radioButton = QRadioButton(self.centralwidget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(650, 200, 95, 20))
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(650, 230, 95, 20))
        self.saveButton = QPushButton(self.centralwidget)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(660, 470, 81, 28))
        self.saveButton.setStyleSheet(u"background-color: rgb(25, 126, 178);\n"
"border-radius:2%;\n"
"color: rgb(255, 255, 255);\n"
"font: bold 8pt;\n"
"font-family: Cascadia Code;\n"
"border: 1px solid gray;")
        self.loadButton = QPushButton(self.centralwidget)
        self.loadButton.setObjectName(u"loadButton")
        self.loadButton.setGeometry(QRect(660, 510, 81, 28))
        self.loadButton.setStyleSheet(u"background-color: rgb(25, 126, 178);\n"
"border-radius:2%;\n"
"color: rgb(255, 255, 255);\n"
"font: bold 8pt;\n"
"font-family: Cascadia Code;\n"
"border: 1px solid gray;")
        self.saveButton_2 = QPushButton(self.centralwidget)
        self.saveButton_2.setObjectName(u"saveButton_2")
        self.saveButton_2.setGeometry(QRect(610, 30, 31, 28))
        self.saveButton_2.setStyleSheet(u"color: rgb(252, 253, 255);\n"
"background-color: rgb(0, 85, 255);\n"
"color: rgb(255, 255, 255);\n"
"font: bold 8pt;\n"
"font-family: Cascadia Code;\n"
"border: 1px solid gray;\n"
"border-radius: 10px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0447\u0438\u0441\u0442\u043a\u0430", None))
        self.solveButton.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u0448\u0435\u043d\u0438\u0435", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"w1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"w2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"K", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"theta", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430 1", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u0443\u043f\u043f\u0430 2", None))
        self.saveButton.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.loadButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c", None))
        self.saveButton_2.setText(QCoreApplication.translate("MainWindow", u"i", None))
    # retranslateUi

