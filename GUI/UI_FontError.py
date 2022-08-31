# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_FontErrorWindow(object):
    def setupUi(self, FontErrorWindow):
        if FontErrorWindow.objectName():
            FontErrorWindow.setObjectName(u"FontErrorWindow")
        FontErrorWindow.resize(300, 150)
        icon = QIcon()
        icon.addFile(u"circle_cut_nlmsd.png", QSize(), QIcon.Normal, QIcon.Off)
        FontErrorWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(FontErrorWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_background = QFrame(self.centralwidget)
        self.frame_background.setObjectName(u"frame_background")
        self.frame_background.setGeometry(QRect(-1, -1, 301, 151))
        self.frame_background.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(206, 230, 245);\n"
"  color:rgb(220, 220, 220);\n"
"}")
        self.frame_background.setFrameShape(QFrame.StyledPanel)
        self.frame_background.setFrameShadow(QFrame.Raised)
        self.text_static_error_information = QLabel(self.frame_background)
        self.text_static_error_information.setObjectName(u"text_static_error_information")
        self.text_static_error_information.setGeometry(QRect(23, 16, 261, 51))
        font = QFont()
        font.setPointSize(11)
        self.text_static_error_information.setFont(font)
        self.text_static_error_information.setStyleSheet(u"color: rgb(59, 59, 59);")
        self.text_static_error_information.setAlignment(Qt.AlignCenter)
        self.btn_exit = QPushButton(self.frame_background)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setGeometry(QRect(120, 91, 61, 31))
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
        FontErrorWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FontErrorWindow)

        QMetaObject.connectSlotsByName(FontErrorWindow)
    # setupUi

    def retranslateUi(self, FontErrorWindow):
        FontErrorWindow.setWindowTitle(QCoreApplication.translate("FontErrorWindow", u"Font not found", None))
        self.text_static_error_information.setText(QCoreApplication.translate("FontErrorWindow", u"\ud3f0\ud2b8\ub97c \uc124\uce58\ud55c \ud6c4 \ub2e4\uc2dc \uc2e4\ud589\ud574 \uc8fc\uc138\uc694.", None))
#if QT_CONFIG(tooltip)
        self.btn_exit.setToolTip(QCoreApplication.translate("FontErrorWindow", u"\uc758\uacac \ubcf4\ub0b4\uae30", None))
#endif // QT_CONFIG(tooltip)
        self.btn_exit.setText(QCoreApplication.translate("FontErrorWindow", u"O K", None))
    # retranslateUi

