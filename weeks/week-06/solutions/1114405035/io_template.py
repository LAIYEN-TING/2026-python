import sys
from typing import Iterator, List


def read_tokens() -> Iterator[str]:
    """從標準輸入讀取所有 token。"""
    for line in sys.stdin:
        for token in line.strip().split():
            yield token


def read_ints() -> List[int]:
    """讀取整個輸入並轉成整數列表。"""
    return [int(token) for token in read_tokens()]


def read_line() -> str:
    """讀取單行輸入並去除尾端換行。"""
    return sys.stdin.readline().rstrip("\n")


def main() -> None:
    data = read_ints()
    if not data:
        return

    # 範例：第一個數字是測資數量，其餘為資料
    t = data[0]
    results = []
    idx = 1
    for _ in range(t):
        if idx >= len(data):
            break
        n = data[idx]
        idx += 1
        values = data[idx: idx + n]
        idx += n
        results.append(sum(values))

    print("\n".join(str(x) for x in results))


if __name__ == '__main__':
    main()
