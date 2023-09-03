import sys
import os
from PySide2.QtWidgets import *
from CreateObjectUI import Ui_MainWindow


class CreateCopyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(CreateCopyWindow, self).__init__()
        self.setupUi(self)

        self.public_folder_path = 'C:/Users/Master/Downloads/MBKS_pr1/MBKS_pr1/Public folder'
        self.private_folder_path = 'C:/Users/Master/Downloads/MBKS_pr1/MBKS_pr1/Private folder'
        self.file_path = self.private_folder_path + '/text_file.txt'

        self.cb = QApplication.clipboard()

        self.pub_dir_line.setText(self.public_folder_path)
        self.priv_dir_line.setText(self.private_folder_path)
        self.file_name_line.setText(self.file_path)

        self.select_priv_dir_btn.clicked.connect(self.select_priv_dir)
        self.select_pub_dir_btn.clicked.connect(self.select_pub_dir)
        self.select_file_btn.clicked.connect(self.select_priv_file)
        self.copy_btn.clicked.connect(self.copy_file)
        self.write_btn.clicked.connect(self.write_to_file)

        self.show()

    def write_to_file(self):
        try:
            f = open(self.file_name_line.text(), 'w')
            with f:
                data = self.text_edit.toPlainText()
                f.write(data)
                f.close()
        except FileNotFoundError:
            print('No such file')

    def copy_file(self):
        try:
            f = open(self.file_name_line.text(), 'r')
            with f:
                self.file_path = self.file_name_line.text()
                data = f.read()
                self.cb.clear(mode=self.cb.Clipboard)
                self.cb.setText(data, mode=self.cb.Clipboard)
                print(self.cb.text(mode=self.cb.Clipboard))
                f.close()
                try:
                    print(self.public_folder_path + '/' + self.file_path.split('/')[-1])
                    f = open(self.public_folder_path + '/' + self.file_path.split('/')[-1], 'w')
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
                                                                   dir='C:/Users/Master/Downloads/MBKS_pr1/MBKS_pr1/')
        if os.path.exists(self.private_folder_path):
            self.priv_dir_line.setText(self.private_folder_path)

    def select_pub_dir(self):
        self.public_folder_path = QFileDialog.getExistingDirectory(self,
                                                                   'Выберите общедоступную папку для отслеживания',
                                                                   dir='C:/Users/Master/Downloads/MBKS_pr1/MBKS_pr1/')
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
    mainWin = CreateCopyWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()