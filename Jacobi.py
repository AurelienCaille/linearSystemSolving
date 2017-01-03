import Matrix
from Rational import Rational as R
from Identity import Identity

def Jacobi(matrix, targeted_vect):
    """
    iterate throught the jacobi method to solve the system
    """
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
    Id = Identity(len(matrix.matrix))
    for i in range(4):
        X_k = ((Id - inv_diag) * matrix * X_k) + (inv_diag * target)
        #erreur potentielle de calcul, ou systeme insolvable.
        
    return(X_k)

if __name__ == "__main__":
    A = Matrix.Matrix([[R(2),    R(3),   R(3), R(1)],
                       [R(-1),   R(1),   R(1), R(1)],
                       [R(-4),   R(-6),  R(3), R(2)],
                       [R(-2),   R(-1),  R(1), R(1)]])
                       
    target = Matrix.Matrix([        [R(1)], 
                                    [R(2)], 
                                    [R(3)], 
                                    [R(4)] ])
    print(Jacobi(A, target))
    
    
