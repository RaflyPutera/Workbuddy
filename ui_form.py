# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(430, 600)
        MainWindow.setMinimumSize(QSize(300, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.mainStackW = QStackedWidget(self.frame_2)
        self.mainStackW.setObjectName(u"mainStackW")
        self.mainStackW.setStyleSheet(u"background-color: rgb(221, 215, 215);")
        self.stackIntro = QWidget()
        self.stackIntro.setObjectName(u"stackIntro")
        self.verticalLayout_2 = QVBoxLayout(self.stackIntro)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.Introframe = QFrame(self.stackIntro)
        self.Introframe.setObjectName(u"Introframe")
        self.Introframe.setFrameShape(QFrame.StyledPanel)
        self.Introframe.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Introframe)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.introText = QLabel(self.Introframe)
        self.introText.setObjectName(u"introText")
        font = QFont()
        font.setFamilies([u"Source Code Pro"])
        font.setPointSize(24)
        font.setBold(True)
        self.introText.setFont(font)
        self.introText.setStyleSheet(u"color:rgb(53, 53, 53)")
        self.introText.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.introText, 0, Qt.AlignBottom)

        self.introVersion = QLabel(self.Introframe)
        self.introVersion.setObjectName(u"introVersion")
        font1 = QFont()
        font1.setFamilies([u"Source Code Pro"])
        font1.setPointSize(14)
        self.introVersion.setFont(font1)
        self.introVersion.setStyleSheet(u"color:rgb(118, 118, 118)")

        self.verticalLayout_4.addWidget(self.introVersion, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.Introframe)

        self.mainStackW.addWidget(self.stackIntro)
        self.stackHome = QWidget()
        self.stackHome.setObjectName(u"stackHome")
        self.verticalLayout_5 = QVBoxLayout(self.stackHome)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.MainFrame = QFrame(self.stackHome)
        self.MainFrame.setObjectName(u"MainFrame")
        self.MainFrame.setFrameShape(QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.MainFrame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.headerFrame = QFrame(self.MainFrame)
        self.headerFrame.setObjectName(u"headerFrame")
        self.headerFrame.setFrameShape(QFrame.StyledPanel)
        self.headerFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.headerFrame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 18)
        self.header = QLabel(self.headerFrame)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(150, 40))
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro"])
        font2.setPointSize(12)
        self.header.setFont(font2)
        self.header.setStyleSheet(u"background-color:rgb(127, 121, 121);\n"
"color:white;\n"
"border: 1px solid;\n"
"border-radius:20px;\n"
"border-color:transparent;")
        self.header.setAlignment(Qt.AlignCenter)
        self.header.setMargin(0)

        self.verticalLayout_7.addWidget(self.header)


        self.verticalLayout_6.addWidget(self.headerFrame, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.functionFrame = QFrame(self.MainFrame)
        self.functionFrame.setObjectName(u"functionFrame")
        self.functionFrame.setMinimumSize(QSize(300, 435))
        self.functionFrame.setMaximumSize(QSize(16777215, 16777215))
        self.functionFrame.setAutoFillBackground(False)
        self.functionFrame.setStyleSheet(u"")
        self.functionFrame.setFrameShape(QFrame.StyledPanel)
        self.functionFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.functionFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, 0, 30, 0)
        self.functionStack = QStackedWidget(self.functionFrame)
        self.functionStack.setObjectName(u"functionStack")
        self.functionStack.setAutoFillBackground(False)
        self.functionStack.setStyleSheet(u"background-color:rgb(199, 192, 192);\n"
"border: 1px solid;\n"
"border-radius:20px;\n"
"border-color:transparent;")
        self.f_start = QWidget()
        self.f_start.setObjectName(u"f_start")
        self.verticalLayout_9 = QVBoxLayout(self.f_start)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_2 = QLabel(self.f_start)
        self.label_2.setObjectName(u"label_2")
        font3 = QFont()
        font3.setFamilies([u"Source Code Pro"])
        font3.setPointSize(16)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"color:rgb(53, 48, 48)")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_2)

        self.functionStack.addWidget(self.f_start)
        self.f_translator = QWidget()
        self.f_translator.setObjectName(u"f_translator")
        self.verticalLayout_8 = QVBoxLayout(self.f_translator)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame = QFrame(self.f_translator)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(200, 0))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"Source Code Pro"])
        font4.setPointSize(11)
        self.label.setFont(font4)
        self.label.setStyleSheet(u"color:rgb(90, 84, 84)")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setIndent(0)

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignHCenter)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(30, 0))
        self.comboBox.setFont(font4)
        self.comboBox.setLayoutDirection(Qt.LeftToRight)
        self.comboBox.setStyleSheet(u"QComboBox{\n"
"	background-color:transparent;\n"
"	color:rgb(90, 84, 84);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView::item {\n"
"	background-color:rgb(221, 215, 215);\n"
"	color:rgb(90, 84, 84);\n"
"}")
        self.comboBox.setEditable(False)
        self.comboBox.setFrame(False)

        self.horizontalLayout_3.addWidget(self.comboBox, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_3 = QFrame(self.f_translator)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_8.addWidget(self.frame_3)

        self.functionStack.addWidget(self.f_translator)
        self.f_notes = QWidget()
        self.f_notes.setObjectName(u"f_notes")
        self.functionStack.addWidget(self.f_notes)
        self.f_calculator = QWidget()
        self.f_calculator.setObjectName(u"f_calculator")
        self.functionStack.addWidget(self.f_calculator)

        self.horizontalLayout_2.addWidget(self.functionStack)


        self.verticalLayout_6.addWidget(self.functionFrame, 0, Qt.AlignVCenter)

        self.navbar = QFrame(self.MainFrame)
        self.navbar.setObjectName(u"navbar")
        self.navbar.setMinimumSize(QSize(0, 65))
        self.navbar.setMaximumSize(QSize(16777215, 65))
        self.navbar.setStyleSheet(u"background-color: rgb(90, 84, 84);")
        self.navbar.setFrameShape(QFrame.StyledPanel)
        self.navbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.navbar)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.calculatorbtn = QPushButton(self.navbar)
        self.calculatorbtn.setObjectName(u"calculatorbtn")
        self.calculatorbtn.setMinimumSize(QSize(50, 50))
        self.calculatorbtn.setMaximumSize(QSize(50, 50))
        self.calculatorbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.calculatorbtn.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	border: 1px solid;\n"
