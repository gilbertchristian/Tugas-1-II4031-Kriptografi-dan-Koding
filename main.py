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
        widget.addWigdet(viginere)
        widget.setCurrentIndex(widget.currentIndex() + 1)

class Viginere(QMainWindow):
        def __init__(self):
        super(Viginere, self).__init__()
        loadUi("cipher.ui", self)
        plaintext = self.textEdit.text()
        key = self.textEdit_2.text()