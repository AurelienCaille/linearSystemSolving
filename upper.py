import Matrix
from Rational import Rational as R
def upper(matrix):
    """
    return the upper matrix of a matrix
    """
    nb_line = len(matrix.matrix)
    An = matrix
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
        
        An = E * An
    return An


def delta(i, j):
    """
    return 1 if i == j
    return 0 if i != j
    """
    if i == j:
        return 1
    else:
        return 0
        

if __name__ == "__main__":
    A = Matrix.Matrix([[R(2), R(3), R(3), R(1)],
                       [R(-1), R(1), R(1), R(1)],
                       [R(-4), R(-6), R(3), R(2)],
                       [R(-2), R(-1), R(1), R(1)]])
    An = upper(A)
    #print (An)
    #Bn = lower (A)
    print (An)
    
                            
            
    
