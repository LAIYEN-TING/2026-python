from collections import Counter
from typing import List


def process_input(input_text: str) -> str:
    lines = input_text.splitlines()
    if not lines:
        return ''

    try:
        n = int(lines[0].strip())
    except ValueError:
        return ''

    counter = Counter()
    for line in lines[1 : 1 + n]:
        for ch in line:
            if ch.isalpha():
                counter[ch.upper()] += 1

    items = sorted(counter.items(), key=lambda item: (-item[1], item[0]))
    return '\n'.join(f"{letter} {count}" for letter, count in items)


def main() -> None:
    import sys
    text = sys.stdin.read()
    print(process_input(text), end='')


if __name__ == '__main__':
    main()
