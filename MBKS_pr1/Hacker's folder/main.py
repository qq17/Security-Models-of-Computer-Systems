import sys
from PySide2.QtWidgets import *
from CreateObjectUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.cb = QApplication.clipboard()

        self.copy_btn.clicked.connect(self.copy_file)
        self.write_btn.clicked.connect(self.write_to_file)

        self.show()

    def write_to_file(self):
        try:
            f = open(self.file_name_line.text(), 'w')
            with f:
                data = self.str_line.text()
                f.write(data)
                f.close()
        except FileNotFoundError:
            print('No such file')

    def copy_file(self):
        f = open(self.file_name_line.text(), 'r')
        with f:
            data = f.read()
            self.cb.clear(mode=self.cb.Clipboard)
            self.cb.setText(data, mode=self.cb.Clipboard)
            print(self.cb.text(mode=self.cb.Clipboard))
            f.close()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit(app.exec_())