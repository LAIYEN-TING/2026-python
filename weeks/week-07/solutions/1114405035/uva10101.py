import re
from typing import Dict, List

SEGMENT_MAP: Dict[str, int] = {
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
REVERSE_SEGMENT_MAP: Dict[int, str] = {value: key for key, value in SEGMENT_MAP.items()}
DIGITS = list(SEGMENT_MAP.keys())

REMOVE_MAP: Dict[str, List[str]] = {}
ADD_MAP: Dict[str, List[str]] = {}
for digit, pattern in SEGMENT_MAP.items():
    remove_list: List[str] = []
    add_list: List[str] = []
    for bit in range(7):
        mask = 1 << bit
        if pattern & mask:
            new_pattern = pattern ^ mask
            if new_pattern in REVERSE_SEGMENT_MAP:
                remove_list.append(REVERSE_SEGMENT_MAP[new_pattern])
        else:
            new_pattern = pattern | mask
            if new_pattern in REVERSE_SEGMENT_MAP:
                add_list.append(REVERSE_SEGMENT_MAP[new_pattern])
    REMOVE_MAP[digit] = remove_list
    ADD_MAP[digit] = add_list

NUMBER_PATTERN = re.compile(r'[+-]?\d+')


def evaluate_side(side: str) -> int:
    tokens = NUMBER_PATTERN.findall(side)
    return sum(int(token) for token in tokens)


def expression_value(expression: str) -> int:
    left, right = expression.split('=', 1)
    return evaluate_side(left) - evaluate_side(right)


def process_input(input_text: str) -> str:
    line = input_text.strip()
    if not line:
        return ''

    if '#' in line:
        expression = line.split('#', 1)[0]
    else:
        expression = line

    chars = list(expression)
    digit_positions = [i for i, ch in enumerate(chars) if ch.isdigit()]
    if not digit_positions:
        return 'No'

    source_options: Dict[int, List[str]] = {}
    dest_options: Dict[int, List[str]] = {}
    for pos in digit_positions:
        digit = chars[pos]
        source_options[pos] = REMOVE_MAP[digit]
        dest_options[pos] = ADD_MAP[digit]

    if expression_value(expression) == 0:
        return f'{expression}#'

    original_chars = list(chars)
    for src in digit_positions:
        for dst in digit_positions:
            if src == dst:
                continue
            for new_src in source_options[src]:
                for new_dst in dest_options[dst]:
                    chars = original_chars.copy()
                    chars[src] = new_src
                    chars[dst] = new_dst
                    candidate = ''.join(chars)
                    if expression_value(candidate) == 0:
                        return f'{candidate}#'
    return 'No'


def main() -> None:
    import sys
    print(process_input(sys.stdin.readline()), end='')


if __name__ == '__main__':
    main()
