# coding: utf8
import sys

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUiType

app = QApplication(sys.argv)
app.setApplicationName('untitled1')
form_class, base_class = loadUiType('test.ui')


class MainWindow(QDialog, form_class):
	def __init__(self, *args):
		super(MainWindow, self).__init__(*args)

		self.setupUi(self)


#-----------------------------------------------------#
form = MainWindow()
form.setWindowTitle('untitled1')
form.show()
sys.exit(app.exec_())