from Rational import Rational as R

class Matrix:
    """ define Matrix """
    
    def __init__(self, matrix):
        """create an empty matrix
        """
        self.matrix = matrix
        
    def multiply(self, matrix):
        """
        define the matrix product
        no change to the initial Matrix
        """
        result = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(matrix.matrix[i])):
                somme = R(0)
                for k in range(len(matrix.matrix)):
                    somme += self.matrix[i][k] * matrix.matrix[k][j]
                line.append(somme)
            result.append(line)
        return Matrix(result)
        
    def reverse_diag(self):
        """
        Test if a matrix is diagonal and reverse it
        """
        result = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix)):
                if i == j and self.matrix[i][j] != 0:
                    line.append(R(1)/self.matrix[i][j])
                else:
                    line.append(R(0))
                if i != j and self.matrix[i][j] != R(0.0):
                    # print(i, j, self.matrix[i][j])
                    raise ValueError("matrix isn't diagonal")
            result.append(line)
        return Matrix(result)
    
    def __mul__(self, matrix):
        return self.multiply(matrix)
        
    def __sub__(self, matrix):
        result = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix)):
                line.append(self.matrix[i][j] - matrix.matrix[i][j])
            result.append(line)
        result = Matrix(result)
        return result
        
    def __add__(self, matrix):
        result = []
        for i in range(len(self.matrix)):
            line = []
            for j in range(len(self.matrix[i])):
                line.append(self.matrix[i][j] + matrix.matrix[i][j])
            result.append(line)
        result = Matrix(result)
        return result
            
    
    def __getitem__(self, number):
        return self.matrix[number]
        
    def __repr__(self):
        result = ""
        for i in range(len(self.matrix)):
            result = result + "( "
            for j in range(len(self.matrix[i])): 
                 result = result + str(self.matrix[i][j]) + "\t"
            result = result + ")\n"
        result = result +"-------------"
        return result.strip()
                
if __name__ == "__main__":
    A = [[R(1), R(2), R(3)],
         [R(3), R(4), R(5)],
         [R(1), R(2), R(3)]]
    
    B = [[R(5), R(6), R(10)],
         [R(7), R(8), R(45)],
         [R(1), R(2), R(3)]]
    A = Matrix(A)
    B = Matrix(B)
    print (A.multiply(B))
    
    A = [[R(3), R(0), R(0)],
        [R(0), R(2), R(0)],
        [R(0), R(0), R(0)]]
    A = Matrix(A)
    print(A.reverse_diag())
    
