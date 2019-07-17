def calculation(str):
    x = y = -1
    # 找出 P T 的位置
    for i in range(len(str)):
        if str[i] == "P":
            x = i
        if str[i] == "T":
            y = i
    # 如果找不到 P T 返回 0
    if x == -1 or y == -1:
        return 0
    # P 在 T 的后面返回 0
    if x > y:
        return 0
    # P T 之间没有字符返回 0
    if y == x + 1:
        return 0
    # 字符串不以 P 开头
    if x != 0:
        b = str[0:x]
    else:
        b = []
    c = str[x+1:y]
    # 字符串不以 T 结尾
    if y != len(str) - 1:
        d = str[y+1:len(str)]
    else:
        d = []
    # 判断各个分段是否由 A 组成
    for i in b:
        if i != "A":
            return 0
    for i in c:
        if i != "A":
            return 0
    for i in d:
        if i != "A":
            return 0
    if d == b * len(c):
        return 1
    else:
        return 0


n = int(input())
for i in range(n):
    str = input()
    if calculation(str) == 1:
        print("YES")
    else:
        print("NO")
