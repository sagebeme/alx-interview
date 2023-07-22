#!/usr/bin/env python3
import sys

def print_stats(total_size, status_codes):
    """
    prints out the status
    """
    print("File size: {}".format(total_size))
    for status_code in sorted(status_codes.keys()):
        if status_codes[status_code] > 0:
            print("{}: {}".format(status_code, status_codes[status_code]))
    print()

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        try:
            fields = line.strip().split()
            ip_address = fields[0]
            status_code = int(fields[-2])
            file_size = int(fields[-1])
            total_size += file_size
            status_codes[status_code] += 1
            line_count += 1

            if line_count == 10:
                print_stats(total_size, status_codes)
                line_count = 0

        except Exception as e:
            # Skip this line if we can't parse it
            pass

except KeyboardInterrupt:
    # Handle Ctrl-C
    print_stats(total_size, status_codes)
    sys.exit(0)

# Print final stats if we don't receive a keyboard interrupt
print_stats(total_size, status_codes)
