from typing import List


def is_jolly_sequence(numbers: List[int]) -> bool:
    n = len(numbers)
    if n <= 1:
        return True

    diffs = set(abs(numbers[i] - numbers[i - 1]) for i in range(1, n))
    return diffs == set(range(1, n))


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.splitlines() if line.strip()]
    results = []
    for line in lines:
        parts = [int(x) for x in line.split()]
        if not parts:
            continue
        n = parts[0]
        numbers = parts[1:1 + n]
        if is_jolly_sequence(numbers):
            results.append('Jolly')
        else:
            results.append('Not jolly')
    return '\n'.join(results)


def main() -> None:
    import sys
    print(process_input(sys.stdin.read()), end='')


if __name__ == '__main__':
    main()