"	border-radius:20px;\n"
"	border-color:transparent;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(39, 36, 36);\n"
"}")
        self.calculatorbtn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.calculatorbtn)

        self.notesbtn = QPushButton(self.navbar)
        self.notesbtn.setObjectName(u"notesbtn")
        self.notesbtn.setMinimumSize(QSize(50, 50))
        self.notesbtn.setMaximumSize(QSize(50, 50))
        self.notesbtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.notesbtn.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	border: 1px solid;\n"
"	border-radius:20px;\n"
"	border-color:transparent;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(39, 36, 36);\n"
"}")
        self.notesbtn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.notesbtn)

        self.translatebtn = QPushButton(self.navbar)
        self.translatebtn.setObjectName(u"translatebtn")
        self.translatebtn.setMinimumSize(QSize(50, 50))
        self.translatebtn.setMaximumSize(QSize(50, 50))
        self.translatebtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.translatebtn.setStyleSheet(u"QPushButton{\n"
"	background-color:transparent;\n"
"	border: 1px solid;\n"
"	border-radius:20px;\n"
"	border-color:transparent;\n"
"}\n"
"QPushButton::hover{\n"
"	background-color: rgb(39, 36, 36);\n"
"}")
        self.translatebtn.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.translatebtn)


        self.verticalLayout_6.addWidget(self.navbar, 0, Qt.AlignBottom)


        self.verticalLayout_5.addWidget(self.MainFrame)

        self.mainStackW.addWidget(self.stackHome)

        self.verticalLayout_3.addWidget(self.mainStackW)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.mainStackW.setCurrentIndex(1)
        self.functionStack.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.introText.setText(QCoreApplication.translate("MainWindow", u"WORKBUDDY", None))
        self.introVersion.setText(QCoreApplication.translate("MainWindow", u"V.x", None))
        self.header.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Welcome back.", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Translate to:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"English", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Indonesian", None))

#if QT_CONFIG(tooltip)
        self.comboBox.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.comboBox.setPlaceholderText("")
        self.calculatorbtn.setText("")
        self.notesbtn.setText("")
        self.translatebtn.setText("")
    # retranslateUi

