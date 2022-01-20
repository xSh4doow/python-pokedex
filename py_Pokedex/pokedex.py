import PyQt5
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import pandas as pd
import sys
import urllib.request
import requests
from pyqt5_plugins.examplebuttonplugin import QtGui


class Pokedex(QWidget):

    def __init__(self):
        super(Pokedex, self).__init__()
        self.inUI()

    def inUI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        self.df = pd.read_json("PKMN.json")
        self.df = self.df.set_index(["#"])

        self.dropdown = QComboBox(self)
        self.names = self.df['Name'].values
        self.dropdown.addItems(self.names)
        grid.addWidget(self.dropdown, 0,0,1,1)

        self.btn = QPushButton("Search", self)
        self.btn.clicked.connect(self.runSearch)
        grid.addWidget(self.btn, 0,1,1,1)

        self.img = QLabel(self)
        grid.addWidget(self.img, 1, 1, 1, 1)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setText('\nName:\n\nType:\n\nHP:\n\nAttack\n\nSp. Attack\n\n Defense:\n\nSp. Defense:\n\nSpeed:\n\nTotal:')
        self.label.setAlignment(Qt.AlignLeft)
        grid.addWidget(self.label, 1, 0, 1, 1)

        self.resize(500,250)
        self.setWindowTitle("Pokedex by Pedro Rocha")
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.show()


    def runSearch(self):

        index = self.dropdown.currentIndex()
        val = self.names[index]
        cond = self.df["Name"] == val

        # Image
        base = 'https://img.pokemondb.net/artwork/'
        img_url = base + str(val).lower() + ".jpg"
        image = QtGui.QImage()
        image.loadFromData(requests.get(img_url).content)
        self.img.setPixmap(QtGui.QPixmap(image))

        # Set values
        name = 'Name:\t\t' + val + '\n\n'
        ty = 'Type:\t\t' + ''.join(self.df[cond]['Type'].values[0]) + '\n\n'
        hp = 'HP:\t\t' + str(self.df[cond]['HP'].values[0]) + '\n\n'
        atk = 'Attack:\t\t' + str(self.df[cond]['Attack'].values[0]) + '\n\n'
        satk = 'Sp. Attack:\t' + str(self.df[cond]['Sp. Atk'].values[0]) + '\n\n'
        deff = 'Defense:\t' + str(self.df[cond]['Defense'].values[0]) + '\n\n'
        sdef = 'Sp. Defense:\t' + str(self.df[cond]['Sp. Def'].values[0]) + '\n\n'
        speed = 'Speed:\t\t' + str(self.df[cond]['Speed'].values[0]) + '\n\n'
        total = 'Total:\t\t' + str(self.df[cond]['Total'].values[0]) + '\n\n'

        # Add text
        final = name + ty + hp + atk + satk + deff + sdef + speed + total
        self.label.setText(final)
        print("adding text")

def main():
    app = QApplication(sys.argv)
    gui = Pokedex()
    sys.exit(app.exec_())
