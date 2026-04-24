#!/usr/bin/env python3
import sys

# 題目：UVA 10035 - Primary Arithmetic
# 目的：計算兩個數相加時產生的進位次數

def solve():
    for line in sys.stdin:
        # 讀取兩個數字
        parts = line.split()
        if not parts or len(parts) < 2:
            continue
            
        a, b = parts[0], parts[1]
        
        # 如果兩個數都是 0，結束程式
        if a == '0' and b == '0':
            break
            
        # 為了方便從個位數開始計算，將字串反轉
        a = a[::-1]
        b = b[::-1]
        
        carries = 0
        carry_in = 0
        
        # 遍歷最長的數字長度
        for i in range(max(len(a), len(b))):
            digit_a = int(a[i]) if i < len(a) else 0
            digit_b = int(b[i]) if i < len(b) else 0
            
            # 計算該位的總和（包含前一位的進位）
            current_sum = digit_a + digit_b + carry_in
            
            # 判斷是否進位
            if current_sum >= 10:
                carries += 1
                carry_in = 1
            else:
                carry_in = 0
                
        # 格式化輸出
        if carries == 0:
            print("No carry operation.")
        elif carries == 1:
            print("1 carry operation.")
        else:
            print(f"{carries} carry operations.")

if __name__ == '__main__':
    solve()
