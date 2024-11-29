
def count_inversions(s):
    inversions = 0
    n= len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] > s[j]:
                inversions += 1
    return inversions

print(count_inversions("AGCT"))
print(count_inversions("ACTG"))
print(count_inversions("ACGT"))