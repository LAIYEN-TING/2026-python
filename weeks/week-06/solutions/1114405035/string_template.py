def parse_numbers(line: str) -> list[int]:
    """將一行空格分隔的數字字串轉成整數列表。"""
    return [int(x) for x in line.strip().split() if x]


def format_output(lines: list[str]) -> str:
    """將結果行串接成輸出字串。"""
    return "\n".join(lines)


def main() -> None:
    import sys

    lines = [line.strip() for line in sys.stdin if line.strip()]
    if not lines:
        return

    results = []
    for line in lines:
        values = parse_numbers(line)
        if not values:
            continue
        # 範例：將每行數字總和輸出
        results.append(str(sum(values)))

    print(format_output(results))


if __name__ == '__main__':
    main()
