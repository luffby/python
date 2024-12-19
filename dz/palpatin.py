n = int(input())
numbers = list(map(int, input().split()))
if numbers[0] > numbers[1]:
    minmin = numbers[1]
    min = numbers[0]
else:
    minmin = numbers[0]
    min = numbers[1]

for i in range(2,n):
    if numbers[i] < min and numbers[i] > minmin:
        min = numbers[i]
    if numbers[i] < minmin:
        minmin = numbers[i]

print(minmin, min)