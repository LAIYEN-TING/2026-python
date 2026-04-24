from typing import List


def rotate_text_90_degrees(lines: List[str]) -> List[str]:
    """將文字旋轉 90 度"""
    if not lines:
        return []

    # 找到最長行的長度
    max_length = max(len(line.rstrip()) for line in lines)

    # 將每一行補齊到相同長度
    padded_lines = [line.rstrip().ljust(max_length) for line in lines]

    # 旋轉
    rotated = []
    for col in range(max_length):
        new_line = ''
        for row in range(len(padded_lines) - 1, -1, -1):
            new_line += padded_lines[row][col]
        rotated.append(new_line.rstrip())

    return rotated


def process_rotated_text(input_lines: List[str]) -> str:
    """處理旋轉文字問題"""
    # 過濾空行
    lines = [line.rstrip('\n') for line in input_lines if line.strip() or line == '\n']

    rotated = rotate_text_90_degrees(lines)
    return '\n'.join(rotated)


def main() -> None:
    import sys
    input_lines = sys.stdin.readlines()
    if input_lines:
        print(process_rotated_text(input_lines))


if __name__ == '__main__':
    main()
