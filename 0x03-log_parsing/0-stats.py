#!/usr/bin/env python3

import sys

def print_statistics(total_size, status_counts):
    print("File size:", total_size)
    for status_code in sorted(status_counts):
        print(f"{status_code}: {status_counts[status_code]}")

def process_logs():
    total_size = 0
    status_counts = {}

    try:
        for line_num, line in enumerate(sys.stdin, start=1):
            try:
                ip_address, _, _, _, _, status_code, file_size = line.strip().split(' ')
                status_code = int(status_code)
                file_size = int(file_size)
            except ValueError:
                continue

            total_size += file_size
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if line_num % 10 == 0:
                print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        pass

    print_statistics(total_size, status_counts)


if __name__ == "__main__":
    process_logs()
