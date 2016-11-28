import Matrix
from Rational import Rational as R
def upper(matrix):

    nb_line = len(matrix.matrix)
    An = A
    for n in range (nb_line-1):
        
        E = []
        for i in range(nb_line):
            E.append([])
            
        for x in range (nb_line):
            for k in range (nb_line):
                if x == k:
                    E[k].append(R(1))
                    continue
                else :
                    if n == x:
                        if x<k:
                            E[k].append((R(0) - An[k][x]) / An[n][n])
                            
                            continue
                        
                E[k].append(R(0))
                
                                    
        E = Matrix.Matrix(E)
        
        An = E.multiply(An)
    return An


def delta(i, j):
    if i == j:
        return 1
    else:
        return 0
def lower(matrix):
#pas fini
    nb_line = len(matrix.matrix)
    En = Matrix.Matrix([[delta(i, j) for i in range(nb_line)]
                                    for j in range(nb_line)])
    for n in range (nb_line - 1):
        
        E = []
        for i in range(nb_line):
            E.append([])
            
        for x in range (nb_line):
            for k in range (nb_line):
                if x == k:
                    E[k].append(1)
                    continue
                else :
                    if n == x:
                        if x>k:
                            E[k].append( An[k][x] / An[n][n])
                            
                            continue
                        
                E[k].append(0)
                
                                    
        E = Matrix.Matrix(E)
        En = E.multiply(En)
        print(E)
        print(En)
    return En

if __name__ == "__main__":
    A = Matrix.Matrix([[R(2), R(3), R(3), R(1)],
                       [R(-1), R(1), R(1), R(1)],
                       [R(-4), R(-6), R(3), R(2)],
                       [R(-2), R(-1), R(1), R(1)]])
    An = upper(A)
    #print (An)
    #Bn = lower (A)
    print (An)
    
                            
            
    
