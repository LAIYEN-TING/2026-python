from collections import Counter
from typing import List, Tuple


def parse_log_line(line: str) -> Tuple[str, str]:
    parts = line.strip().split()
    if len(parts) != 2:
        raise ValueError('每筆紀錄應包含 user action')
    return parts[0], parts[1]


def user_event_counts(log_lines: List[str]) -> Counter[str]:
    counter = Counter()
    for line in log_lines:
        user, _ = parse_log_line(line)
        counter[user] += 1
    return counter


def sort_user_counts(user_counts: Counter[str]) -> List[Tuple[str, int]]:
    return sorted(user_counts.items(), key=lambda item: (-item[1], item[0]))


def top_action(log_lines: List[str]) -> Tuple[str, int]:
    action_counts = Counter()
    for line in log_lines:
        _, action = parse_log_line(line)
        action_counts[action] += 1

    if not action_counts:
        return '', 0

    max_count = max(action_counts.values())
    top_actions = [action for action, count in action_counts.items() if count == max_count]
    return sorted(top_actions)[0], max_count


def process_log_summary(input_text: str) -> str:
    lines = [line for line in input_text.strip().splitlines() if line.strip()]
    if not lines:
        return ''

    count = int(lines[0].strip())
    log_lines = lines[1:1 + count]
    user_counts = user_event_counts(log_lines)
    sorted_counts = sort_user_counts(user_counts)
    action, action_count = top_action(log_lines)

    output_lines = [f"{user} {total}" for user, total in sorted_counts]
    output_lines.append(f"top_action: {action} {action_count}")
    return '\n'.join(output_lines)


def main() -> None:
    import sys

    raw_input = sys.stdin.read().strip()
    if raw_input:
        print(process_log_summary(raw_input))


if __name__ == '__main__':
    main()
