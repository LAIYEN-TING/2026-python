import sys, math

lines = sys.stdin.read().split()
if lines:
    n = int(lines[0])
    for i in range(n):
        num1 = int(lines[2*i+1], 2)
        num2 = int(lines[2*i+2], 2)
        if math.gcd(num1, num2) > 1:
            print(f"Pair #{i+1}: All you need is love!")
        else:
            print(f"Pair #{i+1}: Love is not all you need!")