import Matrix

matrix_a = Matrix.Matrix(2, 2)
matrix_b = Matrix.Matrix(0, 0)

for i in range(2):
    print('Type values for Matrix %d: ' % (i + 1))
    a = input("Enter the number of rows: ")
    b = input("Enter the number of columns: ")

    try:
        A = Matrix.Matrix(int(a), int(b))
        A.fill()
        A.display()
        if i == 0:
            matrix_a = A
        else:
            matrix_b = A
    except ValueError:
        print("Please enter an integer value!")
        break

Matrix.Matrix.multiplication(matrix_a, matrix_b)