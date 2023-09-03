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
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.str_lbl = QLabel(self.centralwidget)
        self.str_lbl.setObjectName(u"str_lbl")

        self.verticalLayout_2.addWidget(self.str_lbl)

        self.str_line = QLineEdit(self.centralwidget)
        self.str_line.setObjectName(u"str_line")

        self.verticalLayout_2.addWidget(self.str_line)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.file_name_lbl = QLabel(self.centralwidget)
        self.file_name_lbl.setObjectName(u"file_name_lbl")

        self.verticalLayout.addWidget(self.file_name_lbl)

        self.file_name_line = QLineEdit(self.centralwidget)
        self.file_name_line.setObjectName(u"file_name_line")

        self.verticalLayout.addWidget(self.file_name_line)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.write_btn = QPushButton(self.centralwidget)
        self.write_btn.setObjectName(u"write_btn")

        self.horizontalLayout.addWidget(self.write_btn)

        self.copy_btn = QPushButton(self.centralwidget)
        self.copy_btn.setObjectName(u"copy_btn")

        self.horizontalLayout.addWidget(self.copy_btn)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

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
        self.str_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u0440\u043e\u043a\u0430", None))
        self.file_name_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u0444\u0430\u0439\u043b\u0430", None))
        self.write_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0438\u0441\u0430\u0442\u044c", None))
        self.copy_btn.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

