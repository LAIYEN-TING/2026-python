def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    n = int(lines[0])
    counts = [0] * n
    for i in range(1, n):
        counts[i] = int(lines[i])

    available = list(range(1, n + 1))
    result = [''] * n
    for i in range(n - 1, -1, -1):
        larger_before = i - counts[i]
        index = len(available) - 1 - larger_before
        result[i] = str(available.pop(index))

    return '\n'.join(result)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
