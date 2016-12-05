import Matrix
from upper import delta

def lower(matrix):
#pas fini
    nb_line = len(matrix.matrix)
    En = Matrix.Matrix([[delta(i, j) for i in range(nb_line)]
                                    for j in range(nb_line)])
    for n in range (nb_line - 1): #E_{n-1} ... E_{1}
        
        #Create empty matrix
        E = []
        for i in range(nb_line):
            E.append([])
        
        #Create E_{n}^{-1} matrix
        for column in range (nb_line):
            for line in range (nb_line):
                if column == line: #in the diagonal
                    E[line].append(1)
                    continue
                else :
                    if n == column and column>line:
                        E[line].append( An[line][column] / An[n][n])
                        continue
                        
                E[line].append(0)
                
                                    
        E = Matrix.Matrix(E)
        En = E.multiply(En)
        print(E)
        print(En)
    return En


if __name__ == "__main__" :
    pass

