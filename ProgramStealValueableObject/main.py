import sys
import os
from PySide2.QtWidgets import *
from PySide2.QtCore import QFileSystemWatcher
from StealObjectUI import Ui_MainWindow


class StealWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(StealWindow, self).__init__()
        self.setupUi(self)

        self.public_folder_path = 'C:/Users/Master/Downloads/MBKS_pr1/MBKS_pr1/Public folder'
        self.hacker_folder_path = 'C:/Users/Master/Downloads/MBKS_pr1/MBKS_pr1/Hacker\'s folder'

        self.cb = QApplication.clipboard()
        self.watcher = QFileSystemWatcher()
        self.watcher.addPath(self.public_folder_path)
        self.pub_dir_line.setText(self.public_folder_path)
        self.hack_dir_line.setText(self.hacker_folder_path)

        self.before = []

        self.select_hack_dir_btn.clicked.connect(self.select_hack_dir)
        self.select_pub_dir_btn.clicked.connect(self.select_pub_dir)
        self.start_monitoring_btn.clicked.connect(self.start_monitoring)
        self.stop_monitoring_btn.clicked.connect(self.stop_monitoring)

        self.show()

    def steal_file(self):
        print('directory changed')
        after = [fname for fname in os.listdir(self.public_folder_path)]
        added = [fname for fname in after if not fname in self.before]
        self.before = after
        for fname in added:
            try:
                f = open(self.public_folder_path + '/' + fname, 'r')
                with f:
                    data = f.read()
                    self.cb.clear(mode=self.cb.Clipboard)
                    self.cb.setText(data, mode=self.cb.Clipboard)
                    print(self.cb.text(mode=self.cb.Clipboard))
                    f.close()
                    self.file_list.addItem(fname)
                    try:
                        f = open(self.hacker_folder_path + '/' + fname, 'w')
                        with f:
                            data = self.cb.text()
                            f.write(data)
                            f.close()
                    except FileNotFoundError:
                        print('No such file')
            except Exception as e:
                print('problem', e)

    def select_hack_dir(self):
        self.hacker_folder_path = QFileDialog.getExistingDirectory(self,
                                                                   'Выберите папку для сохранения украденных файлов',
                                                                   dir='C:/Users/Master/Downloads/MBKS_pr1/MBKS_pr1/')
        if os.path.exists(self.hacker_folder_path):
            self.hack_dir_line.setText(self.hacker_folder_path)

    def select_pub_dir(self):
        self.public_folder_path = QFileDialog.getExistingDirectory(self,
                                                                   'Выберите общедоступную папку для отслеживания',
                                                                   dir='C:/Users/Master/Downloads/MBKS_pr1/MBKS_pr1/')
        if os.path.exists(self.public_folder_path):
            self.pub_dir_line.setText(self.public_folder_path)

    def start_monitoring(self):
        print(self.pub_dir_line.text())
        print(os.path.exists(self.pub_dir_line.text()))
        print(self.hack_dir_line.text())
        print(os.path.exists(self.hack_dir_line.text()))
        if not os.path.exists(self.pub_dir_line.text()) or not os.path.exists(self.hack_dir_line.text()):
            if not os.path.exists(self.pub_dir_line.text()):
                msg = QMessageBox(QMessageBox.Critical, 'Ошибка', 'Указанной общедоступной папки не существует',
                                  parent=self)
                msg.show()
            if not os.path.exists(self.hack_dir_line.text()):
                msg = QMessageBox(QMessageBox.Critical, 'Ошибка', 'Указанной папки нарушителя не существует',
                                  parent=self)
                msg.show()
            return

        self.public_folder_path = self.pub_dir_line.text()
        self.hacker_folder_path = self.hack_dir_line.text()

        self.watcher.removePaths(self.watcher.directories())
        self.watcher.addPath(self.public_folder_path)

        self.steal_file()
        self.watcher.directoryChanged.connect(self.steal_file)
        self.status_lbl.setText('Ведется отслеживание папки ' + self.public_folder_path)


    def stop_monitoring(self):
        self.watcher.directoryChanged.disconnect(self.steal_file)
        self.status_lbl.setText('Отслеживание не ведется')

def main():
    app = QApplication(sys.argv)
    mainWin = StealWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()