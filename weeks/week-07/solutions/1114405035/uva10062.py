from typing import List


class FenwickTree:
    def __init__(self, size: int) -> None:
        self.size = size
        self.tree = [0] * (size + 1)

    def add(self, index: int, value: int) -> None:
        while index <= self.size:
            self.tree[index] += value
            index += index & -index

    def prefix_sum(self, index: int) -> int:
        result = 0
        while index > 0:
            result += self.tree[index]
            index -= index & -index
        return result

    def find_kth(self, k: int) -> int:
        index = 0
        bit_mask = 1 << (self.size.bit_length() - 1)
        while bit_mask:
            next_index = index + bit_mask
            if next_index <= self.size and self.tree[next_index] < k:
                k -= self.tree[next_index]
                index = next_index
            bit_mask >>= 1
        return index + 1


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    n = int(lines[0])
    counts = [0] * n
    for i in range(1, n):
        counts[i] = int(lines[i])

    fenwick = FenwickTree(n)
    for i in range(1, n + 1):
        fenwick.add(i, 1)

    answer: List[str] = [''] * n
    for i in range(n - 1, -1, -1):
        larger_before = i - counts[i]
        rank = larger_before + 1
        # Find the (rank)-th largest remaining number.
        remaining = fenwick.prefix_sum(n)
        target = remaining - rank + 1
        value = fenwick.find_kth(target)
        answer[i] = str(value)
        fenwick.add(value, -1)

    return '\n'.join(answer)


def main() -> None:
    import sys
    print(process_input(sys.stdin.read()), end='')


if __name__ == '__main__':
    main()
