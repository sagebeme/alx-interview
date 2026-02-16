0x03. Log parsing
=================

This project parses **logs from stdin**: read line by line, parse a format (e.g. IP, date, status, size), and print statistics (e.g. total file size and count by status code). You practice stdin, parsing, and signal handling (e.g. SIGINT).

Tasks
-----

### 0. Log parsing / stats

mandatory

Read log lines from stdin, parse each line (e.g. regex or split), aggregate file size and status-code counts, and print stats every 10 lines or on Ctrl+C. Run: `python3 0-stats.py` and pipe a log file or type input.

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x03-log_parsing`
-   File: `0-stats.py`

---

**How to run / test**

1. Run: `python3 0-stats.py < logfile` or generate lines and pipe.
2. Trigger a keyboard interrupt (Ctrl+C) to see final stats if required.
