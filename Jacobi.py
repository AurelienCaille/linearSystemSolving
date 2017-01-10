import Matrix
from Rational import Rational as R
from Identity import Identity

def Jacobi(matrix, targeted_vect, iteration = 5):
    """
    iterate throught the jacobi method to solve the system
    """
    
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
        X_k.append([1])
    X_k = Matrix.Matrix(X_k)


    for i in range(iteration):
        X_k = ((Id - inv_diag * matrix) * X_k) + (inv_diag * target)
        # (I - D^-1 * A) * X_k + D^-1 * Y
        #erreur potentielle de calcul, ou systeme insolvable.
        
    return(X_k)

if __name__ == "__main__":
    A = Matrix.Matrix([[R(2), R(0)],
                       [R(0), R(2)]])
                       
    target = Matrix.Matrix([        [R(1)], 
                                    [R(2)]])
    print(Jacobi(A, target, 100))
    
    
