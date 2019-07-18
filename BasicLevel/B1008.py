a = []
count = 0
n, m = map(int, input().split())
m = m % n
a = input().split()

# 输出 n-m 号到 n-1 号
for i in range(n - m, n):
    print(a[i], end="")
    count = count + 1
    if count < n:
        print(" ", end="")

# 输出 0 号 到 n - m - 1 号
for i in range(0, n - m):
    print(a[i],end="")
    count = count + 1
    if count < n:
        print(" ",end="")
