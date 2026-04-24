#!/usr/bin/env python3
import sys

def is_jolly(nums: list) -> bool:
    if not nums:
        return False
    n = nums[0]
    if n == 1:
        return True
    
    sequence = nums[1:]
    diffs = set()
    for i in range(n - 1):
        diff = abs(sequence[i] - sequence[i+1])
        if 1 <= diff <= n - 1:
            diffs.add(diff)
            
    return len(diffs) == n - 1

def process_input(input_text: str) -> str:
    lines = input_text.strip().splitlines()
    results = []
    for line in lines:
        parts = list(map(int, line.split()))
        if not parts:
            continue
        if is_jolly(parts):
            results.append("Jolly")
        else:
            results.append("Not jolly")
    return '\n'.join(results)

def main():
    input_text = sys.stdin.read()
    if input_text:
        print(process_input(input_text))

if __name__ == '__main__':
    main()
