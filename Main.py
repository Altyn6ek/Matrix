class Matrix:
    # Parent (super matrix)

    def __init__(self, value):
        self.dimension = value                                             # Dimension of created square matrix
        self.data = [[0]*value for i in range(value)]                      # Contains values of the matrix

    def display(self) -> object:                                           # Displaying a square matrix(2 or 3 dimensions)
        if self.dimension == 2:
            return f"{self.data[0]}\n{self.data[1]}"
        elif self.dimension == 3:
            return f"{self.data[0]}\n{self.data[1]}\n{self.data[2]}"
        else:
            return f"Sorry we doesn't support such format of square matrix"

    def filling(self):                                                   # Filling elements
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                print('Type value for element X%d%d: ' % (i+1, j+1))
                x = input()
                self.data[i][j] = int(x)

a = input("Type dimension of square matrix A: ")

try:
    b = int(a)
    A = Matrix(b)
    print(A.display())
except ValueError:
    print("Please enter an integer value")

try:
    A.filling()
    print(A.display())
except ValueError:
    print("Something went wronnnng...")