from typing import List


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    outputs: List[str] = []
    cases = int(lines[0])
    for i in range(1, cases + 1):
        n_str, p_str, idx_str = lines[i].split()
        n = int(n_str)
        p = float(p_str)
        player = int(idx_str)

        if p == 0.0:
            outputs.append('0.0000')
            continue

        if p == 1.0:
            outputs.append('1.0000' if player == 1 else '0.0000')
            continue

        base = (1.0 - p) ** (player - 1)
        cycle = (1.0 - p) ** n
        probability = base * p / (1.0 - cycle)
        outputs.append(f'{probability:.4f}')

    return '\n'.join(outputs)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
