from collections import defaultdict
from typing import Dict, List


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    n = int(lines[0])
    values: List[int] = [int(line) for line in lines[1 : 1 + n]]

    pair_sums: Dict[int, int] = defaultdict(int)
    for a in values:
        for b in values:
            pair_sums[a + b] += 1

    triple_sums: Dict[int, int] = defaultdict(int)
    for a in values:
        for b in values:
            for c in values:
                triple_sums[a + b + c] += 1

    total = 0
    for f in values:
        for triple_sum, count in triple_sums.items():
            total += count * pair_sums[f - triple_sum]

    return str(total)


def main() -> None:
    import sys
    print(process_input(sys.stdin.read()), end='')


if __name__ == '__main__':
    main()
