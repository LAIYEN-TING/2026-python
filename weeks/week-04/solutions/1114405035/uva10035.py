#!/usr/bin/env python3
import sys

def count_carries(a_str: str, b_str: str) -> int:
    a = a_str[::-1]
    b = b_str[::-1]
    carries = 0
    carry_in = 0
    for i in range(max(len(a), len(b))):
        da = int(a[i]) if i < len(a) else 0
        db = int(b[i]) if i < len(b) else 0
        if da + db + carry_in >= 10:
            carries += 1
            carry_in = 1
        else:
            carry_in = 0
    return carries

def process_input(input_text: str) -> str:
    lines = input_text.strip().splitlines()
    results = []
    for line in lines:
        parts = line.split()
        if len(parts) < 2:
            continue
        a, b = parts[0], parts[1]
        if a == '0' and b == '0':
            break
        c = count_carries(a, b)
        if c == 0:
            results.append("No carry operation.")
        elif c == 1:
            results.append("1 carry operation.")
        else:
            results.append(f"{c} carry operations.")
    return '\n'.join(results)

def main():
    input_text = sys.stdin.read()
    if input_text:
        print(process_input(input_text))

if __name__ == '__main__':
    main()
