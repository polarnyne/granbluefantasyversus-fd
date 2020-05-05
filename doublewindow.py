from PyQt5 import QtCore, QtGui, QtWidgets
from granwidget import Ui_Form, iBeelzebub, iCharlotta, iDjeeta, iFerry, iGran, iKatalina, iLadiva, iLancelot, iLowain, iMetera, iNarmaya, iPercival, iSoriz, iVaseraga, iZeta, iZooey
import granqt

transporting_data = None

def transportData(chara):
    global transporting_data
    transporting_data = str(granqt.fighters[chara].get_framedata())

class Ui_MainWindow(object):
    
    def openwindow(self):
        
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(645, 766)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.bBeelzebub = QtWidgets.QLabel(self.centralwidget)
        self.bBeelzebub.setGeometry(QtCore.QRect(10, 10, 151, 151))
        self.bBeelzebub.setText("")
        self.bBeelzebub.setPixmap(QtGui.QPixmap("resources/finals/beelzebub.png"))
        self.bBeelzebub.setObjectName("bBeelzebub")
        
        self.bCharlotta = QtWidgets.QLabel(self.centralwidget)
        self.bCharlotta.setGeometry(QtCore.QRect(170, 10, 151, 151))
        self.bCharlotta.setText("")
        self.bCharlotta.setPixmap(QtGui.QPixmap("resources/finals/charlotta.png"))
        self.bCharlotta.setObjectName("bCharlotta")
        
        self.bDjeeta = QtWidgets.QLabel(self.centralwidget)
        self.bDjeeta.setGeometry(QtCore.QRect(330, 10, 151, 151))
        self.bDjeeta.setText("")
        self.bDjeeta.setPixmap(QtGui.QPixmap("resources/finals/djeeta.png"))
        self.bDjeeta.setObjectName("bDjeeta")
        
        self.bFerry = QtWidgets.QLabel(self.centralwidget)
        self.bFerry.setGeometry(QtCore.QRect(490, 10, 151, 151))
        self.bFerry.setText("")
        self.bFerry.setPixmap(QtGui.QPixmap("resources/finals/ferry.png"))
        self.bFerry.setObjectName("bFerry")
        
        self.bGran = QtWidgets.QLabel(self.centralwidget)
        self.bGran.setGeometry(QtCore.QRect(10, 190, 151, 151))
        self.bGran.setText("")
        self.bGran.setPixmap(QtGui.QPixmap("resources/finals/gran.png"))
        self.bGran.setObjectName("bGran")
        
        self.bKatalina = QtWidgets.QLabel(self.centralwidget)
        self.bKatalina.setGeometry(QtCore.QRect(170, 190, 151, 151))
        self.bKatalina.setText("")
        self.bKatalina.setPixmap(QtGui.QPixmap("resources/finals/katalina.png"))
        self.bKatalina.setObjectName("bKatalina")
        
        self.bLadiva = QtWidgets.QLabel(self.centralwidget)
        self.bLadiva.setGeometry(QtCore.QRect(330, 190, 151, 151))
        self.bLadiva.setText("")
        self.bLadiva.setPixmap(QtGui.QPixmap("resources/finals/ladiva.png"))
        self.bLadiva.setObjectName("bLadiva")
        
        self.bLancelot = QtWidgets.QLabel(self.centralwidget)
        self.bLancelot.setGeometry(QtCore.QRect(490, 190, 151, 151))
        self.bLancelot.setText("")
        self.bLancelot.setPixmap(QtGui.QPixmap("resources/finals/lancelot.png"))
        self.bLancelot.setObjectName("bLancelot")
        
        self.bLowain = QtWidgets.QLabel(self.centralwidget)
        self.bLowain.setGeometry(QtCore.QRect(10, 370, 151, 151))
        self.bLowain.setText("")
        self.bLowain.setPixmap(QtGui.QPixmap("resources/finals/lowain.png"))
        self.bLowain.setObjectName("bLowain")
        
        self.bMetera = QtWidgets.QLabel(self.centralwidget)
        self.bMetera.setGeometry(QtCore.QRect(170, 370, 151, 151))
        self.bMetera.setText("")
        self.bMetera.setPixmap(QtGui.QPixmap("resources/finals/metera.png"))
        self.bMetera.setObjectName("bMetera")
        
        self.bNarmaya = QtWidgets.QLabel(self.centralwidget)
        self.bNarmaya.setGeometry(QtCore.QRect(330, 370, 151, 151))
        self.bNarmaya.setText("")
        self.bNarmaya.setPixmap(QtGui.QPixmap("resources/finals/narmaya.png"))
        self.bNarmaya.setObjectName("bNarmaya")
        
        self.bPercival = QtWidgets.QLabel(self.centralwidget)
        self.bPercival.setGeometry(QtCore.QRect(490, 370, 151, 151))
        self.bPercival.setText("")
        self.bPercival.setPixmap(QtGui.QPixmap("resources/finals/percival.png"))
        self.bPercival.setObjectName("bPercival")
        
        self.bSoriz = QtWidgets.QLabel(self.centralwidget)
        self.bSoriz.setGeometry(QtCore.QRect(10, 550, 151, 151))
        self.bSoriz.setText("")
        self.bSoriz.setPixmap(QtGui.QPixmap("resources/finals/soriz.png"))
        self.bSoriz.setObjectName("bSoriz")
        
        self.bVaseraga = QtWidgets.QLabel(self.centralwidget)
        self.bVaseraga.setGeometry(QtCore.QRect(170, 550, 151, 151))
        self.bVaseraga.setText("")
        self.bVaseraga.setPixmap(QtGui.QPixmap("resources/finals/vaseraga.png"))
        self.bVaseraga.setObjectName("bVaseraga")
        
        self.bZeta = QtWidgets.QLabel(self.centralwidget)
        self.bZeta.setGeometry(QtCore.QRect(330, 550, 151, 151))
        self.bZeta.setText("")
        self.bZeta.setPixmap(QtGui.QPixmap("resources/finals/zeta.png"))
        self.bZeta.setObjectName("bZeta")
        
        self.bZooey = QtWidgets.QLabel(self.centralwidget)
        self.bZooey.setGeometry(QtCore.QRect(490, 550, 151, 151))
        self.bZooey.setText("")
        self.bZooey.setPixmap(QtGui.QPixmap("resources/finals/zooey.png"))
        self.bZooey.setObjectName("bZooey")

        ########################################################################################## BUTTONS ############################################

        self.pBeelzebub = QtWidgets.QPushButton(self.centralwidget)
        self.pBeelzebub.setGeometry(QtCore.QRect(14, 160, 141, 23))
        self.pBeelzebub.setObjectName("pBeelzebub")
        self.pBeelzebub.clicked.connect(iBeelzebub)
        self.pBeelzebub.clicked.connect(self.openwindow)
        
        self.pCharlotta = QtWidgets.QPushButton(self.centralwidget)
        self.pCharlotta.setGeometry(QtCore.QRect(174, 160, 141, 23))
        self.pCharlotta.setObjectName("pCharlotta")
        self.pCharlotta.clicked.connect(iCharlotta)
        self.pCharlotta.clicked.connect(self.openwindow)
        
        self.pDjeeta = QtWidgets.QPushButton(self.centralwidget)
        self.pDjeeta.setGeometry(QtCore.QRect(334, 160, 141, 23))
        self.pDjeeta.setObjectName("pDjeeta")
        self.pDjeeta.clicked.connect(iDjeeta)
        self.pDjeeta.clicked.connect(self.openwindow)
        
        self.pFerry = QtWidgets.QPushButton(self.centralwidget)
        self.pFerry.setGeometry(QtCore.QRect(494, 160, 141, 23))
        self.pFerry.setObjectName("pFerry")
        self.pFerry.clicked.connect(iFerry)
        self.pFerry.clicked.connect(self.openwindow)
        
        self.pGran = QtWidgets.QPushButton(self.centralwidget)
        self.pGran.setGeometry(QtCore.QRect(14, 340, 141, 23))
        self.pGran.setObjectName("pGran")
        self.pGran.clicked.connect(iGran)
        self.pGran.clicked.connect(self.openwindow)
        
        self.pKatalina = QtWidgets.QPushButton(self.centralwidget)
        self.pKatalina.setGeometry(QtCore.QRect(174, 340, 141, 23))
        self.pKatalina.setObjectName("pKatalina")
        self.pKatalina.clicked.connect(iKatalina)
        self.pKatalina.clicked.connect(self.openwindow)

        self.pLadiva = QtWidgets.QPushButton(self.centralwidget)
        self.pLadiva.setGeometry(QtCore.QRect(334, 340, 141, 23))
        self.pLadiva.setObjectName("pLadiva")
        self.pLadiva.clicked.connect(iLadiva)
        self.pLadiva.clicked.connect(self.openwindow)
        
        self.pLancelot = QtWidgets.QPushButton(self.centralwidget)
        self.pLancelot.setGeometry(QtCore.QRect(490, 340, 151, 23))
        self.pLancelot.setObjectName("pLancelot")
        self.pLancelot.clicked.connect(iLancelot)
        self.pLancelot.clicked.connect(self.openwindow)
        
        self.pLowain = QtWidgets.QPushButton(self.centralwidget)
        self.pLowain.setGeometry(QtCore.QRect(14, 520, 141, 23))
        self.pLowain.setObjectName("pLowain")
        self.pLowain.clicked.connect(iLowain)
        self.pLowain.clicked.connect(self.openwindow)
        
        self.pMetera = QtWidgets.QPushButton(self.centralwidget)
        self.pMetera.setGeometry(QtCore.QRect(174, 520, 141, 23))
        self.pMetera.setObjectName("pMetera")
        self.pMetera.clicked.connect(iMetera)
        self.pMetera.clicked.connect(self.openwindow)
        
        self.pNarmaya = QtWidgets.QPushButton(self.centralwidget)
        self.pNarmaya.setGeometry(QtCore.QRect(334, 520, 141, 23))
        self.pNarmaya.setObjectName("pNarmaya")
        self.pNarmaya.clicked.connect(iNarmaya)
        self.pNarmaya.clicked.connect(self.openwindow)
        
        self.pPercival = QtWidgets.QPushButton(self.centralwidget)
        self.pPercival.setGeometry(QtCore.QRect(494, 520, 141, 23))
        self.pPercival.setObjectName("pPercival")
        self.pPercival.clicked.connect(iPercival)
        self.pPercival.clicked.connect(self.openwindow)

        self.pSoriz = QtWidgets.QPushButton(self.centralwidget)
        self.pSoriz.setGeometry(QtCore.QRect(14, 700, 141, 23))
        self.pSoriz.setObjectName("pSoriz")
        self.pSoriz.clicked.connect(iSoriz)
        self.pSoriz.clicked.connect(self.openwindow)
        
        self.pVaseraga = QtWidgets.QPushButton(self.centralwidget)
        self.pVaseraga.setGeometry(QtCore.QRect(174, 700, 141, 23))
        self.pVaseraga.setObjectName("pVaseraga")
        self.pVaseraga.clicked.connect(iVaseraga)
        self.pVaseraga.clicked.connect(self.openwindow)
        
        self.pZeta = QtWidgets.QPushButton(self.centralwidget)
        self.pZeta.setGeometry(QtCore.QRect(334, 700, 141, 23))
        self.pZeta.setObjectName("pZeta")
        self.pZeta.clicked.connect(iZeta)
        self.pZeta.clicked.connect(self.openwindow)
        
        self.pZooey = QtWidgets.QPushButton(self.centralwidget)
        self.pZooey.setGeometry(QtCore.QRect(494, 700, 141, 23))
        self.pZooey.setObjectName("pZooey")
        self.pZooey.clicked.connect(iZooey)
        self.pZooey.clicked.connect(self.openwindow)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 645, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pBeelzebub.setText(_translate("MainWindow", "Beelzebub"))
        self.pCharlotta.setText(_translate("MainWindow", "Charlotta"))
        self.pDjeeta.setText(_translate("MainWindow", "Djeeta"))
        self.pFerry.setText(_translate("MainWindow", "Ferry"))
        self.pGran.setText(_translate("MainWindow", "Gran"))
        self.pKatalina.setText(_translate("MainWindow", "Katalina"))
        self.pLadiva.setText(_translate("MainWindow", "Ladiva"))
        self.pLancelot.setText(_translate("MainWindow", "Lancelot"))
        self.pLowain.setText(_translate("MainWindow", "Lowain"))
        self.pMetera.setText(_translate("MainWindow", "Metera"))
        self.pNarmaya.setText(_translate("MainWindow", "Narmaya"))
        self.pPercival.setText(_translate("MainWindow", "Percival"))
        self.pSoriz.setText(_translate("MainWindow", "Soriz"))
        self.pVaseraga.setText(_translate("MainWindow", "Vaseraga"))
        self.pZeta.setText(_translate("MainWindow", "Zeta"))
        self.pZooey.setText(_translate("MainWindow", "Zooey"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
