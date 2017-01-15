from Matrix import Matrix
from Matrix import Identity
from Rational import Rational as R

class LinearSystem():
    def __init__(self, A, Y):

        self.A = A
        self.Y = Y
        self.U = A.upper()
        self.L = A.lower()
    def Jacobi(self, iteration = 5):
        """
        iterate throught the jacobi method to solve the system
        """
        matrix = self.A
        targeted_vect = self.Y
        Id = Identity(len(matrix.matrix))
        
        #exctract the Diagonal from the matrix
        Diag = []
        for i in range(len(matrix.matrix)):
            line = []
            for j in range(len(matrix.matrix)):
                if i == j:
                    line.append(matrix.matrix[i][j])
                else:
                    line.append(R(0))
            Diag.append(line)
        Diag = Matrix(Diag)
        
        inv_diag = Diag.reverse_diag()
        
        X_k = []
        for i in range(len(matrix.matrix)):
            X_k.append([0])
        X_k = Matrix(X_k)


        for i in range(iteration):
            print(i)
            X_k = ((Id - inv_diag * matrix) * X_k) + (inv_diag * target)
            # (I - D^-1 * A) * X_k + D^-1 * Y
            #erreur potentielle de calcul, ou systeme insolvable.
            
        return(X_k)


    def LUResolution(self):
        B = []
        for yindex in range(len(self.Y.matrix)):
            y = self.Y[yindex][0]
            b = y/self.L[yindex][yindex]
            for i in range(len(B)):
                b = b - (self.L[yindex][i] * B[i][0]) / self.L[yindex][yindex]
            B.append([b])
        B = Matrix(B)
        X = []
        for bindex in range(len(B.matrix)-1, -1, -1):
            b = B[bindex][0]
            x = b/ self.U[bindex][bindex]
            for xindex in range(len(X)):
                x = x - (self.U[bindex][-xindex-1] * X[xindex][0])/ self.U[bindex][bindex]
            X.append([x])
        X.reverse()
        return Matrix(X)

if __name__ == "__main__":
    A = Matrix([    [R(2),    R(3),   R(3), R(1)],
                    [R(-1),   R(1),   R(1), R(1)],
                    [R(-4),   R(-6),  R(3), R(2)],
                    [R(-2),   R(-1),  R(1), R(1)]])

    Y = Matrix([        [R(21)], 
                        [R(8)],
                        [R(1)],
                        [R(3)]])
                        
    LS = LinearSystem(A, Y)
    X = LS.LUResolution()
    
    print(A * X)
    
