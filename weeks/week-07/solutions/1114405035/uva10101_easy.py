import re

SEGMENTS = {
    '0': 0x3F,
    '1': 0x06,
    '2': 0x5B,
    '3': 0x4F,
    '4': 0x66,
    '5': 0x6D,
    '6': 0x7D,
    '7': 0x07,
    '8': 0x7F,
    '9': 0x6F,
}
REVERSE = {v: k for k, v in SEGMENTS.items()}
REMOVE = {}
ADD = {}
for digit, pattern in SEGMENTS.items():
    REMOVE[digit] = []
    ADD[digit] = []
    for bit in range(7):
        mask = 1 << bit
        if pattern & mask:
            new_pattern = pattern ^ mask
            if new_pattern in REVERSE:
                REMOVE[digit].append(REVERSE[new_pattern])
        else:
            new_pattern = pattern | mask
            if new_pattern in REVERSE:
                ADD[digit].append(REVERSE[new_pattern])

NUMBER_RE = re.compile(r'[+-]?\d+')


def evaluate_side(expr: str) -> int:
    return sum(int(x) for x in NUMBER_RE.findall(expr))


def process_input(input_text: str) -> str:
    line = input_text.strip()
    if not line:
        return ''
    expression = line.split('#', 1)[0]
    chars = list(expression)
    digits = [i for i, ch in enumerate(chars) if ch.isdigit()]
    if not digits:
        return 'No'

    def expression_value(expr: str) -> int:
        left, right = expr.split('=', 1)
        return evaluate_side(left) - evaluate_side(right)

    for src in digits:
        for dst in digits:
            if src == dst:
                continue
            for new_src in REMOVE[chars[src]]:
                for new_dst in ADD[chars[dst]]:
                    chars[src] = new_src
                    chars[dst] = new_dst
                    candidate = ''.join(chars)
                    if expression_value(candidate) == 0:
                        return f'{candidate}#'
            chars[src] = expression[src]
            chars[dst] = expression[dst]

    return 'No'


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.readline()), end='')
