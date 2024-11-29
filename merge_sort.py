def digital_root_ai(n):
    if n == 0:
        return 0
    return 1 + (n - 1) % 9
#
# def sort_by_digital_root(arr):
#     return sorted(arr, key=lambda x: (digital_root(x), x))
#
# # Ввод данных
# numbers = list(map(int, input().split()))
#
# # Сортировка
# sorted_numbers = sort_by_digital_root(numbers)
#
# # Вывод результата
# print(*sorted_numbers)

# def merge(A, B):
#     res = []
#     i = 0
#     j = 0
#     while i < len(A) and j < len(B):
#         if A[i] <= B[j]:
#             res.append(A[i])
#             i += 1
#         else:
#             res.append(B[j])
#             j += 1
#     res += A[i:] + B[j:]
#     return res

def digital_root(n):
    if n == 0:
        return 0
    return digital_root(n // 10) + n % 10

A = [15, 14, 13, 12, 11, 6, 5]
for i in A:
    print(digital_root(i), digital_root_ai(i))


def merge(A: list, B: list):
    C = [0] * (len(A + B))
    i = j = k = 0

    while i < len(A) and j < len(B):

        if A[i] <= B[j]:
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


print(merge_sort([3, 4, 5, 1, 2, 4]))


# def merge(A, B):
#     res = []
#     i = 0
#     j = 0
#     while i < len(A):
#         if digital_root(A[i]) > digital_root(B[j]):
#             A, B = B, A
#             i, j = j, i
#         res.append(A[i])
#         i += 1
#     res += B[j:]
#     return res
#
# def mergesort(A):
#     if len(A) < 2:
#         return A
#     mid = len(A) // 2
#     left = A[:mid]
#     right = A[mi d:]
#     return merge(mergesort(left), mergesort(right))

A = [15, 14, 13, 12, 11, 6, 5]
print(mergesort(A))