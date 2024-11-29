def digital_root(n):
    while n > 9:
        n = digital_root(n // 10) + n % 10
    return n

def merge(A: list, B: list):
    C = [0] * (len(A + B))
    i = j = k = 0

    while i < len(A) and j < len(B):

        if digital_root(A[i]) < digital_root(B[j]):
            C[k] = A[i]
            i += 1

        elif digital_root(A[i]) == digital_root(B[j]):
            if A[i] > B[j]:
                C[k] = B[j]
                j+=1
            else:
                C[k] = A[i]
                i += 1

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

A = list(map(int, input().split()))
print(*merge_sort(A))
