cola = 2
rowa = 3
colb = 3
rowb = 2

# Function to compute the Kronecker Product of two matrices
def Kroneckerproduct(A, B):
    C = [[0 for j in range(cola * colb)] for i in range(rowa * rowb)]
    for i in range(0, rowa):
        for k in range(0, rowb):
            for j in range(0, cola):
                for l in range(0, colb):
                    C[i * rowb + k][j * colb + l] = A[i][j] * B[k][l]
                    print(C[i * rowb + k][j * colb + l], end=' ')
            print("\n")

# Driver code.
A = [[0 for j in range(2)] for i in range(3)]
B = [[0 for j in range(3)] for i in range(2)]

A[0][0] = 1
A[0][1] = 2
A[1][0] = 3
A[1][1] = 4
A[2][0] = 1
A[2][1] = 0

B[0][0] = 0
B[0][1] = 5
B[0][2] = 2
B[1][0] = 6
B[1][1] = 7
B[1][2] = 3

Kroneckerproduct(A, B)
