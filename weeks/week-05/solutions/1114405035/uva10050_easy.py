def process_input(input_text: str) -> str:
    data = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not data:
        return ''

    output = []
    idx = 0
    t = int(data[idx])
    idx += 1

    for _ in range(t):
        n = int(data[idx]); idx += 1
        p = int(data[idx]); idx += 1
        hartals = [int(data[idx + i]) for i in range(p)]
        idx += p

        days = set()
        for hartal in hartals:
            for d in range(hartal, n + 1, hartal):
                if d % 7 not in (0, 6):
                    days.add(d)

        output.append(str(len(days)))

    return '\n'.join(output)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
