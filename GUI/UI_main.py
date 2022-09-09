# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 400)
        icon = QIcon()
        icon.addFile(u"circle_cut_nlmsd.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_static_1 = QFrame(self.centralwidget)
        self.frame_static_1.setObjectName(u"frame_static_1")
        self.frame_static_1.setGeometry(QRect(-1, -1, 641, 401))
        self.frame_static_1.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(114, 154, 211);\n"
"  color:rgb(220, 220, 220);\n"
"  border-radius: 5px;\n"
"}")
        self.frame_static_1.setFrameShape(QFrame.StyledPanel)
        self.frame_static_1.setFrameShadow(QFrame.Raised)
        self.frame_static_2 = QFrame(self.frame_static_1)
        self.frame_static_2.setObjectName(u"frame_static_2")
        self.frame_static_2.setGeometry(QRect(20, 20, 601, 361))
        self.frame_static_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(206, 230, 245);\n"
"  color:rgb(220, 220, 220);\n"
"  border-radius: 5px;\n"
"}")
        self.frame_static_2.setFrameShape(QFrame.StyledPanel)
        self.frame_static_2.setFrameShadow(QFrame.Raised)
        self.frame_static_3 = QFrame(self.frame_static_2)
        self.frame_static_3.setObjectName(u"frame_static_3")
        self.frame_static_3.setGeometry(QRect(20, 80, 561, 261))
        self.frame_static_3.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"  color:rgb(220, 220, 220);\n"
