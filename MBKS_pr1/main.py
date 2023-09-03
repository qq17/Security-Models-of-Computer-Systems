import sys
from PySide2.QtWidgets import QApplication
from ProgramCreateValueableObject import *
from ProgramCreateValueableObject.main import CreateCopyWindow
from ProgramStealValueableObject.main import StealWindow

app = QApplication(sys.argv)
steal_win = StealWindow()
create_copy_win = CreateCopyWindow()
sys.exit(app.exec_())