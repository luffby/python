n = int(input())
numbers = list(map(int, input().split()))
x = int(input())
cnt = 0
for i in range(n):
    if x == numbers[i]:
        cnt += 1
print(cnt)