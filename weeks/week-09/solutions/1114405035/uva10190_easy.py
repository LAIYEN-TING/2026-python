import sys

for line in sys.stdin:
    if not line.strip(): continue
    n, m = map(int, line.split())
    
    if m <= 1 or n <= 1:
        print("Boring!")
        continue
        
    ans = []
    while n > 1:
        if n % m != 0: break
        ans.append(str(n))
        n //= m
        
    if n == 1:
        print(" ".join(ans + ["1"]))
    else:
        print("Boring!")