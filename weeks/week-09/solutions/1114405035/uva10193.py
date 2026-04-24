import sys
import math

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    idx = 1
    for i in range(1, n + 1):
        # 解析二進位字串為十進位整數
        num1 = int(input_data[idx], 2)
        num2 = int(input_data[idx+1], 2)
        idx += 2
        
        if math.gcd(num1, num2) > 1:
            print(f"Pair #{i}: All you need is love!")
        else:
            print(f"Pair #{i}: Love is not all you need!")

if __name__ == '__main__':
    solve()