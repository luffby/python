import math
a = int(input())
b = int(input())
c = int(input())
D = b ** 2 - 4*c*a
if D > 0:
    print((-b + math.sqrt(D))/2*a)
    print((-b - math.sqrt(D))/2*a)
elif D == 0:
    print((-b) / (2 * a))
