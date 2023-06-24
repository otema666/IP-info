import ipinfo
import pprint
import requests
import os
import webbrowser
import utils
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QLineEdit, QVBoxLayout, QWidget, QInputDialog
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore

# Variables
api_key = "f0b7f18a3e7541149ae064d21b443589"
access_token = '13e422b8b69e59'
handler = ipinfo.getHandler(access_token)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("IP Info")
        self.resize(500, 500)
        
        self.textbox = QLineEdit(self)
        self.textbox.move(30, 20)
        self.textbox.resize(200, 30)

        self.button = QPushButton("Enter", self)
        self.button.move(250, 20)
        self.button.resize(100, 30)
        self.button.clicked.connect(self.on_click)

        self.label = QLabel('This is label'*100, self)
        self.label.move(30, 70)
        self.label.resize(440, 400)
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        self.label.setStyleSheet("border: 1px solid black;")

        self.show()

        
    @pyqtSlot()
    def on_click(self):
        details = handler.getDetails(self.textbox.text())
        utils.getdetails(details)
  

app = QApplication([])
window = MainWindow()
window.show()

app.exec()