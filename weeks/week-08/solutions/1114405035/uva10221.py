import sys
import math

def solve():
    for line in sys.stdin:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) < 3:
            continue
        
        s = float(parts[0])
        a = float(parts[1])
        unit = parts[2]
        
        # 單位轉換：分 -> 度
        if unit == "min":
            a /= 60.0
            
        # 保證角度不會超過 180 度 (取較短距離)
        a = a % 360.0
        if a > 180.0:
            a = 360.0 - a
            
        r = 6440.0 + s
        
        arc = r * a * math.pi / 180.0
        chord = 2.0 * r * math.sin(a * math.pi / 360.0)
        
        print(f"{arc:.6f} {chord:.6f}")

if __name__ == '__main__':
    solve()