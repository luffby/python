def lcs(A,B)
    ans = []
    F = [[0] * (len(B) + 1) for i in range(len(A) + 1)] #A - cтолбцы
    for i in range(1, len(A) + 1):
        for j in range(1,len(B)+1):
                if A[i-1] = B[j-1]:
                    F[i][j] = 1 + F[i-1][j-1]
                else:
                    F[i][j] = max(F[i-1][j], F[i][j-1])
    return F[-1][-1]

    lcs_string = []
    m = len(A)
    n = len(B)
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string.append(X[i - 1])
            i -= 1
            j -= 1
        elif F[i - 1][j] >= F[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return F[-1][-1]

print(lcs([],[]))