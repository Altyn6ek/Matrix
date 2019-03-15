class Matrix:
    # Class for operations under matrices

    def __init__(self, row, column):
        self.dimension = (row, column)      # Dimension of created square matrix
        self.data = []
        for i in range(row):
            self.data.append([0] * column)

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
    # @staticmethod
    # def multiplication(a, b):
    #     rows_a = a.dimension[0]
    #     columns_a = a.dimension[1]
    #     rows_b = b.dimension[0]
    #     columns_b = b.dimension[1]
    #
    #     c = Matrix(rows_a, columns_b)
    #
    #     if rows_a == columns_b and columns_a == rows_b:
    #         for i in range(rows_a):
    #             for j in range(columns_b):
    #                 for k in range(columns_a):
    #                     c.data[i][j] += a.data[i][k] * b.data[k][j]
    #     else:
    #         print('Matrices are not compatible to multiply!')
    #
    #     print('Result of multiplying: ')
    #     c.display()