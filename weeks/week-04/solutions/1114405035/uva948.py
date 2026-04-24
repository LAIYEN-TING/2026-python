#!/usr/bin/env python3
import sys

def process_input(input_text: str) -> str:
    tokens = input_text.split()
    if not tokens:
        return ""
    
    it = iter(tokens)
    try:
        m_str = next(it)
        m = int(m_str)
        outputs = []
        for case in range(m):
            n = int(next(it))
            k = int(next(it))
            
            maybe_light = [True] * (n + 1)
            maybe_heavy = [True] * (n + 1)
            
            for _ in range(k):
                pi = int(next(it))
                left = [int(next(it)) for _ in range(pi)]
                right = [int(next(it)) for _ in range(pi)]
                result = next(it)
                
                left_set = set(left)
                right_set = set(right)
                involved = left_set | right_set
                
                if result == '=':
                    for coin in involved:
                        maybe_light[coin] = False
                        maybe_heavy[coin] = False
                elif result == '<':
                    for coin in range(1, n + 1):
                        if coin not in involved:
                            maybe_light[coin] = False
                            maybe_heavy[coin] = False
                        elif coin in left_set:
                            maybe_heavy[coin] = False
                        elif coin in right_set:
                            maybe_light[coin] = False
                elif result == '>':
                    for coin in range(1, n + 1):
                        if coin not in involved:
                            maybe_light[coin] = False
                            maybe_heavy[coin] = False
                        elif coin in left_set:
                            maybe_light[coin] = False
                        elif coin in right_set:
                            maybe_heavy[coin] = False
            
            candidates = [c for c in range(1, n + 1) if maybe_light[c] or maybe_heavy[c]]
            outputs.append(str(candidates[0]) if len(candidates) == 1 else "0")
            
        return '\n\n'.join(outputs)
    except StopIteration:
        return ""

def main() -> None:
    input_text = sys.stdin.read()
    if input_text:
        print(process_input(input_text), end='')

if __name__ == '__main__':
    main()
