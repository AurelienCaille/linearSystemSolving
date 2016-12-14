import Matrix
from Identity import Identity
from Rational import Rational as R

def lower(matrix):
#pas fini
    nb_line = len(matrix.matrix)
    An = Identity(nb_line)

    for n in range (nb_line - 1): #E_{n-1} ... E_{1}
        
        #Create empty matrix
        E = []
        En = Identity(nb_line)
        for i in range(nb_line):
            E.append([])
        
        #Create E_{n}^{-1} matrix
        for column in range (nb_line):
            for line in range (nb_line):
                if column == line: #in the diagonal
                    E[line].append(R(1))
                    continue
                else :
                    if n == column and column>line:
                        E[line].append( An[line][column] / An[n][n])
                        continue
                        
                E[line].append(R(0))
                
                                    
        E = Matrix.Matrix(E)
        En = E.multiply(En)
        print(E)
        print(En)
    return En


if __name__ == "__main__":
    A = Matrix.Matrix([[R(2),    R(3),   R(3), R(1)],
                       [R(-1),   R(1),   R(1), R(1)],
                       [R(-4),   R(-6),  R(3), R(2)],
                       [R(-2),   R(-1),  R(1), R(1)]])
    An = lower(A)
    print (An)

