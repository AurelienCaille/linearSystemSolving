import Matrix

def upper(matrix):

    line = len(matrix.matrix)
    An = A
    for n in range (line-1):
        
        E = []
        for i in range(line):
            E.append([])
            
        for x in range (line):
            for k in range (line):
                if x == k:
                    E[k].append(1)
                    continue
                else :
                    if n == x:
                        if x<k:
                            E[k].append(- float(An.matrix[k][x]) / An.matrix[n][n])
                            
                            continue
                        
                E[k].append(0)
                
                                    
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
    line = len(matrix.matrix)
    En = Matrix.Matrix([[delta(i, j) for i in range(line)] for j in range(line)])
    for n in range (line - 1):
        
        E = []
        for i in range(line):
            E.append([])
            
        for x in range (line):
            for k in range (line):
                if x == k:
                    E[k].append(1)
                    continue
                else :
                    if n == x:
                        if x>k:
                            E[k].append( float(An.matrix[k][x]) / An.matrix[n][n])
                            
                            continue
                        
                E[k].append(0)
                
                                    
        E = Matrix.Matrix(E)
        En = E.multiply(En)
        print(E)
        print(En)
    return En

if __name__ == "__main__":
    A = Matrix.Matrix([[2, 3, 3, 1], [-1, 1, 1, 1], [-4, -6, 3, 2], [-2, -1, 1, 1]])
    An = upper(A)
    #print (An)
    Bn = lower (A)
    print (Bn)
    
                            
            
    
