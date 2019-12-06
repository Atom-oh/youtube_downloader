# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLabel

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1600, 1200)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(1450, 20, 131, 241))
        self.buttonBox.setOrientation(QtCore.Qt.Vertical)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayoutWidget = QtWidgets.QWidget(Dialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 1421, 1091))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setEnabled(True)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 0, 1, 1)
        self.videoRadio = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.videoRadio.setObjectName("videoRadio")
        self.buttonGroup = QtWidgets.QButtonGroup(Dialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.videoRadio)
        self.gridLayout.addWidget(self.videoRadio, 3, 1, 1, 1)
        self.youtubeURL = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.youtubeURL.setObjectName("youtubeURL")
        self.gridLayout.addWidget(self.youtubeURL, 1, 1, 1, 1)
        self.outputText = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.outputText.setObjectName("outputText")
        self.gridLayout.addWidget(self.outputText, 6, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.mp3Radio = QtWidgets.QRadioButton(self.gridLayoutWidget)
        self.mp3Radio.setObjectName("mp3Radio")
        self.buttonGroup.addButton(self.mp3Radio)
        self.gridLayout.addWidget(self.mp3Radio, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(106, 1154, 91, 1051))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        # self.buttonBox.accepted.connect(Dialog.accept)
        # self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "저장위치"))
        self.videoRadio.setText(_translate("Dialog", "동영상"))
        self.label.setText(_translate("Dialog", "Youtube 주소"))
        self.mp3Radio.setText(_translate("Dialog", "mp3"))
        self.label_4.setText(_translate("Dialog", "저장형식"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    ui = Ui_Dialog()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())