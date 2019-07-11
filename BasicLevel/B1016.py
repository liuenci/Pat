a, da, b, db = map(int, input().split())
pa = 0
pb = 0
while a != 0:
    if a % 10 == da:
        pa = pa * 10 + da
    a = int(a / 10)

while b != 0:
    if b % 10 == db:
        pb = pb * 10 + db
    b = int(b / 10)

print(pa + pb)