"  border-radius: 20px;\n"
"}")
        self.frame_static_3.setFrameShape(QFrame.StyledPanel)
        self.frame_static_3.setFrameShadow(QFrame.Raised)
        self.text_static_videolink = QLabel(self.frame_static_3)
        self.text_static_videolink.setObjectName(u"text_static_videolink")
        self.text_static_videolink.setGeometry(QRect(20, 30, 111, 31))
        font = QFont()
        font.setFamily(u"PF\uc2a4\ud0c0\ub354\uc2a4\ud2b8")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.text_static_videolink.setFont(font)
        self.text_static_videolink.setStyleSheet(u"color: rgb(114, 154, 211);")
        self.text_static_videolink.setAlignment(Qt.AlignCenter)
        self.text_static_filename = QLabel(self.frame_static_3)
        self.text_static_filename.setObjectName(u"text_static_filename")
        self.text_static_filename.setGeometry(QRect(20, 80, 101, 31))
        font1 = QFont()
        font1.setFamily(u"PF\uc2a4\ud0c0\ub354\uc2a4\ud2b8")
        font1.setPointSize(14)
        self.text_static_filename.setFont(font1)
        self.text_static_filename.setStyleSheet(u"color: rgb(114, 154, 211);")
        self.text_static_filename.setAlignment(Qt.AlignCenter)
        self.btn_static_video_download_start = QPushButton(self.frame_static_3)
        self.btn_static_video_download_start.setObjectName(u"btn_static_video_download_start")
        self.btn_static_video_download_start.setEnabled(True)
        self.btn_static_video_download_start.setGeometry(QRect(237, 210, 91, 31))
        font2 = QFont()
        font2.setFamily(u"PF\uc2a4\ud0c0\ub354\uc2a4\ud2b8")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.btn_static_video_download_start.setFont(font2)
        self.btn_static_video_download_start.setStyleSheet(u"QPushButton {\n"
"	color: rgb(153, 197, 145);\n"
"	background-color: white;\n"
"	border: 4px solid rgb(153, 197, 145);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover:!pressed {\n"
"	color: white;\n"
"	background-color: rgb(153, 197, 145);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:disabled {\n"
"	color: white;\n"
"	background-color: rgb(153, 197, 145);\n"
"	border-radius: 5px;\n"
"}")
        self.progressbar_video_download = QProgressBar(self.frame_static_3)
        self.progressbar_video_download.setObjectName(u"progressbar_video_download")
        self.progressbar_video_download.setEnabled(True)
        self.progressbar_video_download.setGeometry(QRect(48, 170, 471, 23))
        self.progressbar_video_download.setStyleSheet(u"QProgressBar {\n"
"	background-color: rgb(233, 234, 233);\n"
"	color: rgb(82, 82, 82);\n"
"	border-style: none;\n"
"	border-radius:10px;\n"
"	text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius: 10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.511, x2:1, y2:0.534091, stop:0.636364 rgba(206, 230, 245, 255), stop:1 rgba(138, 187, 255, 255));\n"
"}")
        self.progressbar_video_download.setValue(0)
        self.btn_static_github_link = QPushButton(self.frame_static_3)
        self.btn_static_github_link.setObjectName(u"btn_static_github_link")
        self.btn_static_github_link.setGeometry(QRect(6, 225, 30, 30))
        self.btn_static_github_link.setMaximumSize(QSize(30, 30))
        font3 = QFont()
        font3.setFamily(u"Social Media Circled")
        font3.setPointSize(20)
        self.btn_static_github_link.setFont(font3)
        self.btn_static_github_link.setStyleSheet(u"QPushButton {\n"
"	color: rgba(114, 154, 211, 255);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton:hover:!pressed {\n"
"	color: rgba(78, 90, 94, 255);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.btn_static_mail_send = QPushButton(self.frame_static_3)
        self.btn_static_mail_send.setObjectName(u"btn_static_mail_send")
        self.btn_static_mail_send.setGeometry(QRect(38, 226, 30, 30))
        self.btn_static_mail_send.setMaximumSize(QSize(30, 30))
        self.btn_static_mail_send.setFont(font3)
        self.btn_static_mail_send.setStyleSheet(u"QPushButton {\n"
"	color: rgba(114, 154, 211, 255);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}\n"
"QPushButton:hover:!pressed {\n"
"	color: rgba(78, 90, 94, 255);\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"}")
        self.text_video_download_status = QLabel(self.frame_static_3)
        self.text_video_download_status.setObjectName(u"text_video_download_status")
        self.text_video_download_status.setGeometry(QRect(8, 148, 541, 21))
        font4 = QFont()
        font4.setFamily(u"PF\uc2a4\ud0c0\ub354\uc2a4\ud2b8")
        font4.setPointSize(12)
        self.text_video_download_status.setFont(font4)
        self.text_video_download_status.setStyleSheet(u"color: rgb(92, 124, 170);")
        self.text_video_download_status.setAlignment(Qt.AlignCenter)
        self.input_videolink = QLineEdit(self.frame_static_3)
        self.input_videolink.setObjectName(u"input_videolink")
        self.input_videolink.setGeometry(QRect(160, 29, 361, 31))
        self.input_videolink.setFont(font4)
        self.input_videolink.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(206, 230, 245,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.input_filename = QLineEdit(self.frame_static_3)
        self.input_filename.setObjectName(u"input_filename")
        self.input_filename.setGeometry(QRect(160, 80, 361, 31))
        self.input_filename.setFont(font4)
        self.input_filename.setStyleSheet(u"background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(206, 230, 245,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.text_static_nlmsd = QLabel(self.frame_static_2)
        self.text_static_nlmsd.setObjectName(u"text_static_nlmsd")
        self.text_static_nlmsd.setGeometry(QRect(40, 20, 501, 51))
        font5 = QFont()
        font5.setFamily(u"PF\uc2a4\ud0c0\ub354\uc2a4\ud2b8")
        font5.setPointSize(32)
        self.text_static_nlmsd.setFont(font5)
        self.text_static_nlmsd.setStyleSheet(u"color: rgb(59, 59, 59);")
        self.text_static_nlmsd.setAlignment(Qt.AlignCenter)
        self.text_static_nlmsd_ver = QLabel(self.frame_static_2)
        self.text_static_nlmsd_ver.setObjectName(u"text_static_nlmsd_ver")
        self.text_static_nlmsd_ver.setGeometry(QRect(525, 41, 70, 31))
        self.text_static_nlmsd_ver.setFont(font1)
        self.text_static_nlmsd_ver.setStyleSheet(u"color: rgb(59, 59, 59);")
        self.text_static_nlmsd_ver.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"New LMS Downloader GUI - by VDoring", None))
#if QT_CONFIG(tooltip)
        self.text_static_videolink.setToolTip(QCoreApplication.translate("MainWindow", u"\ub2e4\uc6b4\ub85c\ub4dc\ud560 \ucf58\ud150\uce20 \ub9c1\ud06c\ub97c \uc785\ub825\ud558\uc138\uc694", None))
#endif // QT_CONFIG(tooltip)
        self.text_static_videolink.setText(QCoreApplication.translate("MainWindow", u"Video   Link", None))
#if QT_CONFIG(tooltip)
        self.text_static_filename.setToolTip(QCoreApplication.translate("MainWindow", u"\uc6d0\ud558\ub294 \ud30c\uc77c \uc774\ub984\uc744 \uc785\ub825\ud558\uc138\uc694", None))
#endif // QT_CONFIG(tooltip)
        self.text_static_filename.setText(QCoreApplication.translate("MainWindow", u"File   Name", None))
#if QT_CONFIG(tooltip)
        self.btn_static_video_download_start.setToolTip(QCoreApplication.translate("MainWindow", u"\ub2e4\uc6b4\ub85c\ub4dc \uc2dc\uc791!", None))
#endif // QT_CONFIG(tooltip)
        self.btn_static_video_download_start.setText(QCoreApplication.translate("MainWindow", u"S T A R T", None))
#if QT_CONFIG(tooltip)
        self.btn_static_github_link.setToolTip(QCoreApplication.translate("MainWindow", u"\ud648\ud398\uc774\uc9c0 \uac00\uae30", None))
#endif // QT_CONFIG(tooltip)
        self.btn_static_github_link.setText(QCoreApplication.translate("MainWindow", u")", None))
#if QT_CONFIG(tooltip)
        self.btn_static_mail_send.setToolTip(QCoreApplication.translate("MainWindow", u"\uac74\uc758\ud558\uae30", None))
#endif // QT_CONFIG(tooltip)
        self.btn_static_mail_send.setText(QCoreApplication.translate("MainWindow", u"k", None))
        self.text_video_download_status.setText(QCoreApplication.translate("MainWindow", u"(\ud604 \ub2e4\uc6b4\ub85c\ub4dc \uc0c1\ud0dc \uba54\uc2dc\uc9c0 \uc785\ub825)", None))
        self.text_static_nlmsd.setText(QCoreApplication.translate("MainWindow", u"New   LMS    Downloader", None))
        self.text_static_nlmsd_ver.setText(QCoreApplication.translate("MainWindow", u"v2.0", None))
    # retranslateUi

