import sys

keys = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"

for line in sys.stdin:
    ans = ""
    for c in line.lower():
        idx = keys.find(c)
        if idx >= 2:
            ans += keys[idx - 2]
        else:
            ans += c
    print(ans, end="")