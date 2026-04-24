from typing import Dict, List, Tuple


def build_valid_masks(columns: int, mountain_mask: int) -> List[int]:
    valid = []
    max_mask = 1 << columns
    for mask in range(max_mask):
        if mask & mountain_mask:
            continue
        if mask & (mask << 1):
            continue
        if mask & (mask << 2):
            continue
        valid.append(mask)
    return valid


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    n, m = map(int, lines[0].split())
    grid = lines[1 : 1 + n]
    mountain_masks: List[int] = []
    for row in grid:
        mask = 0
        for index, ch in enumerate(row):
            if ch == 'H':
                mask |= 1 << index
        mountain_masks.append(mask)

    valid_masks_per_row: List[List[int]] = [build_valid_masks(m, mountain_masks[row]) for row in range(n)]

    dp: Dict[Tuple[int, int], int] = {(0, 0): 0}
    for row in range(n):
        next_dp: Dict[Tuple[int, int], int] = {}
        for current in valid_masks_per_row[row]:
            for (prev_mask, prev_prev_mask), value in dp.items():
                if current & prev_mask:
                    continue
                if current & prev_prev_mask:
                    continue
                new_value = value + current.bit_count()
                key = (current, prev_mask)
                if new_value > next_dp.get(key, 0):
                    next_dp[key] = new_value
        dp = next_dp

    result = max(dp.values()) if dp else 0
    return str(result)


def main() -> None:
    import sys
    print(process_input(sys.stdin.read()), end='')


if __name__ == '__main__':
    main()
