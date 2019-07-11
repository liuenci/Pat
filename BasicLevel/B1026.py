c1, c2 = map(int, input().split())
ans = c2 - c1
if ans % 100 >= 50:
    ans = ans / 100 + 1
else:
    ans = ans / 100
print('%02d:%02d:%02d'%(ans / 3600, ans % 3600 / 60, ans % 60))