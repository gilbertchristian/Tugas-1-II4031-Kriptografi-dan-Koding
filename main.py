import sys
from tkinter import Widget
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

import sqlite3
import os
import csv
import datetime

class Menu(QMainWindow):
    def __init__(self):
        super(Menu, self).__init__()
        loadUi("home.ui", self)
        self.pushButton_5.clicked.connect(self.Viginere)
        self.pushButton_6.clicked.connect(self.Extended)
        self.pushButton_7.clicked.connect(self.Playfair)
        self.pushButton_8.clicked.connect(self.Enigma)

    def Viginere(self):
        viginere = Viginere()
        widget.addWidget(viginere)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Extended(self):
        extended = Extended()

    def Playfair(self):
        playfair = Playfair()
    
    def Enigma(self):
        enigma = Enigma()

class Viginere(QMainWindow):
    def __init__(self):
        super(Viginere, self).__init__()
        loadUi("cipher.ui", self)
        # plaintext = self.textEdit.text()
        # key = self.textEdit_2.text()


# main
app = QApplication(sys.argv)
welcome = Menu()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")