import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets

class WelcomeScreen(QDialog):
    def __init__(self):
        super(WelcomeScreen,self).__init__()
        loadUi("Welcome.ui",self)

        #join button on welcome screen
        self.Join_Button1.clicked.connect(self.gotoJoin)
        
        #host a room button on welcome screen
        self.HostButton.clicked.connect(self.gotocreate)

    def gotoJoin(self):
        login=JoinPage()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def gotocreate(self):
        create=createHost()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)

class JoinPage(QDialog):
    def __init__(self):
        super(JoinPage,self).__init__()
        loadUi("JoinPage.ui",self)

class createHost(QDialog):
    def __init__(self):
        super(createHost,self).__init__()
        loadUi("createRoom.ui",self)

#main
app=QApplication(sys.argv)
welcome=WelcomeScreen()
widget=QStackedWidget()
widget.setWindowTitle("Crossplatform Desktop Application")
widget.addWidget(welcome)
widget.setFixedHeight(800)
widget.setFixedWidth(1200)
widget.show()
try:
    sys.exit(app.exec())
except:
    print("Exiting.....")