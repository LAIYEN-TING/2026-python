#!/usr/bin/env python3
import sys

# 題目：UVA 10038 - Jolly Jumpers
# 目的：判斷一個序列是否為 Jolly Jumper（相鄰差的絕對值包含 1 到 n-1）

def solve():
    for line in sys.stdin:
        parts = list(map(int, line.split()))
        if not parts:
            continue
            
        n = parts[0]
        # 如果只有一個元素，一定是 Jolly Jumper
        if n == 1:
            print("Jolly")
            continue
            
        nums = parts[1:]
        # 用一個集合（或布林陣列）記錄出現過的差值
        diffs = set()
        
        # 計算相鄰元素的差的絕對值
        for i in range(n - 1):
            diff = abs(nums[i] - nums[i+1])
            # 差值必須在 1 到 n-1 之間
            if 1 <= diff <= n - 1:
                diffs.add(diff)
                
        # 如果集合的大小剛好是 n-1，代表 1 到 n-1 都出現過了
        if len(diffs) == n - 1:
            print("Jolly")
        else:
            print("Not jolly")

if __name__ == '__main__':
    solve()
