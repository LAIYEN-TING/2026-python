from typing import List


def parse_sequence(input_text: str) -> List[int]:
    return [int(item) for item in input_text.strip().split() if item]


def dedupe_keep_order(numbers: List[int]) -> List[int]:
    seen = set()
    result = []
    for value in numbers:
        if value not in seen:
            seen.add(value)
            result.append(value)
    return result


def even_numbers(numbers: List[int]) -> List[int]:
    return [value for value in numbers if value % 2 == 0]


def process_sequence(input_text: str) -> str:
    numbers = parse_sequence(input_text)
    deduped = dedupe_keep_order(numbers)
    asc_sorted = sorted(numbers)
    desc_sorted = sorted(numbers, reverse=True)
    evens = even_numbers(numbers)

    lines = [
        f"dedupe: {' '.join(str(num) for num in deduped)}",
        f"asc: {' '.join(str(num) for num in asc_sorted)}",
        f"desc: {' '.join(str(num) for num in desc_sorted)}",
        f"evens: {' '.join(str(num) for num in evens)}",
    ]
    return '\n'.join(lines)


def main() -> None:
    import sys

    raw_input = sys.stdin.read().strip()
    if raw_input:
        print(process_sequence(raw_input))


if __name__ == '__main__':
    main()
