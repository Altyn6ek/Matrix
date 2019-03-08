class Matrix:
    # Parent (square matrix)

    def __init__(self, row, column):
        self.dimension = (row, column)                          # Dimension of created square matrix
        self.data = [[0]*column for i in range(row)]            # Default filling with 0 values

    # Printing a matrix
    def display(self) -> object:
        for i in range(len(self.data)):  # ! Make here using enumerate
            print(self.data[i])

    # Filling elements i-rows j-columns
    def filling(self):
        for i in range(len(self.data)):  # ! Make here using enumerate
            for j in range(len(self.data[i])):  # ! Make here using enumerate
                print('Type value for element X%d%d: ' % (i+1, j+1))
                x = input()
                self.data[i][j] = int(x)

    # The multiplication of two matrices
    def multiplication(self, matrix_a, matrix_b):
        print('matrix A: ' + matrix_a)
        print('MULTIPLICATION')
        print('matrix B: ' + matrix_b)