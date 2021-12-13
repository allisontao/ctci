# Zero Matrix: Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.

m = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]


def set_zeroes(matrix):
    row = [False] * len(matrix)
    cols = [False] * len(matrix[0])

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                cols[j] = True

    for i in range(len(row)):
        if row[i]:
            for j in range(len(matrix[0])):
                matrix[i][j] = 0

    for j in range(len(cols)):
        if cols[j]:
            for i in range(len(matrix)):
                matrix[i][j] = 0

    print(matrix)


set_zeroes(m)
