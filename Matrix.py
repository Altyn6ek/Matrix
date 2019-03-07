class Matrix:
    # Parent (square matrix)

    def __init__(self, row, column):
        self.dimension = (row, column)          # Dimension of created square matrix
        self.data = [[0]*column for i in range(row)]            # Default filling with 0 values

    def display(self) -> object:            # Printing a matrix
        for i in range(len(self.data)):
            print(self.data[i])

    def filling(self):          # Filling elements i-row j-column
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                print('Type value for element X%d%d: ' % (i+1, j+1))
                x = input()
                self.data[i][j] = int(x)

    def multiplication(self, matrixA, matrixB):         # The multiplication of two matrices