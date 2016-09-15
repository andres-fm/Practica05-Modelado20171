import sys
from PyQt4 import QtGui
from datetime import date

class Mexico(QtGui.QWidget) :    

    def __init__(self) :
        super(Mexico, self).__init__()
        self.config_ventana()
        self.crea_aprietame()
        self.personajes()      
        self.show()

    def personajes(self) :
        lbl = QtGui.QLabel("""Personajes importantes de la independencia:
        					 \nMiguel Hidalgo
        					 \nJose Maria Morelos
        					 \nJosefa Ortiz""", self)
        lbl.move(15, 10)

    def config_ventana(self) :
        self.setGeometry(100, 100, 650, 450)
        self.setWindowTitle('¡Viva Mexico!')
        self.setWindowIcon(QtGui.QIcon('mexico.png')) 

    def crea_aprietame(self) :
        self.qbtn = QtGui.QPushButton('Aprietame', self)
        self.qbtn.clicked.connect(self.dieciseis)
        self.qbtn.move(200, 150) 

    def dieciseis(self) :
        hoy = date.today()
        sig_sept = date(hoy.year, 9, 16) if hoy <= date(hoy.year, 9, 16) else date(hoy.year+1, 9, 16)
        dias = (sig_sept - hoy).days
        self.qbtn.setText("¡Faltan " + str(dias) + " dias para el próximo 16 de septiembre!")
        self.qbtn.resize(self.qbtn.sizeHint())
        
        
def main() :    
    app = QtGui.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('mexico.png'))
    ex = Mexico()
    sys.exit(app.exec_())


if __name__ == '__main__' :
    main()
