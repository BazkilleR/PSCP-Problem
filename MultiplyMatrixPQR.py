"""asdada"""

def create_matrix(p, q, r):
    """Create matrix A of size p x q and matrix B of size q x r."""
    a = []
    b = []

    # Create matrix A (p x q)
    for _ in range(p):
        row = []
        for _ in range(q):
            row.append(int(input()))
        a.append(row)

    # Create matrix B (q x r)
    for _ in range(q):
        row = []
        for _ in range(r):
            row.append(int(input()))
        b.append(row)

    return a, b

def multiply(a, b):
    """Multiply matrix A and matrix B."""
    p = len(a)       # Rows in A
    q = len(a[0])    # Columns in A / Rows in B
    r = len(b[0])    # Columns in B

    # Resultant matrix will be of size p x r
    result = [[0 for _ in range(r)] for _ in range(p)]

    # Matrix multiplication logic
    for i in range(p):
        for j in range(r):
            for k in range(q):
                result[i][j] += a[i][k] * b[k][j]

    # Print the resulting matrix
    for row in result:
        print(" ".join(map(str, row)))

pp = int(input())
qq = int(input())
rr = int(input())

a_matrix, b_matrix = create_matrix(pp, qq, rr)
multiply(a_matrix, b_matrix)
