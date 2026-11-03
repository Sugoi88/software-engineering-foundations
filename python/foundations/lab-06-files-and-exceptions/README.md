# Lab 06: Files and Exceptions

**Status: Complete, including the Lab 06J capstone**

## Exercises

The scripts progress from `read_file.py`, `with_open.py`, and `read_lines.py` through file-based parsing, missing-file handling, permission-error handling, defensive parsing, and output writing. `multiple_file_errors.py` deliberately opens `missing.log` to exercise the missing-file handler. `write_results.py` writes three predefined dictionaries to `processed_events.txt`.

## Capstone

`full_log_pipeline.py` reads `security.log`, strips each line, calls `parse_log()`, skips malformed records, classifies valid events, collects dictionaries, and writes `processed_events-capstone.txt`.

Run from this directory with Python 3:

```sh
python3 full_log_pipeline.py
```

Input uses four pipe-separated fields:

```text
2026-10-26|FAILED_LOGIN|admin|10.0.0.25
```

`parse_log()` validates field count and normalizes the event name. `classify_event()` returns HIGH for event names containing `failed` with usernames starting with `admin`, MEDIUM for other `failed` events, and LOW otherwise. The main loop owns collection; the output loop owns formatting and writing.

The included input produces four output records:

```text
User: admin | Event: failed_login | Source IP: 10.0.0.25 | Severity: HIGH
User: morgan | Event: login_success | Source IP: 10.0.0.14 | Severity: LOW
User: root | Event: failed_login | Source IP: 10.0.0.88 | Severity: MEDIUM
User: admin | Event: vpn_failure | Source IP: 123.456.32.60 | Severity: LOW
```

`BROKEN` and blank lines are skipped. `vpn_failure` is LOW because `failure` does not contain `failed`.

## Error handling and current limits

Input `FileNotFoundError` and `PermissionError` produce explanatory messages. The writing stage runs after these handlers, so failed input access can create or overwrite the output with an empty file. Write mode replaces existing output, and output-file errors are not handled in this exercise.

Validation checks only that there are four fields. Dates, empty values, and IP addresses are not validated; the included `123.456.32.60` illustrates text processing and is not a valid IPv4 address. Username matching remains case-sensitive. These are introductory exercises, with the curriculum structure preserved.
