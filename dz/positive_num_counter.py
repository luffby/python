n = int(input())
numbers = list(map(int, input().split()))

cnt = 0
for i in range(n):
    if numbers[i] > 0:
        cnt += 1
print(cnt)