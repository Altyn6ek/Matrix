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