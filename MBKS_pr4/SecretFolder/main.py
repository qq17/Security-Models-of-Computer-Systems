import sys
import os
from PySide2.QtWidgets import *
from PySide2.QtCore import QAbstractTableModel, Qt
from MandatModelUI import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.accesslvl_cb.addItems(['','TopSecret', 'Secret', 'NonSecret'])
        self.accesslvl = {}

        self.folder_path = ''
        self.destination_folder = ''
        self.file_path = ''
        # self.private_folder_path = 'C:/Users/Master/PycharmProjects/MBKS_pr1/Private folder'
        # self.file_path = self.private_folder_path + '/text_file.txt'

        self.cb = QApplication.clipboard()

        # self.pub_dir_line.setText(self.public_folder_path)
        # self.priv_dir_line.setText(self.private_folder_path)
        # self.file_name_line.setText(self.file_path)

        self.folder_btn.clicked.connect(self.select_folder)
        self.accesslvl_btn.clicked.connect(self.set_accesslvl)
        self.copyfile_btn.clicked.connect(self.select_file)
        self.destination_folder_btn.clicked.connect(self.select_destination)
        self.copy_btn.clicked.connect(self.copy_file)
        # self.write_btn.clicked.connect(self.write_to_file)

        self.show()

    def select_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self,
                                                            'Выберите папку',
                                                            dir='C:/Users/Master/PycharmProjects/MBKS_pr4')
        if os.path.exists(self.folder_path):
            self.folder_line.setText(self.folder_path)

    def set_accesslvl(self):
        if os.path.exists(self.folder_line.text()):
            print(self.accesslvl_cb.currentText())
            if self.accesslvl_cb.currentText() == 'TopSecret':
                self.accesslvl_tb.append(self.folder_line.text() + ' - TopSecret')
                self.accesslvl[self.folder_line.text()] = 2
            if self.accesslvl_cb.currentText() == 'Secret':
                self.accesslvl_tb.append(self.folder_line.text() + ' - Secret')
                self.accesslvl[self.folder_line.text()] = 1
            if self.accesslvl_cb.currentText() == 'NonSecret':
                self.accesslvl_tb.append(self.folder_line.text() + ' - NonSecret')
                self.accesslvl[self.folder_line.text()] = 0

        print(self.accesslvl)

    def select_file(self):
        self.file_path = QFileDialog.getOpenFileName(self,
                                                     'Выберите файл',
                                                     dir='C:/Users/Master/PycharmProjects/MBKS_pr4')[0]
        print(self.file_path)
        if os.path.exists(self.file_path):
            self.copyfile_line.setText(self.file_path)

    def select_destination(self):
        self.destination_folder = QFileDialog.getExistingDirectory(self,
                                                            'Выберите папку назначения',
                                                            dir='C:/Users/Master/PycharmProjects/MBKS_pr4')
        if os.path.exists(self.destination_folder):
            self.destination_folder_line.setText(self.destination_folder)


    def copy_file(self):
        try:
            f = open(self.copyfile_line.text(), 'r')
            with f:
                self.file_path = self.copyfile_line.text()
                data = f.read()
                self.cb.clear(mode=self.cb.Clipboard)
                self.cb.setText(data, mode=self.cb.Clipboard)
                print(self.cb.text(mode=self.cb.Clipboard))
                f.close()
                try:
                    print(self.destination_folder + '/' + self.file_path.split('/')[-1])
                    f = open(self.destination_folder + '/' + self.file_path.split('/')[-1], 'w')
                    with f:
                        data = self.cb.text()
                        f.write(data)
                        f.close()
                except FileNotFoundError:
                    print('No such file')
        except Exception as e:
            print('problem', e)

    def select_priv_dir(self):
        self.private_folder_path = QFileDialog.getExistingDirectory(self,
                                                                   'Выберите личную папку',
                                                                   dir='C:/Users/Master/PycharmProjects/MBKS_pr1')
        if os.path.exists(self.private_folder_path):
            self.priv_dir_line.setText(self.private_folder_path)

    def select_pub_dir(self):
        self.public_folder_path = QFileDialog.getExistingDirectory(self,
                                                                   'Выберите общедоступную папку для отслеживания',
                                                                   dir='C:/Users/Master/PycharmProjects/MBKS_pr1')
        if os.path.exists(self.public_folder_path):
            self.pub_dir_line.setText(self.public_folder_path)

    def select_priv_file(self):
        self.file_path = QFileDialog.getOpenFileName(self, 'Выберите файл', dir=self.private_folder_path)[0]
        print(self.file_path)
        if os.path.exists(self.file_path):
            self.file_name_line.setText(self.file_path)
            f = open(self.file_path, 'r')
            with f:
                data = f.read()
                self.text_edit.setText(data)
                f.close()

def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()