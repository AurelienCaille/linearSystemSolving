import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor
import sip
from Matrix import Matrix
from LinearSystem import LinearSystem
from Rational import Rational as R

def stringToInt(string):
    string = string.split("/")
    if len(string) == 1:
        try:
            d = int(string[0])
            n = 1
        except:

            raise ValueError("It's not an integer!")

    if len(string) == 2:

        try:
            d = int(string[0])
            n = int(string[1])

        except:

            raise ValueError("They are not integer:")

    return R(d, n)
            
    


class MatrixInputWidget(QWidget):
    """Widget to enter the value of a square matrix and modify its size"""

    def __init__(self, size):

        super().__init__()

        self.size = size

        self.line_edit = []

        self.initUI()

    def initUI(self):

        #Button to modify the size
        self.plusButton = QPushButton("+")
        self.lessButton = QPushButton("-")

        #Grid for layout
        self.grid = QGridLayout()
        self.setLayout(self.grid)

        #Add input
        self.grid_input = QGridLayout()
        centWidget = QWidget()

        centWidget.setLayout(self.grid_input)

        for i in range(0, self.size):
            self.line_edit.append([])
            for j in range(0, self.size):
                qle = QLineEdit(self)
                self.line_edit[i].append(qle)
                self.grid_input.addWidget(self.line_edit[i][j], i, j)

        #Add widget to grid
        self.grid.addWidget(self.plusButton, 0, 0)
        self.grid.addWidget(self.lessButton, 2, 2)
        self.grid.addWidget(centWidget, 1, 1)


        self.show()

class VectorInputWidget(QWidget):
    """Widget to enter a column vector"""

    def __init__(self, size):

        super().__init__()

        self.size = size

        self.line_edit = []
        #self.parent = parent

        self.initUI()


    def initUI(self):

        #Grid for layout
        grid = QGridLayout()
        self.setLayout(grid)

        for i in range(0, self.size):
            qle = QLineEdit(self)
            self.line_edit.append(qle)
            grid.addWidget(self.line_edit[i], i, 0)
        self.show()     


        
class SystemInputWidget(QWidget):
    """Widget to enter a linear system"""

    def __init__(self, size):

        super().__init__()

        self.size = size

        self.viw = VectorInputWidget(size)
        self.miw = MatrixInputWidget(size)

        self.initUI()


    def initUI(self):

        self.grid = QHBoxLayout(self)
        self.setLayout(self.grid)
        self.grid.addWidget(self.miw)
        self.grid.addWidget(self.viw)


        self.show()


class LinearSystemInterface(QMainWindow):
    """Interface to enter a linearSystem, print LU decomposition and solve it with LU or Jacobi method"""

    def __init__(self, size):

        super(LinearSystemInterface, self).__init__()
        self.size = size
        self.initUI()

        
    def initUI(self):

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle("Linear System Solving Interface")

        self.siw = SystemInputWidget(self.size)

        self.setCentralWidget(self.siw)

        self.siw.miw.plusButton.clicked.connect(lambda: self.changeSize(1))
        self.siw.miw.lessButton.clicked.connect(lambda: self.changeSize(-1))

        resolutionAction = QAction('&LU Resolution', self)
        resolutionAction.setShortcut("Ctrl+Enter")
        resolutionAction.triggered.connect(self.solveSystem)

        decompositionAction = QAction('&LU Decomposition', self)
        decompositionAction.triggered.connect(self.getLUDecomposition)

        self.statusBar()

        menubar = self.menuBar()
        lu_menu = menubar.addMenu('LU')
        lu_menu.addAction(resolutionAction)
        lu_menu.addAction(decompositionAction)
   
        
        self.statusBar().showMessage('Ready')
        self.show()


    def changeSize(self, i):

        self.size += i
        sip.delete(self.siw)
        self.siw = SystemInputWidget(self.size)
        self.setCentralWidget(self.siw)
        self.siw.miw.plusButton.clicked.connect(lambda: self.changeSize(1))
        self.siw.miw.lessButton.clicked.connect(lambda: self.changeSize(-1))
        self.show()

    def solveSystem(self):

        A, B = self.getSystem()

        ls = LinearSystem(A, B)
        print(ls.LUResolution())
        
    def getLUDecomposition(self):
        
        A, B = self.getSystem()

        print('Lower\n', A.lower())
        print('Upper\n', A.upper())

    def getSystem(self):

        A = []
        B =  []


        #Get A
        for i in range(0, self.size):
            A.append([])
            for j in range(0, self.size):
                A[i].append(stringToInt(self.siw.miw.line_edit[i][j].text()))

        A = Matrix(A)

        #Get B
        for i in range(0, self.size):
            B.append([stringToInt(self.siw.viw.line_edit[i].text())])


        B = Matrix(B)

        return A,B

        



if __name__ == "__main__":

    
    app = QApplication(sys.argv)
    lsi = LinearSystemInterface(2)
    sys.exit(app.exec_())
