import sys

def solve():
    # 逐行讀取輸入
    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            n, m = map(int, line.split())
        except ValueError:
            continue
            
        # 例外條件：除數與被除數必須 >= 2
        if m < 2 or n < 2:
            print("Boring!")
            continue
            
        seq = []
        temp = n
        while temp > 1:
            if temp % m != 0:
                break
            seq.append(temp)
            temp //= m
        
        if temp == 1:
            seq.append(1)
            print(" ".join(map(str, seq)))
        else:
            print("Boring!")

if __name__ == '__main__':
    solve()