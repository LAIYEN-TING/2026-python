#!/usr/bin/env python3
import sys

# 題目：UVA 10008 - What's Cryptanalysis?
# 目的：統計字元出現次數，並按次數降序、字母升序排列

def solve():
    # 讀取輸入行數
    input_data = sys.stdin.read().splitlines()
    if not input_data:
        return
        
    # 用字典來統計每個大寫字母出現的次數
    counts = {}
    
    # 遍歷所有輸入行（跳過第一行的數量 n）
    for line in input_data[1:]:
        for char in line:
            # 只統計英文字母
            if char.isalpha():
                # 統一轉成大寫
                up_char = char.upper()
                counts[up_char] = counts.get(up_char, 0) + 1
                
    # 將字典轉換為列表，方便排序
    # 排序條件：次數降序 (-x[1])，字母升序 (x[0])
    sorted_chars = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
    
    # 輸出結果
    for char, count in sorted_chars:
        print(f"{char} {count}")

if __name__ == '__main__':
    solve()
