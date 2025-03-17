import sys
import re


def parse_log_line(line: str) -> dict:
    pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (\w.+)"
    match = re.match(pattern, line)
    if match:
        return {
            "timestamp": match.group(1),
            "level": match.group(2),
            "message": match.group(3)
        }
    else:
        raise ValueError("Invalid format log line")


def load_logs(file_path: str) -> list:
    logs = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                try:
                    logs.append(parse_log_line(line.strip()))
                except ValueError:
                    print(f"Skipping invalid log line: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)
    except IOError:
        print(f"Error: Could not read the file '{file_path}'.")
        sys.exit(1)
    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    valid_levs: set = {"INFO", "ERROR", "DEBUG", "WARNING"}
    if level.upper() not in valid_levs:
        raise ValueError(f"Invalid log level: {level}")
    return [log for log in logs if log["level"] == level.upper()]


def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        level = log["level"]
        counts[level] = counts.get(level, 0) + 1
    return dict(sorted(counts.items()))


def display_log_counts(counts: dict) -> None:
    print(f"{'Рівень логування':<15} | {'Кількість':<10}")
    print("-" * 26)
    for level, count in counts.items():
        print(f"{level:<15} | {count:<10}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("File not specified.")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)

    if not logs:
        print("No valid log records found in the file.")
        sys.exit(1)

    if len(sys.argv) == 2:
        counts = count_logs_by_level(logs)
        display_log_counts(counts)

    elif len(sys.argv) == 3:
        level = sys.argv[2]
        try:
            filtered_logs = filter_logs_by_level(logs, level)
            print(f"Logs for level '{level.upper()}':")
            for log in filtered_logs:
                print(f"{log['timestamp']} - {log['message']}")
        except ValueError as e:
            print(e)
