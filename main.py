# import PyQt5 library for UI
from PyQt5 import QtWidgets, uic

# initialise app UI
app = QtWidgets.QApplication([])
ui = uic.loadUi("WinUI.ui")
ui.setWindowTitle("Easy Text Editor")

def Open():
    address = ui.Address.displayText()
    file = open(address, 'r', encoding='utf-8')
    if not file: return
    _text = file.read()
    ui.Editor.setText(_text)
    ui.Name.setText(address)
    file.close()

def Save():
    name_raw = ui.Name.displayText()
    if '.' in name_raw and len(name_raw.split(".")[-1]) < 1:
        name = name_raw + ".txt"
    _file = open(name, 'w', encoding='utf-8')
    _text = ui.Editor.toPlainText()
    _file.write(_text)
    _file.close()

def Close():
    ui.Editor.setText("")
    ui.Name.setText("")

ui.Open.clicked.connect(Open)
ui.Save.clicked.connect(Save)
ui.Close.clicked.connect(Close)

ui.show()
app.exec()
