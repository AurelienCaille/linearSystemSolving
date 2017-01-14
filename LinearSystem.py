from Matrix import Matrix
from Identity import Identity


class LinearSystem():
    def __init__(A, Y):

        self.A = A
        self.Y = Y

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
        Diag = Matrix.Matrix(Diag)
        
        inv_diag = Diag.reverse_diag()
        
        X_k = []
        for i in range(len(matrix.matrix)):
            X_k.append([0])
        X_k = Matrix.Matrix(X_k)


        for i in range(iteration):
            print(i)
            X_k = ((Id - inv_diag * matrix) * X_k) + (inv_diag * target)
            # (I - D^-1 * A) * X_k + D^-1 * Y
            #erreur potentielle de calcul, ou systeme insolvable.
            
        return(X_k)


    def LUResolution(self):
        pass
