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
        return Matrix(result)
    
    def __repr__(self):
        result = ""
        for i in range(len(self.matrix)):
            result = result + "( "
            for j in range(len(self.matrix)): 
                 result = result + str(self.matrix[i][j]) + " "
            result = result + ")\n"
        result = result +"-------------"
        return result.strip()
                
if __name__ == "__main__":
    A = [[1, 2, 3],
         [3, 4, 5],
         [1, 2, 3]]
    
    B = [[5, 6, 10],
         [7, 8, 45],
         [1, 2, 3]]
    A = Matrix(A)
    B = Matrix(B)
    print (A.multiply(B))
    
