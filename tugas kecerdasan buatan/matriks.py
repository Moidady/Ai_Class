# Matriks A
A = [
    [1, 4, 7],
    [3, 6, 9]
]

# Matriks B
B = [
    [5, 7, 8, 1],
    [6, 4, 9, 12],
    [11, 18, 14, 2]
]

# Matriks hasil perkalian A x B
result = [
            [0, 0, 0, 0], 
            [0, 0, 0, 0]
        ]

# Melakukan perkalian matriks
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
            

# Mencetak matriks hasil
for row in result:
    print(row)

print(len(A))

"""
import numpy as np

# Matriks A
A = np.array([
    [1, 4, 7],
    [3, 6, 9]
])

# Matriks B
B = np.array([
    [5, 7, 8, 1],
    [6, 4, 9, 12],
    [11, 18, 14, 2]
])

# Melakukan perkalian matriks A x B
result = np.matmul(A, B)

# Mencetak matriks hasil
print(result)
"""