import sys
from tkinter import Widget
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QMainWindow
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QPixmap

from viginere import Viginere_Process
from playfair import Playfair_Process
from viginere_extended import Viginere_Extended_Process
from enigma import Enigma_Process

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
        widget.addWidget(extended)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Playfair(self):
        playfair = Playfair()
        widget.addWidget(playfair)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Enigma(self):
        enigma = Enigma()
        widget.addWidget(enigma)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Viginere(QMainWindow):
    def __init__(self):
        super(Viginere, self).__init__()
        loadUi("cipher.ui", self)

        self.label_6.setText("Viginere Cipher")
        self.pushButton_5.clicked.connect(self.Menu)
        self.pushButton.clicked.connect(self.Default)
        self.pushButton_2.clicked.connect(self.Grouped)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        # plaintext = self.textEdit.text()
        # key = self.textEdit_2.text()

    def Default(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = Viginere_Process(plaintext, key)

        self.textBrowser.setText(res[0])
        self.textBrowser_2.setText(res[2])

    def Grouped(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = Viginere_Process(plaintext, key)
        self.textBrowser.setText(res[1])
        self.textBrowser_2.setText(res[2])


class Extended(QMainWindow):
    def __init__(self):
        super(Extended, self).__init__()
        loadUi("cipher.ui", self)
        self.label_6.setText("Ext. Viginere Cipher")
        self.pushButton_5.clicked.connect(self.Menu)
        self.pushButton.clicked.connect(self.Default)
        self.pushButton_2.clicked.connect(self.Grouped)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Default(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = Viginere_Extended_Process(plaintext, key)
        self.textBrowser.setText(res[0])
        self.textBrowser_2.setText(res[2])

    def Grouped(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = Viginere_Extended_Process(plaintext, key)
        self.textBrowser.setText(res[1])
        self.textBrowser_2.setText(res[2])


class Playfair(QMainWindow):
    def __init__(self):
        super(Playfair, self).__init__()
        loadUi("cipher.ui", self)
        self.label_6.setText("Playfair Cipher")
        self.pushButton_5.clicked.connect(self.Menu)
        self.pushButton.clicked.connect(self.Default)
        self.pushButton_2.clicked.connect(self.Grouped)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Default(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = Playfair_Process(plaintext, key)

        self.textBrowser.setText(res[0])
        self.textBrowser_2.setText(res[2])

    def Grouped(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = Playfair_Process(plaintext, key)
        self.textBrowser.setText(res[1])
        self.textBrowser_2.setText(res[2])


class Enigma(QMainWindow):
    def __init__(self):
        super(Enigma, self).__init__()
        loadUi("cipher.ui", self)
        self.label_6.setText("Enigma Cipher")
        self.pushButton_5.clicked.connect(self.Menu)
        self.pushButton.clicked.connect(self.Default)
        self.pushButton_2.clicked.connect(self.Grouped)

    def Menu(self):
        menu = Menu()
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def Default(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = Enigma_Process(plaintext, key)
        self.textBrowser.setText(res[0])
        # self.textBrowser_2.setText(res[2])

    def Grouped(self):
        plaintext = self.textEdit.toPlainText()
        key = self.textEdit_2.toPlainText()
        res = Enigma_Process(plaintext, key)
        self.textBrowser.setText(res[1])
        # self.textBrowser_2.setText(res[2])


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
