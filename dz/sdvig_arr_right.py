n = int(input())
numbers = list(map(int, input().split()))
tmp = numbers[n-1]
for i in range(n-1, 0, -1):
    numbers[i] = numbers[i-1]
numbers[0] = tmp
print(*numbers)