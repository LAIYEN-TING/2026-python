def process_tex_quotes(input_text: str) -> str:
    """處理 TeX 引號替換"""
    result = []
    quote_count = 0

    for char in input_text:
        if char == '"':
            if quote_count % 2 == 0:
                result.append('``')
            else:
                result.append("''")
            quote_count += 1
        else:
            result.append(char)

    return ''.join(result)


def main() -> None:
    import sys
    for line in sys.stdin:
        print(process_tex_quotes(line.rstrip()))


if __name__ == '__main__':
    main()
