# coding: utf-8
 
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from pyDownloader import getVideo,getAudio
import os
from win32com.shell import shell, shellcon

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("Youtube_main.ui")
        self.ui.show()
        self.initUI()

    def initUI(self):
        self.ui.outputButton.clicked.connect(self.on_click)
        self.ui.buttonBox.accepted.connect(self.accept)
        self.ui.buttonBox.rejected.connect(self.reject)
        self.ui.videoRadio.setChecked(True)
        self.ui.outputText.setText(shell.SHGetFolderPath(0, shellcon.CSIDL_PERSONAL, None, 0))
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if fileName:
            print(fileName)        
            self.ui.outputText.setText(fileName)

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        self.openFileNameDialog()
        
    @pyqtSlot()
    def accept(self):
        urls = self.ui.youtubeURL.toPlainText().splitlines()
        if( self.ui.videoRadio.isChecked()):
            getVideo(urls, outputPath=self.ui.outputText.text())
        else:
            getAudio(urls, outputPath=self.ui.outputText.text())
        
        
    @pyqtSlot()
    def reject(self):
        self.exit()
 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())