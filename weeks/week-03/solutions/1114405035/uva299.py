from typing import List


def count_swaps_to_sort(arr: List[int]) -> int:
    """計算氣泡排序所需的交換次數"""
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return swaps


def process_train_sorting(input_lines: List[str]) -> str:
    """處理火車排序問題"""
    results = []
    i = 0
    while i < len(input_lines):
        line = input_lines[i].strip()
        if not line:
            i += 1
            continue

        # 第一行：測試案例數量
        if line.isdigit():
            num_cases = int(line)
            i += 1
            for _ in range(num_cases):
                if i >= len(input_lines):
                    break
                # 火車長度
                length_line = input_lines[i].strip()
                if not length_line:
                    i += 1
                    continue
                length = int(length_line)
                i += 1

                # 火車排列
                if i >= len(input_lines):
                    break
                train_line = input_lines[i].strip()
                if not train_line:
                    i += 1
                    continue
                train = [int(x) for x in train_line.split()]
                i += 1

                # 計算交換次數
                swaps = count_swaps_to_sort(train[:])  # 複製避免修改原陣列
                results.append(f"Optimal train swapping takes {swaps} swaps.")
        else:
            i += 1

    return '\n'.join(results)


def main() -> None:
    import sys
    input_lines = [line for line in sys.stdin if line.strip()]
    if input_lines:
        print(process_train_sorting(input_lines))


if __name__ == '__main__':
    main()
