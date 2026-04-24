def process_input(input_text: str) -> str:
    tokens = input_text.strip().split()
    if not tokens:
        return ''

    n = int(tokens[0])
    q = int(tokens[1])
    idx = 2
    values = [0] * (n + 1)
    results = []

    for _ in range(q):
        op = int(tokens[idx])
        idx += 1
        if op == 1:
            i = int(tokens[idx])
            idx += 1
            values[i] ^= 1
        else:
            l = int(tokens[idx])
            r = int(tokens[idx + 1])
            idx += 2
            parity = sum(values[l:r + 1]) % 2
            results.append('1' if parity else '0')

    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
