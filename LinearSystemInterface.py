import sys

from PyQt5.QtWidgets import QMainWindow, QFrame, QDesktopWidget, QApplication
from PyQt5.QtGui import QPainter, QColor


class MatrixInputWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        plusButton = QPushButton("+")
        lessButton = QPushButton("-")

        


        

    


class LinearSystemInterface(QMainWindow):

    def __init__(self):

        super().__init__()

        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Linear System Solving Interface")

        menubar = self.menuBar()
        lu_decomposition = menubar.addMenu('LU')
        jacobi = menubar.addMenu('Jacobi')
        
        
        self.statusBar().showMessage('Ready')
        self.show()



if __name__ == "__main__":

    
    app = QApplication(sys.argv)
    lsi = LinearSystemInterface()
    sys.exit(app.exec_())
