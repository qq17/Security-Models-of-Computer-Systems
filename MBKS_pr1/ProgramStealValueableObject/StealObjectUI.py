# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'StealObjectUI.ui'
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
        MainWindow.resize(515, 371)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.select_hack_dir_btn = QPushButton(self.centralwidget)
        self.select_hack_dir_btn.setObjectName(u"select_hack_dir_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.select_hack_dir_btn.sizePolicy().hasHeightForWidth())
        self.select_hack_dir_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.select_hack_dir_btn)

        self.hack_dir_line = QLineEdit(self.centralwidget)
        self.hack_dir_line.setObjectName(u"hack_dir_line")

        self.horizontalLayout_3.addWidget(self.hack_dir_line)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.select_pub_dir_btn = QPushButton(self.centralwidget)
        self.select_pub_dir_btn.setObjectName(u"select_pub_dir_btn")
        sizePolicy.setHeightForWidth(self.select_pub_dir_btn.sizePolicy().hasHeightForWidth())
        self.select_pub_dir_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.select_pub_dir_btn)

        self.pub_dir_line = QLineEdit(self.centralwidget)
        self.pub_dir_line.setObjectName(u"pub_dir_line")

        self.horizontalLayout.addWidget(self.pub_dir_line)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.start_monitoring_btn = QPushButton(self.centralwidget)
        self.start_monitoring_btn.setObjectName(u"start_monitoring_btn")

        self.horizontalLayout_2.addWidget(self.start_monitoring_btn)

        self.stop_monitoring_btn = QPushButton(self.centralwidget)
        self.stop_monitoring_btn.setObjectName(u"stop_monitoring_btn")

        self.horizontalLayout_2.addWidget(self.stop_monitoring_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.status_lbl = QLabel(self.centralwidget)
        self.status_lbl.setObjectName(u"status_lbl")
        self.status_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.status_lbl)

        self.file_list = QListWidget(self.centralwidget)
        self.file_list.setObjectName(u"file_list")

        self.verticalLayout.addWidget(self.file_list)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 515, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0440\u0430\u0436\u0430 \u0434\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0445 \u0446\u0435\u043d\u043d\u044b\u0445 \u043e\u0431\u044a\u0435\u043a\u0442\u043e\u0432", None))
        self.select_hack_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043f\u0430\u043f\u043a\u0443 \u043d\u0430\u0440\u0443\u0448\u0438\u0442\u0435\u043b\u044f", None))
        self.select_pub_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043e\u0431\u0449\u0435\u0434\u043e\u0441\u0442\u0443\u043f\u043d\u0443\u044e \u043f\u0430\u043f\u043a\u0443", None))
        self.start_monitoring_btn.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0447\u0430\u0442\u044c \u043e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.stop_monitoring_btn.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0441\u0442\u0430\u043d\u043e\u0432\u0438\u0442\u044c \u043e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u043d\u0438\u0435", None))
        self.status_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0442\u0441\u043b\u0435\u0436\u0438\u0432\u0430\u043d\u0438\u0435 \u043d\u0435 \u0432\u0435\u0434\u0435\u0442\u0441\u044f", None))
    # retranslateUi

