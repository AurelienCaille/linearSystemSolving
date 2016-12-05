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