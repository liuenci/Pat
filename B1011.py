n = int(input())
tcase = 1
while n != 0:
    a, b, c = map(int,input().split())
    if a + b > c:
        print('Case #%s: true' %(tcase))
    else:
        print('Case #%s: false' %(tcase))
    tcase = tcase + 1
    n = n - 1
