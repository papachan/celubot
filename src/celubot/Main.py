'''
Created on Mar 19, 2013

@author: papachan
'''
import sys
import platform

from PySide import QtCore, QtGui
from PySide.QtGui import QApplication, QMainWindow, QMessageBox, QDesktopWidget
from gui.MainForm import Ui_MainWindow

__version__ = '0.0.1'


class MainWindow(QMainWindow):
    '''
    Main window widget
    '''

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    import sys

    if platform.system() == "Linux":
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        print "... running"
        sys.exit(app.exec_())
