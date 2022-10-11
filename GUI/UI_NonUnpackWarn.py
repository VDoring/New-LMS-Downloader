# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_NonUnpackWarnWindow(object):
    def setupUi(self, NonUnpackWarnWindow):
        if NonUnpackWarnWindow.objectName():
            NonUnpackWarnWindow.setObjectName(u"NonUnpackWarnWindow")
        NonUnpackWarnWindow.resize(400, 200)
        icon = QIcon()
        icon.addFile(u"circle_cut_nlmsd.png", QSize(), QIcon.Normal, QIcon.Off)
        NonUnpackWarnWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(NonUnpackWarnWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_background = QFrame(self.centralwidget)
        self.frame_background.setObjectName(u"frame_background")
        self.frame_background.setGeometry(QRect(-1, -1, 401, 201))
        self.frame_background.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(206, 230, 245);\n"
"  color:rgb(220, 220, 220);\n"
"}")
        self.frame_background.setFrameShape(QFrame.StyledPanel)
        self.frame_background.setFrameShadow(QFrame.Raised)
        self.text_static_error_information_1 = QLabel(self.frame_background)
        self.text_static_error_information_1.setObjectName(u"text_static_error_information_1")
        self.text_static_error_information_1.setGeometry(QRect(5, 40, 391, 31))
        font = QFont()
        font.setPointSize(12)
        self.text_static_error_information_1.setFont(font)
        self.text_static_error_information_1.setStyleSheet(u"color: rgb(59, 59, 59);")
        self.text_static_error_information_1.setAlignment(Qt.AlignCenter)
        self.btn_exit = QPushButton(self.frame_background)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(170, 141, 61, 31))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.btn_exit.setFont(font1)
        self.btn_exit.setStyleSheet(u"QPushButton {\n"
"	color: rgb(153, 197, 145);\n"
"	background-color: white;\n"
"	border: 4px solid rgb(153, 197, 145);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover:!pressed {\n"
"	color: white;\n"
"	background-color: rgb(153, 197, 145);\n"
"	border-radius: 5px;\n"
"}")
        self.text_static_error_information_2 = QLabel(self.frame_background)
        self.text_static_error_information_2.setObjectName(u"text_static_error_information_2")
        self.text_static_error_information_2.setGeometry(QRect(-5, 18, 401, 31))
        self.text_static_error_information_2.setFont(font)
        self.text_static_error_information_2.setStyleSheet(u"color: rgb(59, 59, 59);")
        self.text_static_error_information_2.setAlignment(Qt.AlignCenter)
        self.text_static_error_information_3 = QLabel(self.frame_background)
        self.text_static_error_information_3.setObjectName(u"text_static_error_information_3")
        self.text_static_error_information_3.setGeometry(QRect(5, 81, 391, 31))
        self.text_static_error_information_3.setFont(font)
        self.text_static_error_information_3.setStyleSheet(u"color: rgb(59, 59, 59);")
        self.text_static_error_information_3.setAlignment(Qt.AlignCenter)
        NonUnpackWarnWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(NonUnpackWarnWindow)

        QMetaObject.connectSlotsByName(NonUnpackWarnWindow)
    # setupUi

    def retranslateUi(self, NonUnpackWarnWindow):
        NonUnpackWarnWindow.setWindowTitle(QCoreApplication.translate("NonUnpackWarnWindow", u"File Location Warning", None))
        self.text_static_error_information_1.setText(QCoreApplication.translate("NonUnpackWarnWindow", u"\uc555\ucd95\uc744 \uc644\uc804\ud788 \ud47c \ub2e4\uc74c, \ub2e4\uc6b4\ub85c\ub354\ub97c \uc2e4\ud589\ud574\uc8fc\uc138\uc694.", None))
#if QT_CONFIG(tooltip)
        self.btn_exit.setToolTip(QCoreApplication.translate("NonUnpackWarnWindow", u"\uc758\uacac \ubcf4\ub0b4\uae30", None))
#endif // QT_CONFIG(tooltip)
        self.btn_exit.setText(QCoreApplication.translate("NonUnpackWarnWindow", u"O K", None))
        self.text_static_error_information_2.setText(QCoreApplication.translate("NonUnpackWarnWindow", u"\uc555\ucd95\ud55c \uc0c1\ud0dc\uc5d0\uc11c \ub2e4\uc6b4\ub85c\ub354\ub97c \uc2e4\ud589\ud558\uc9c0 \ub9c8\uc2ed\uc2dc\uc624.", None))
        self.text_static_error_information_3.setText(QCoreApplication.translate("NonUnpackWarnWindow", u"\ud30c\uc77c \uacbd\ub85c \uc624\ub958\uac00 \ubc1c\uc0dd\ud558\uae30 \ub54c\ubb38\uc785\ub2c8\ub2e4.", None))
    # retranslateUi

