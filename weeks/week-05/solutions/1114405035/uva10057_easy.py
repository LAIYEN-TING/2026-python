def process_input(input_text: str) -> str:
    numbers = [int(x) for x in input_text.strip().split() if x]
    idx = 0
    results = []

    while idx < len(numbers):
        n = numbers[idx]
        idx += 1
        if n == 0:
            break

        arr = sorted(numbers[idx:idx + n])
        idx += n
        if n % 2 == 1:
            a = arr[n // 2]
            ways = 1
        else:
            a = arr[n // 2 - 1]
            ways = arr[n // 2] - arr[n // 2 - 1] + 1

        results.append(f'{a} {arr.count(a)} {ways}')

    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
