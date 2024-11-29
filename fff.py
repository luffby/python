import sys
def count_inversions(s):
    inversions = 0
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] > s[j]:
                inversions += 1
    return inversions


def merge(A: list, B: list):
    C = [0] * (len(A + B))
    i = j = k = 0

    while i < len(A) and j < len(B):

        if count_inversions(A[i]) < count_inversions(B[j]):
            C[k] = A[i]
            i += 1

        elif count_inversions(A[i]) == count_inversions(B[j]):
            C[k] = A[i]
            i+=1

        else:

            C[k] = B[j]
            j += 1

        k += 1

    while i < len(A):
        C[k] = A[i]
        i += 1
        k += 1

    while j < len(B):
        C[k] = B[j]
        j += 1
        k += 1

    return C


def merge_sort(A):
    if len(A) < 2:
        return A

    mid = len(A) // 2
    L = [A[i] for i in range(0, mid)]
    R = [A[i] for i in range(mid, len(A))]

    A = merge(merge_sort(L), merge_sort(R))

    return A


k = int(input())
for j in range(k):
    n, m = map(int, input().split())
    A = [0] * m
    for a in
    A = sys.stdin.read().splitlines()
    print(*merge_sort(A), sep='\n')
    for  i in range(k - 2):
        print('\n')