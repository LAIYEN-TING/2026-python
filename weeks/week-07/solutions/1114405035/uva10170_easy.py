def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    output_lines = []
    for line in lines:
        s, d = map(int, line.split())
        current = s
        total_days = s
        while total_days < d:
            current += 1
            total_days += current
        output_lines.append(str(current))

    return '\n'.join(output_lines)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
