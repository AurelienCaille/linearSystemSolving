class Matrix:
    """Classe definissant les elements matriciels
    """
    def __init__(self, matrix):
        """create an empty matrix
        """
        self.matrix = matrix
    def multiply(self, matrix):
        """definit le protuit matriciel
        """
        result = []
        for i in range(len(matrix.matrix)):
            line = []
            for j in range(len(matrix.matrix)):
                somme = 0
                for k in range(len(matrix.matrix)):
                    somme += self.matrix[i][k]*matrix.matrix[k][j]
                line.append(somme)
            result.append(line)
        return result
                
if __name__ == "__main__":
    A = [[1, 2],[3, 4]]
    B = [[5, 6],[7, 8]]
    A = Matrix(A)
    B = Matrix(B)
    print (A.multiply(B))
    
