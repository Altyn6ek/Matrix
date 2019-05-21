#!/usr/bin/env python
from Matrix import Matrix

matrix_a = Matrix(2, 2)
matrix_b = Matrix(0, 0)

# Filling matrices a and b
for i in range(2):
    print('Type values for Matrix %d: ' % (i + 1))
    a = input("Enter the number of rows: ")
    b = input("Enter the number of columns: ")

    try:
        A = Matrix(int(a), int(b))
        A.fill()
        if i == 0:
            matrix_a = A
        else:
            matrix_b = A
    except ValueError:
        print("Please enter an integer value!")
        break

# Matrix.multiplication(matrix_a, matrix_b)
matrix_a.plus(matrix_b).display()
### comment
