from typing import List, Tuple


def parse_student_line(line: str) -> Tuple[str, int, int]:
    parts = line.strip().split()
    if len(parts) != 3:
        raise ValueError('每筆資料應包含 name score age')
    name, score_text, age_text = parts
    return name, int(score_text), int(age_text)


def sort_students(records: List[Tuple[str, int, int]]) -> List[Tuple[str, int, int]]:
    return sorted(records, key=lambda record: (-record[1], record[2], record[0]))


def top_k_students(records: List[Tuple[str, int, int]], k: int) -> List[Tuple[str, int, int]]:
    return sort_students(records)[:k]


def process_student_ranking(input_text: str) -> str:
    lines = [line for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    first_line = lines[0].split()
    if len(first_line) != 2:
        raise ValueError('第一行應包含 n k')

    _, k_text = first_line
    k = int(k_text)
    records = [parse_student_line(line) for line in lines[1:]]
    selected = top_k_students(records, k)
    return '\n'.join(f"{name} {score} {age}" for name, score, age in selected)


def main() -> None:
    import sys

    raw_input = sys.stdin.read().strip()
    if raw_input:
        print(process_student_ranking(raw_input))


if __name__ == '__main__':
    main()
