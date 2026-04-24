from typing import List


def process_input(input_text: str) -> str:
    lines = [line.strip() for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    results: List[str] = []
    idx = 0
    t = int(lines[idx])
    idx += 1

    for _ in range(t):
        total_days = int(lines[idx])
        idx += 1
        party_count = int(lines[idx])
        idx += 1
        parties = [int(lines[idx + i]) for i in range(party_count)]
        idx += party_count

        strike_days = [False] * (total_days + 1)
        for h in parties:
            for day in range(h, total_days + 1, h):
                weekday = day % 7
                if weekday == 6 or weekday == 0:
                    continue
                strike_days[day] = True

        results.append(str(sum(strike_days)))

    return '\n'.join(results)


if __name__ == '__main__':
    import sys
    print(process_input(sys.stdin.read()), end='')
