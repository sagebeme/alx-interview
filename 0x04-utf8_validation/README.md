0x04. UTF-8 validation
======================

This project implements **UTF-8 validation**: given a list of integers (each representing one byte), determine if the sequence is valid UTF-8. You practice bit manipulation and the UTF-8 encoding rules.

Tasks
-----

### 0. UTF-8 validation

mandatory

Implement a function `validUTF8(data)` that returns True if the list of integers is valid UTF-8, False otherwise. Multi-byte characters follow the leading byte pattern (e.g. 110xxxxx for 2-byte). Run: `python3 0-main.py` or import and call with a list.

**Repo:**

-   GitHub repository: `alx-interview`
-   Directory: `0x04-utf8_validation`
-   File: (main solution file)

---

**How to do the exercises yourself**

1. Check the leading byte to see how many continuation bytes (10xxxxxx) follow.
2. Validate each continuation byte and advance; return False on any invalid sequence.
