#!/usr/bin/env python3
import sys
from collections import Counter

def process_input(input_text: str) -> str:
    lines = input_text.splitlines()
    if not lines:
        return ""
    
    try:
        n = int(lines[0].strip())
    except ValueError:
        return ""
        
    counter = Counter()
    for i in range(1, min(n + 1, len(lines))):
        for char in lines[i]:
            if char.isalpha():
                counter[char.upper()] += 1
                
    sorted_chars = sorted(counter.items(), key=lambda x: (-x[1], x[0]))
    return '\n'.join(f"{char} {count}" for char, count in sorted_chars)

def main():
    input_text = sys.stdin.read()
    if input_text:
        print(process_input(input_text))

if __name__ == '__main__':
    main()
