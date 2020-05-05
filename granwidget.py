from PyQt5 import QtCore, QtGui, QtWidgets
import granqt

my_fighter = None

#   Import characters info
def iBeelzebub():
        global my_fighter
        my_fighter = str(granqt.fighters['beelzebub'].get_framedata())  

def iCharlotta():
        global my_fighter
        my_fighter = str(granqt.fighters['charlotta'].get_framedata())

def iDjeeta():
        global my_fighter
        my_fighter = str(granqt.fighters['djeeta'].get_framedata())

def iFerry():
        global my_fighter
        my_fighter = str(granqt.fighters['ferry'].get_framedata())

def iGran():
        global my_fighter
        my_fighter = str(granqt.fighters['gran'].get_framedata())

def iKatalina():
        global my_fighter
        my_fighter = str(granqt.fighters['katalina'].get_framedata())

def iLadiva():
        global my_fighter
        my_fighter = str(granqt.fighters['ladiva'].get_framedata())

def iLancelot():
        global my_fighter
        my_fighter = str(granqt.fighters['lancelot'].get_framedata())

def iLowain():
        global my_fighter
        my_fighter = str(granqt.fighters['lowain'].get_framedata())

def iMetera():
        global my_fighter
        my_fighter = str(granqt.fighters['metera'].get_framedata())

def iNarmaya():
        global my_fighter
        my_fighter = str(granqt.fighters['narmaya'].get_framedata())

def iPercival():
        global my_fighter
        my_fighter = str(granqt.fighters['percival'].get_framedata())

def iSoriz():
        global my_fighter
        my_fighter = str(granqt.fighters['soriz'].get_framedata())

def iVaseraga():
        global my_fighter
        my_fighter = str(granqt.fighters['vaseraga'].get_framedata())

def iZeta():
        global my_fighter
        my_fighter = str(granqt.fighters['zeta'].get_framedata())

def iZooey():
        global my_fighter
        my_fighter = str(granqt.fighters['zooey'].get_framedata())


#   GUI

class Ui_Form(object):


    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.resize(400, 800)

        self.frameLabel = QtWidgets.QLabel(Form)
        self.frameLabel.setObjectName("frameLabel")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.frameLabel.setText('Default text')
        self.frameLabel.setText(my_fighter)         # The information stored in my_fighter should be printed here

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())