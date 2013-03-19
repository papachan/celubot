import unittest
import sys
import Main
from PySide import QtGui
from PySide.QtTest import QTest
from PySide import __version_info__, __version__, QtCore


class MainApplicationInstance(unittest.TestCase):

    def setUp(self):
        self.app = QtGui.QApplication.instance()
        if not self.app:
            self.app = QtGui.QApplication(sys.argv)
        self.widget = Main.MainWindow()

    def appDestroyed(self):
        self.assert_(False)

    def testInstanceObject(self):
        self.assert_(self.widget)

    def testClickedButton(self):
        self.assert_(self.widget.ui.key1)


class CheckForVariablesTest(unittest.TestCase):

    def testVersions(self):
        self.assert_(__version_info__ >= (1, 0, 0))
        self.assert_(__version_info__ < (99, 99, 99))
        self.assert_(__version__)

        self.assert_(QtCore.__version_info__ >= (4, 5, 0))
        self.assert_(QtCore.__version__)

if __name__ == '__main__':
    unittest.main()
