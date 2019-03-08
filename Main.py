import Matrix

matrixA = Matrix.Matrix(2,2)
matrixB = Matrix.Matrix(2,2)

# Entering data
for i in range(2):
    print('Type values for Matrix %d: ' % (i + 1))
    a = input("Enter the number of rows: ")
    b = input("Enter the number of columns: ")

    try:
        A = Matrix.Matrix(int(a), int(b))
        print(A.display())
        A.filling()
        if i == 0:
            matrixA = A
        else:
            matrixB = A
        print(A.display())
    except ValueError:
        print("Please enter a number!")

Matrix.multiplication(matrixA, matrixB))
