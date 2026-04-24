def process_input(input_text: str) -> str:
    lines = [line for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    output = []
    t = int(lines[0])
    for row in lines[1:t + 1]:
        tokens = row.split()
        n = int(tokens[0])
        p = float(tokens[1])
        i = int(tokens[2])

        if p == 1.0:
            output.append('1.0000' if i == 1 else '0.0000')
            continue

        q = 1.0 - p
        result = (q ** (i - 1)) * p / (1.0 - q ** n)
        output.append(f'{result:.4f}')

    return '\n'.join(output)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
