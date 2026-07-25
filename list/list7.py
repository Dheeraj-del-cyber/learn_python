import re
n = int(input())
for i in range(n):
    number = input()
    if re.fullmatch(r"[789]\d{9}", number):
        print("YES")
    else:
        print("NO")