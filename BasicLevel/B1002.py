n = input()
lookup = {1: "yi", 2: "er", 3: "san", 4: "si", 5: "wu", 6: "liu", 7: "qi", 8: "ba", 9: "jiu", 0: "ling"}
sum = 0
for i in n:
    sum = sum + int(i)
sumStr = str(sum)
len = len(sumStr)
for x in range(len - 1):
    num = int(sumStr[x])
    print(lookup[num] + " ", end="")
print(lookup[int(sumStr[len - 1])])