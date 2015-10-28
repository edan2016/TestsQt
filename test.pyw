# coding: utf8
import sys

from PyQt4.QtCore import pyqtSlot
from PyQt4.QtGui import QApplication, QDialog
from PyQt4.uic import loadUiType

app = QApplication(sys.argv)
app.setApplicationName('untitled2')
form_class, base_class = loadUiType('test.ui')


class MainWindow(QDialog, form_class):
	def __init__(self, *args):
		super(MainWindow, self).__init__(*args)

		self.setupUi(self)


# -----------------------------------------------------#
form = MainWindow()
form.setWindowTitle('untitled2')
form.show()
sys.exit(app.exec_())
