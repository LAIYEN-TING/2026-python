#!/usr/bin/env python3
import sys

# 題目：UVA 10019 (實際上是 Hashmat the Brave Warrior)
# 目的：計算兩個大整數之間的絕對差值

def solve():
    # 使用 sys.stdin 讀取每一行
    for line in sys.stdin:
        # 將行拆分成數字列表
        parts = line.split()
        if not parts:
            continue
        
        # 將字串轉換為整數
        # Python 會自動處理大整數，所以不需要擔心 2^63 的範圍
        a = int(parts[0])
        b = int(parts[1])
        
        # 輸出兩個數字差的絕對值
        print(abs(a - b))

if __name__ == '__main__':
    solve()
