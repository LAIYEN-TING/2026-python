from typing import Dict, List


def valid_masks(columns: int, mountain_mask: int) -> List[int]:
    masks = []
    for mask in range(1 << columns):
        if mask & mountain_mask:
            continue
        if mask & (mask << 1):
            continue
        if mask & (mask << 2):
            continue
        masks.append(mask)
    return masks


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    n, m = map(int, lines[0].split())
    grid = lines[1 : 1 + n]
    mountain_masks = []
    for row in grid:
        mask = 0
        for idx, ch in enumerate(row):
            if ch == 'H':
                mask |= 1 << idx
        mountain_masks.append(mask)

    row_masks = [valid_masks(m, mountain_masks[i]) for i in range(n)]
    dp: Dict[tuple[int, int], int] = {(0, 0): 0}

    for i in range(n):
        next_dp: Dict[tuple[int, int], int] = {}
        for mask in row_masks[i]:
            for (prev, prev2), value in dp.items():
                if mask & prev:
                    continue
                if mask & prev2:
                    continue
                new_value = value + mask.bit_count()
                key = (mask, prev)
                if new_value > next_dp.get(key, 0):
                    next_dp[key] = new_value
        dp = next_dp

    return str(max(dp.values()) if dp else 0)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
