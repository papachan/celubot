import unittest
import Main
from PySide.QtTest import QTest
from PySide import __version_info__, __version__, QtCore


class TestWidget(unittest.TestCase):

    def setUp(self):
        pass

    def testReturnFunction(self):
        self.assertEqual(1, Main.returnFunction())


class ApplicationInstance(unittest.TestCase):

    def appDestroyed(self):
        self.assert_(True)

    def testInstanceObject(self):
        self.assert_(True)
        #d = Main.MainWindow()
        #self.assert_(d)


class CheckForVariablesTest(unittest.TestCase):

    def testVersions(self):
        self.assert_(__version_info__ >= (1, 0, 0))
        self.assert_(__version_info__ < (99, 99, 99))
        self.assert_(__version__)

        self.assert_(QtCore.__version_info__ >= (4, 5, 0))
        self.assert_(QtCore.__version__)

if __name__ == '__main__':
    unittest.main()
