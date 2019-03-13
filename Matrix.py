class Matrix:
    # Class for operations under matrices

    def __init__(self, row, column):
        self.dimension = (row, column)      # Dimension of created square matrix
        self.data = [[0]*column for i in range(row)]        # Matrix list, default filling with 0 values

    # Printing a matrix
    def display(self) -> object:
        for i in range(len(self.data)):
            print(self.data[i])

    # Filling elements i-row j-column
    def fill(self):
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                print('Type value for element X%d%d: ' % (i+1, j+1))
                x = input()
                self.data[i][j] = int(x)

    # The multiplication of two matrices
    @staticmethod
    def multiplication(a, b):
        rows_a = len(int(a.dimension))
        columns_a = len(int(a.dimension[1]))
        rows_b = len(int(b.dimension))
        columns_b = len(int(b.dimension[1]))

        c = [[0 for row in range(columns_b)] for col in range(rows_a)]

        if rows_a == columns_b and columns_a == rows_b:
            for i in range(rows_a):
                for j in range(columns_b):
                    for k in range(columns_a):
                        c[i][j] += a[i][k] * b[k][j]
            c.display()
        else:
            print("Matrices are not compatible to multiply!")