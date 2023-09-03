import sys
import os
from PySide2.QtWidgets import *
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

        self.cb = QApplication.clipboard()

        self.folder_btn.clicked.connect(self.select_folder)
        self.accesslvl_btn.clicked.connect(self.set_accesslvl)
        self.copyfile_btn.clicked.connect(self.select_file)
        self.destination_folder_btn.clicked.connect(self.select_destination)
        self.copy_btn.clicked.connect(self.copy_file)

        self.show()

    def select_folder(self):
        self.folder_path = QFileDialog.getExistingDirectory(self,
                                                            'Выберите папку',
                                                            dir='C:/Users/Master/Downloads/MBKS_pr4/MBKS_pr4')
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
                                                     dir='C:/Users/Master/Downloads/MBKS_pr4/MBKS_pr4')[0]
        print(self.file_path)
        if os.path.exists(self.file_path):
            self.copyfile_line.setText(self.file_path)

    def select_destination(self):
        self.destination_folder = QFileDialog.getExistingDirectory(self,
                                                            'Выберите папку назначения',
                                                            dir='C:/Users/Master/Downloads/MBKS_pr4/MBKS_pr4')
        if os.path.exists(self.destination_folder):
            self.destination_folder_line.setText(self.destination_folder)


    def copy_file(self):
        try:
            self.file_path = self.copyfile_line.text()
            dir = os.path.dirname(self.file_path)
            print(dir)
            if dir not in self.accesslvl.keys():
                print('netu')
                self.msg = QMessageBox(QMessageBox.Critical,
                                       'Ошибка',
                                       'Папке, в которой находится выбранный файл, не присвоен уровень конфиденциальности',
                                       parent=self)
                self.msg.setModal(False)
                self.msg.show()
                return
            if self.destination_folder not in self.accesslvl.keys():
                print('netu dest')
                self.msg = QMessageBox(QMessageBox.Critical,
                                       'Ошибка',
                                       'Папке назначения не присвоен уровень конфиденциальности',
                                       parent=self)
                self.msg.setModal(False)
                self.msg.show()
                return
            if self.accesslvl[dir] > self.accesslvl[self.destination_folder]:
                print('cant')
                self.msg = QMessageBox(QMessageBox.Critical,
                                       'Ошибка',
                                       'Папка, в которой находится выбранный файл, имеет больший уровень конфиденциальности чем папка назначения',
                                       parent=self)
                self.msg.setModal(False)
                self.msg.show()
                return
            f = open(self.file_path, 'r')
            with f:
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

def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()