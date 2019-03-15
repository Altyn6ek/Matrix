import Matrix


# Multiplication of 2 matrices
def multiplications(a, b):
    rows_a = a.dimension[0]
    columns_a = a.dimension[1]
    rows_b = b.dimension[0]
    columns_b = b.dimension[1]

    c = Matrix(rows_a, columns_b)

    if rows_a == columns_b and columns_a == rows_b:
        for i in range(rows_a):
            for j in range(columns_b):
                for k in range(columns_a):
                    c.data[i][j] += a.data[i][k] * b.data[k][j]
    else:
        print('Matrices are not compatible to multiply!')

    print('Result of multiplying: ')
    c.display()
