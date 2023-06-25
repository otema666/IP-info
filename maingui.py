import ipinfo
import utils.utils as utils
import os
import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow, QLabel, QLineEdit, QCheckBox, QInputDialog
from PyQt5.QtCore import pyqtSlot, QUrl
from PyQt5.QtGui import QFont, QIcon, QDesktopServices
from PyQt5 import QtCore

# Variables
api_key = "f0b7f18a3e7541149ae064d21b443589"
access_token = '13e422b8b69e59'
handler = ipinfo.getHandler(access_token)
colorsd=["#03001C", "#150050", "#610094", "#C4DFDF", "#F8F6F4"]
colorsl=["#F8F6F4", "#C4DFDF", "#E3F4F4", "#150050", "#03001C"]
colors = []

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

class MainWindow(QMainWindow):
    def link(self, linkStr):

        QDesktopServices.openUrl(QUrl(linkStr))

    def __init__(self):
        super().__init__()

        self.dark = 0
        
        colors = colorsl
        self.setWindowIcon(QIcon(resource_path("logo.png")))
        self.setWindowTitle("IP Info")
        self.resize(600, 550)
        self.setStyleSheet("""
        background-color: #F8F6F4;
        """)
        
        self.label = QLabel("Escribe una IP o deja el espacio en blanco para poner tu IP actual:", self)
        self.label.move(30, 10)
        self.label.resize(540, 30)
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        self.label.setStyleSheet("""
        font-family: Helvetica; 
        """)

        self.textbox = QLineEdit(self)
        self.textbox.move(30, 30)
        self.textbox.resize(200, 30)
        self.textbox.setStyleSheet("""
        border: none;
        border-bottom: 2px solid #C4DFDF;
        """)

        self.button = QPushButton("Enter", self)
        self.button.move(250, 30)
        self.button.resize(100, 30)
        self.button.clicked.connect(self.on_click_enter)
        self.button.setStyleSheet("""
        QPushButton {
                border: none;
                border-radius: 5px;
                background-color: #C4DFDF;
        }
        QPushButton:pressed {
            background-color: #afc7c7;
        }
        """)

        self.darklight = QPushButton("Dark mode", self)
        self.darklight.move(530, 0)
        self.darklight.resize(70, 20)
        self.darklight.clicked.connect(self.on_click_color)
        self.darklight.setStyleSheet(f"""
        border: none;
        background-color: {colors[3]};
        color: {colors[1]};
        """)
        
        self.checkbox = QCheckBox('Show all info', self)
        self.checkbox.setGeometry(490, 30, 100, 30)
        self.checkbox.stateChanged.connect(self.on_check)
        check = self.checkbox.isChecked()
        print(check)

        dt = ["???" for a in range(12)]
        self.label = QLabel(f"""
        <style>
        ul {{
            list-style-type: none;
            font-size: 12pt;
        }}
        </style>
        <h2>Información básica:</h2>
        <ul><li>Hostname: {dt[0]}</li>
        <li>Organización: {dt[1]}</li></ul>
        <br>
        
        <h2>Seguridad:</h2>
        <ul><li>VPN: ???<li>
        <li>Proxy: ???</li>
        <li>TOR: ???</li>
        <li>Relay: ???</li></ul>
        <br>
        
        <h2>Geolocalización:</h2>
        <ul><li>País: {dt[2]}<li>
        <li>Región: {dt[3]}</li>
        <li>Ciudad: {dt[4]}</li>
        <li>CP: {dt[5]}</li>
        <li>Zona Horaria: {dt[6]}</li>
        <li>Google Maps: {dt[8]}</li>
        <li>Whatismyipaddress: <url>{dt[9]}</url></li></ul>
        """, self)
        self.label.move(30, 70)
        self.label.resize(540, 450)
        self.label.setAlignment(QtCore.Qt.AlignLeft)
        self.label.setStyleSheet("""
        background-color: #E3F4F4;
        border-radius: 5px;
        font-family: Helvetica;
        padding-left: 10px;
        padding-top: 10px;
        """)

        self.show()

    def on_check(self):
        pass

    @pyqtSlot()
    def on_click_color(self):
        if self.dark == 1:
            self.dark = 0
            colors = colorsl
            self.darklight.setText("Dark mode")
            self.button.setStyleSheet(f"""
            QPushButton {{
                border: none;
                border-radius: 5px;
                background-color: {colors[1]};
            }}
            QPushButton:pressed {{
                background-color: #afc7c7;
            }}
            """)
        elif self.dark == 0:
            self.dark = 1
            colors = colorsd
            self.darklight.setText("Light mode")
            self.button.setStyleSheet(f"""
            QPushButton {{
                border: none;
                border-radius: 5px;
                background-color: {colors[1]};
            }}
            QPushButton:pressed {{
                background-color: #25067a;
            }}
            """)
        
        self.setStyleSheet(f"""
        background-color: {colors[0]};
        color: {colors[4]};
        """)
        self.label.setStyleSheet(f"""
        background-color: {colors[2]};
        border-radius: 5px;
        font-family: Helvetica;
        padding-left: 10px;
        padding-top: 10px;
        """)
        self.darklight.setStyleSheet(f"""
        border: none;
        background-color: {colors[3]};
        color: {colors[1]};
        """)
        self.textbox.setStyleSheet(f"""
        border: none;
        border-bottom: 2px solid {colors[1]};
        """)

    @pyqtSlot()
    def on_click_enter(self):

        self.setWindowTitle("Loading...")
        if self.textbox.text() == "":
            self.textbox.setText(utils.getIp())
            if self.textbox.text() == "False":
                dt = ["error" for a in range(8)]
                return dt

        details = handler.getDetails(self.textbox.text())
        dt = utils.getDetails(details, self.textbox.text())

        self.label.linkActivated.connect(self.link)
        if self.checkbox.isChecked():
            self.label.setText(f"""
            <style>
            ul {{
                list-style-type: none;
                font-size: 12pt;
            }}
            </style>
            <h2>Información básica:</h2>
            <ul><li>Hostname: {dt[0]}</li>
            <li>Organización: {dt[1]}</li></ul>
            <br>
            
            <h2>Seguridad:</h2>
            <ul><li>VPN: {utils.verificar(self.textbox.text(), "vpn")}<li>
            <li>Proxy: {utils.verificar(self.textbox.text(), "pro")}</li>
            <li>TOR: {utils.verificar(self.textbox.text(), "tor")}</li>
            <li>Relay: {utils.verificar(self.textbox.text(), "rel")}</li></ul>
            <br>
            
            <h2>Geolocalización:</h2>
            <ul><li>Continente: {dt[11]["continent"]["name"]}<li>
            <li>País: {dt[2]} (Moneda: {dt[11]["country_currency"]["code"]}/{dt[11]["country_currency"]["symbol"]})<li>
            <li>Región: {dt[3]}</li>
            <li>Ciudad: {dt[4]}</li>
            <li>CP: {dt[5]}</li>
            <li>Zona Horaria: {dt[6]}</li>
            <li>Coordenadas: <a href="{dt[8]}">{dt[7]}</a></li>
            <li>Whatismyipaddress: <a href="{dt[9]}">{dt[10]}</a></li></ul>
            <br>
            """)
        
        else:
            self.label.setText(f"""
            <style>
            ul {{
                list-style-type: none;
                font-size: 12pt;
            }}
            </style>
            <h2>Información básica:</h2>
            <ul><li>Hostname: {dt[0]}</li>
            <li>Organización: {dt[1]}</li></ul>
            <br>
            
            <h2>Seguridad:</h2>
            <ul><li>VPN: {utils.verificar(self.textbox.text(), "vpn")}<li>
            <li>Proxy: {utils.verificar(self.textbox.text(), "pro")}</li>
            <li>TOR: {utils.verificar(self.textbox.text(), "tor")}</li>
            <li>Relay: {utils.verificar(self.textbox.text(), "rel")}</li></ul>
            <br>
            
            <h2>Geolocalización:</h2>
            <ul><li>País: {dt[2]}<li>
            <li>Región: {dt[3]}</li>
            <li>Ciudad: {dt[4]}</li>
            <li>CP: {dt[5]}</li>
            <li>Zona Horaria: {dt[6]}</li>
            <li>Coordenadas: <a href="{dt[8]}">{dt[7]}</a></li>
            <li>Whatismyipaddress: <a href="{dt[9]}">{dt[10]}</a></li></ul>
            <br>
            """)
        self.setWindowTitle("IP info")
  

app = QApplication([])
window = MainWindow()
window.show()

app.exec()