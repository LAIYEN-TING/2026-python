from typing import List


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    outputs: List[str] = []
    for line in lines:
        s, d = map(int, line.split())
        low = 0
        high = 200000000
        while low < high:
            mid = (low + high) // 2
            total_days = (mid + 1) * (2 * s + mid) // 2
            if total_days >= d:
                high = mid
            else:
                low = mid + 1
        outputs.append(str(s + low))

    return '\n'.join(outputs)


def main() -> None:
    import sys
    print(process_input(sys.stdin.read()), end='')


if __name__ == '__main__':
    main()
