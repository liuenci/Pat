failA = failB = 0
n = int(input())
for i in range(n):
    a1, a2, b1, b2 = map(int, input().split())
    if a1 + b1 == a2 and a1 + b1 != b2:
        failB = failB + 1
    elif a1 + b1 != a2 and a1 + b1 == b2:
        failA = failA + 1
print("%d %d"%(failA, failB))