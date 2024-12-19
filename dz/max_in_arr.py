n = int(input())
numbers = list(map(int, input().split()))
max = numbers[0]
for i in range(1,n):
    if numbers[i] > max:
        max = numbers[i]

print(max)