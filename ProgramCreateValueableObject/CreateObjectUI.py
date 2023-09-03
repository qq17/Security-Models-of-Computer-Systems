# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreateObjectUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(517, 308)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.select_priv_dir_btn = QPushButton(self.centralwidget)
        self.select_priv_dir_btn.setObjectName(u"select_priv_dir_btn")

        self.horizontalLayout_3.addWidget(self.select_priv_dir_btn)

        self.priv_dir_line = QLineEdit(self.centralwidget)
        self.priv_dir_line.setObjectName(u"priv_dir_line")

        self.horizontalLayout_3.addWidget(self.priv_dir_line)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.select_pub_dir_btn = QPushButton(self.centralwidget)
        self.select_pub_dir_btn.setObjectName(u"select_pub_dir_btn")

        self.horizontalLayout_4.addWidget(self.select_pub_dir_btn)

        self.pub_dir_line = QLineEdit(self.centralwidget)
        self.pub_dir_line.setObjectName(u"pub_dir_line")

        self.horizontalLayout_4.addWidget(self.pub_dir_line)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_file_btn = QPushButton(self.centralwidget)
        self.select_file_btn.setObjectName(u"select_file_btn")

        self.horizontalLayout_2.addWidget(self.select_file_btn)

        self.file_name_line = QLineEdit(self.centralwidget)
        self.file_name_line.setObjectName(u"file_name_line")

        self.horizontalLayout_2.addWidget(self.file_name_line)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.content_lbl = QLabel(self.centralwidget)
        self.content_lbl.setObjectName(u"content_lbl")
        self.content_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.content_lbl)

        self.text_edit = QTextEdit(self.centralwidget)
        self.text_edit.setObjectName(u"text_edit")

        self.verticalLayout_2.addWidget(self.text_edit)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.write_btn = QPushButton(self.centralwidget)
        self.write_btn.setObjectName(u"write_btn")

        self.horizontalLayout.addWidget(self.write_btn)

        self.copy_btn = QPushButton(self.centralwidget)
        self.copy_btn.setObjectName(u"copy_btn")

        self.horizontalLayout.addWidget(self.copy_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 517, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0437\u0434\u0430\u043d\u0438\u0435 \u0438 \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0446\u0435\u043d\u043d\u043e\u0433\u043e \u043e\u0431\u044a\u0435\u043a\u0442\u0430", None))
        self.select_priv_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0440\u0438\u0432\u0430\u0442\u043d\u0443\u044e \u043f\u0430\u043f\u043a\u0443", None))
        self.select_pub_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043e\u0431\u0449\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0443\u044e \u043f\u0430\u043f\u043a\u0443", None))
        self.select_file_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u0444\u0430\u0439\u043b", None))
        self.content_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0434\u0435\u0440\u0436\u0438\u043c\u043e\u0435 \u0444\u0430\u0439\u043b\u0430", None))
        self.write_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.copy_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c \u0432 \u043e\u0431\u0449\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0443\u044e \u043f\u0430\u043f\u043a\u0443", None))
    # retranslateUi

