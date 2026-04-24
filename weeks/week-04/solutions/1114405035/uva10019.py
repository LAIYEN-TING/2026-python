#!/usr/bin/env python3
import sys

def process_input(input_text: str) -> str:
    # 將輸入依行分割，並過濾掉空行
    lines = input_text.strip().splitlines()
    results = []
    
    for line in lines:
        if not line.strip():
            continue
        try:
            # 讀取每行的兩個整數
            nums = list(map(int, line.split()))
            if len(nums) == 2:
                # 計算絕對值差
                results.append(str(abs(nums[0] - nums[1])))
        except ValueError:
            continue
            
    return '\n'.join(results)

def main():
    # 從標準輸入讀取所有內容並處理
    input_data = sys.stdin.read()
    if input_data:
        print(process_input(input_data))

if __name__ == '__main__':
    main()
