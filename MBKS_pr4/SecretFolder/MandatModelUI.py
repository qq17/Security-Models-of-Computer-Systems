# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MandatModelUI.ui'
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
        MainWindow.resize(728, 568)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.accesslvl_lbl = QLabel(self.centralwidget)
        self.accesslvl_lbl.setObjectName(u"accesslvl_lbl")

        self.verticalLayout.addWidget(self.accesslvl_lbl)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.folder_line = QLineEdit(self.centralwidget)
        self.folder_line.setObjectName(u"folder_line")

        self.horizontalLayout.addWidget(self.folder_line)

        self.folder_btn = QPushButton(self.centralwidget)
        self.folder_btn.setObjectName(u"folder_btn")

        self.horizontalLayout.addWidget(self.folder_btn)

        self.accesslvl_cb = QComboBox(self.centralwidget)
        self.accesslvl_cb.setObjectName(u"accesslvl_cb")

        self.horizontalLayout.addWidget(self.accesslvl_cb)

        self.accesslvl_btn = QPushButton(self.centralwidget)
        self.accesslvl_btn.setObjectName(u"accesslvl_btn")

        self.horizontalLayout.addWidget(self.accesslvl_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.accesslvl_tb = QTextBrowser(self.centralwidget)
        self.accesslvl_tb.setObjectName(u"accesslvl_tb")

        self.verticalLayout.addWidget(self.accesslvl_tb)

        self.copyfile_lbl = QLabel(self.centralwidget)
        self.copyfile_lbl.setObjectName(u"copyfile_lbl")

        self.verticalLayout.addWidget(self.copyfile_lbl)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.copyfile_line = QLineEdit(self.centralwidget)
        self.copyfile_line.setObjectName(u"copyfile_line")

        self.horizontalLayout_2.addWidget(self.copyfile_line)

        self.copyfile_btn = QPushButton(self.centralwidget)
        self.copyfile_btn.setObjectName(u"copyfile_btn")

        self.horizontalLayout_2.addWidget(self.copyfile_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.destination_lbl = QLabel(self.centralwidget)
        self.destination_lbl.setObjectName(u"destination_lbl")

        self.verticalLayout.addWidget(self.destination_lbl)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.destination_folder_line = QLineEdit(self.centralwidget)
        self.destination_folder_line.setObjectName(u"destination_folder_line")

        self.horizontalLayout_3.addWidget(self.destination_folder_line)

        self.destination_folder_btn = QPushButton(self.centralwidget)
        self.destination_folder_btn.setObjectName(u"destination_folder_btn")

        self.horizontalLayout_3.addWidget(self.destination_folder_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.copy_btn = QPushButton(self.centralwidget)
        self.copy_btn.setObjectName(u"copy_btn")

        self.verticalLayout.addWidget(self.copy_btn)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 728, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043d\u0434\u0430\u0442\u043d\u0430\u044f \u043c\u043e\u0434\u0435\u043b\u044c", None))
        self.accesslvl_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u043d\u0438\u0435 \u0443\u0440\u043e\u0432\u043d\u044f \u0434\u043e\u0441\u0442\u0443\u043f\u0430", None))
        self.folder_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.accesslvl_cb.setCurrentText("")
        self.accesslvl_btn.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0434\u0430\u0442\u044c", None))
        self.copyfile_lbl.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u0434\u043b\u044f \u043a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u044f", None))
        self.copyfile_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.destination_lbl.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0430\u043f\u043a\u0430 \u043d\u0430\u0437\u043d\u0430\u0447\u0435\u043d\u0438\u044f", None))
        self.destination_folder_btn.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c", None))
        self.copy_btn.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043f\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
    # retranslateUi

