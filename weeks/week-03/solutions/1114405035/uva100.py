from typing import List, Tuple, Set


def calculate_cycle_length(n: int) -> int:
    """計算 Collatz 序列的 cycle-length"""
    count = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    return count


def find_max_cycle_length(i: int, j: int) -> int:
    """在區間 [min(i,j), max(i,j)] 內找到最大的 cycle-length"""
    start, end = min(i, j), max(i, j)
    max_length = 0
    for num in range(start, end + 1):
        length = calculate_cycle_length(num)
        if length > max_length:
            max_length = length
    return max_length


def process_input_line(line: str) -> str:
    """處理輸入行，輸出結果"""
    parts = line.strip().split()
    if len(parts) != 2:
        raise ValueError("每行應包含兩個整數")
    i, j = int(parts[0]), int(parts[1])
    max_length = find_max_cycle_length(i, j)
    return f"{i} {j} {max_length}"


def main() -> None:
    import sys
    for line in sys.stdin:
        if line.strip():
            print(process_input_line(line))


if __name__ == '__main__':
    main()
