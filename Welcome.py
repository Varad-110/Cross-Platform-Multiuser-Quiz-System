# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Welcome.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1200, 800)
        self.widget1 = QtWidgets.QWidget(Dialog)
        self.widget1.setGeometry(QtCore.QRect(0, 0, 1200, 800))
        self.widget1.setAutoFillBackground(False)
        self.widget1.setStyleSheet("QWidget#widget1{\n"
"background-color:qlineargradient(spread:pad, x1:0.527, y1:0.607955, x2:0.528, y2:1, stop:0 rgba(34, 71, 114, 255), stop:1 rgba(255, 255, 255, 255))}")
        self.widget1.setObjectName("widget1")
        self.Lable_1 = QtWidgets.QLabel(self.widget1)
        self.Lable_1.setGeometry(QtCore.QRect(360, 100, 480, 80))
        self.Lable_1.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 40pt \"MS Shell Dlg 2\";\n"
"")
        self.Lable_1.setTextFormat(QtCore.Qt.PlainText)
        self.Lable_1.setScaledContents(False)
        self.Lable_1.setAlignment(QtCore.Qt.AlignCenter)
        self.Lable_1.setObjectName("Lable_1")
        self.label_2 = QtWidgets.QLabel(self.widget1)
        self.label_2.setGeometry(QtCore.QRect(360, 175, 480, 40))
        self.label_2.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.HostButton = QtWidgets.QPushButton(self.widget1)
        self.HostButton.setGeometry(QtCore.QRect(435, 525, 330, 40))
        self.HostButton.setStyleSheet("color:rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(61, 128, 205);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"border-radius:20px")
        self.HostButton.setObjectName("HostButton")
        self.Join_Button1 = QtWidgets.QPushButton(self.widget1)
        self.Join_Button1.setGeometry(QtCore.QRect(435, 450, 330, 40))
        self.Join_Button1.setStyleSheet("color:rgb(255, 255, 255);\n"
"\n"
"background-color: rgb(61, 128, 205);\n"
"font: 20pt \"MS Shell Dlg 2\";\n"
"border-radius:20px")
        self.Join_Button1.setObjectName("Join_Button1")
        self.label_3 = QtWidgets.QLabel(self.widget1)
        self.label_3.setGeometry(QtCore.QRect(360, 215, 480, 40))
        self.label_3.setStyleSheet("color:rgb(255, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";\n"
"")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Lable_1.setText(_translate("Dialog", "Welcome"))
        self.label_2.setText(_translate("Dialog", "to the multiuser quiz apllication"))
        self.HostButton.setText(_translate("Dialog", "Host a Room"))
        self.Join_Button1.setText(_translate("Dialog", "Join Room"))
        self.label_3.setText(_translate("Dialog", "Join a Room Or Host a Room"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
