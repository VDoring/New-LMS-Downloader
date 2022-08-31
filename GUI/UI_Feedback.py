# -*- coding: utf-8 -*-

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_FeedbackWindow(object):
    def setupUi(self, FeedbackWindow):
        if FeedbackWindow.objectName():
            FeedbackWindow.setObjectName(u"FeedbackWindow")
        FeedbackWindow.resize(480, 300)
        icon = QIcon()
        icon.addFile(u"circle_cut_nlmsd.png", QSize(), QIcon.Normal, QIcon.Off)
        FeedbackWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(FeedbackWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_static_1 = QFrame(self.centralwidget)
        self.frame_static_1.setObjectName(u"frame_static_1")
        self.frame_static_1.setGeometry(QRect(-1, -1, 481, 301))
        self.frame_static_1.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(206, 230, 245);\n"
"  color:rgb(220, 220, 220);\n"
"  border-radius: 5px;\n"
"}")
        self.frame_static_1.setFrameShape(QFrame.StyledPanel)
        self.frame_static_1.setFrameShadow(QFrame.Raised)
        self.frame_static_2 = QFrame(self.frame_static_1)
        self.frame_static_2.setObjectName(u"frame_static_2")
        self.frame_static_2.setGeometry(QRect(20, 60, 441, 221))
        self.frame_static_2.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"  color:rgb(220, 220, 220);\n"
"  border-radius: 20px;\n"
"}")
        self.frame_static_2.setFrameShape(QFrame.StyledPanel)
        self.frame_static_2.setFrameShadow(QFrame.Raised)
        self.btn_static_user_idea_send = QPushButton(self.frame_static_2)
        self.btn_static_user_idea_send.setObjectName(u"btn_static_user_idea_send")
        self.btn_static_user_idea_send.setGeometry(QRect(184, 180, 71, 31))
        font = QFont()
        font.setFamily(u"PF\uc2a4\ud0c0\ub354\uc2a4\ud2b8")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.btn_static_user_idea_send.setFont(font)
        self.btn_static_user_idea_send.setStyleSheet(u"QPushButton {\n"
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
        self.input_user_idea = QPlainTextEdit(self.frame_static_2)
        self.input_user_idea.setObjectName(u"input_user_idea")
        self.input_user_idea.setGeometry(QRect(40, 20, 361, 151))
        font1 = QFont()
        font1.setFamily(u"PF\uc2a4\ud0c0\ub354\uc2a4\ud2b8")
        font1.setPointSize(14)
        self.input_user_idea.setFont(font1)
        self.input_user_idea.setStyleSheet(u"background-color: rgb(241, 241, 241);\n"
"color: rgb(59, 59, 59);")
        self.text_user_idea_send_status = QLabel(self.frame_static_2)
        self.text_user_idea_send_status.setObjectName(u"text_user_idea_send_status")
        self.text_user_idea_send_status.setGeometry(QRect(261, 185, 171, 21))
        font2 = QFont()
        font2.setFamily(u"PF\uc2a4\ud0c0\ub354\uc2a4\ud2b8")
        font2.setPointSize(12)
        self.text_user_idea_send_status.setFont(font2)
        self.text_user_idea_send_status.setStyleSheet(u"color: rgb(92, 124, 170);")
        self.text_user_idea_send_status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.text_static_send_input_suggestions_idea = QLabel(self.frame_static_1)
        self.text_static_send_input_suggestions_idea.setObjectName(u"text_static_send_input_suggestions_idea")
        self.text_static_send_input_suggestions_idea.setGeometry(QRect(20, 10, 441, 51))
        font3 = QFont()
        font3.setFamily(u"PF\uc2a4\ud0c0\ub354\uc2a4\ud2b8")
        font3.setPointSize(20)
        self.text_static_send_input_suggestions_idea.setFont(font3)
        self.text_static_send_input_suggestions_idea.setStyleSheet(u"color: rgb(59, 59, 59);")
        self.text_static_send_input_suggestions_idea.setAlignment(Qt.AlignCenter)
        FeedbackWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(FeedbackWindow)

        QMetaObject.connectSlotsByName(FeedbackWindow)
    # setupUi

    def retranslateUi(self, FeedbackWindow):
        FeedbackWindow.setWindowTitle(QCoreApplication.translate("FeedbackWindow", u"Send Feedback", None))
#if QT_CONFIG(tooltip)
        self.btn_static_user_idea_send.setToolTip(QCoreApplication.translate("FeedbackWindow", u"\uc758\uacac \ubcf4\ub0b4\uae30", None))
#endif // QT_CONFIG(tooltip)
        self.btn_static_user_idea_send.setText(QCoreApplication.translate("FeedbackWindow", u"O  K  !", None))
        self.input_user_idea.setPlaceholderText(QCoreApplication.translate("FeedbackWindow", u"\uc5ec\uae30\uc5d0  \uc785\ub825\ud558\uc138\uc694  .  .  .", None))
        self.text_user_idea_send_status.setText(QCoreApplication.translate("FeedbackWindow", u"(\uc804\uc1a1 \uc644\ub8cc \uc5ec\ubd80 \uc785\ub825)", None))
        self.text_static_send_input_suggestions_idea.setText(QCoreApplication.translate("FeedbackWindow", u"Input     Suggestions  /  Idea", None))
    # retranslateUi

