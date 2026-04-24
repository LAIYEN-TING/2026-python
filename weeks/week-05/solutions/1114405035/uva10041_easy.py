def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    output_lines = []
    case_count = int(lines[0])
    for i in range(case_count):
        values = list(map(int, lines[i + 1].split()))
        positions = sorted(values[1:])
        median = positions[len(positions) // 2]
        output_lines.append(str(sum(abs(x - median) for x in positions)))

    return '\n'.join(output_lines)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
