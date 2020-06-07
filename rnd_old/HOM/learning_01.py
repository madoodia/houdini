# madoodia@gmail.com
# ------------------
import hou

def pringChilds(node):
	for n in node.children():
		print n


# Making window with PySide2
from PySide2 import QtCore, QtWidgets

stylesheet = hou.qt.styleSheet()

class TestWindow(QtWidgets.QWidget):
    """"""
    def __init__(self, parent=None):
        """"""
        super(TestWindow, self).__init__(parent)

        hbox = QtWidgets.QHBoxLayout(self)

        btn = QtWidgets.QPushButton("Hello")
        hbox.addWidget(btn)

        self.setWindowFlags(QtCore.Qt.Window)

mainWindow = hou.qt.mainWindow()
win = TestWindow(mainWindow)
win.setStyleSheet(stylesheet)

win.show()

# or
from PySide2 import QtCore, QtWidgets

# Same Color as houdini
class TestWindow(QtWidgets.QWidget):
    """"""
    def __init__(self, parent=None):
        """"""
        QtWidgets.QWidget.__init__(self, parent)

        hbox = QtWidgets.QHBoxLayout(self)

        btn = QtWidgets.QPushButton("Hello")
        hbox.addWidget(btn)

        self.setWindowFlags(QtCore.Qt.Window)
        #self.setStyleSheet(hou.qt.styleSheet())
        self.setProperty("houdiniStyle", True)
        self.resize(200, 100)

win = TestWindow(hou.qt.mainWindow())
win.show()

# other sample
import os, sys
from hutil.Qt.QtCore import *
from hutil.Qt.QtGui import *
from hutil.Qt.QtWidgets import *
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()
    def initUI(self):
        self.setStyleSheet(hou.qt.styleSheet())
        self.setProperty("houdiniStyle", True)
        self.setWindowTitle('Houdini16 Python Test')
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        g_layout = QVBoxLayout()
        layout = QFormLayout()
        main_widget.setLayout(g_layout)
        self.parm = QSpinBox()
        self.parm.setValue(30)
        layout.addRow('Parameter', self.parm)
        self.exec_btn = QPushButton('Button')
        g_layout.addLayout(layout)
        g_layout.addWidget(self.exec_btn)
w = MainWindow()
w.show()

