# Lab 05: Strings and Parsing

**Status: Complete**

Exercises progress through string cleanup, splitting delimited text, building dictionaries, processing multiple logs, extracting parser and classifier functions, and rejecting malformed records.

- `string_practice.py`: interactive whitespace and case normalization.
- `log_parser.py`: a three-field hostname/level/message example.
- `structured_log.py` and `multiple_log_parser.py`: four-field security events.
- `log_classifier.py` and `event_classifier_function.py`: severity rules.
- `log_parser_function.py` and `defensive_log_parser.py`: reusable parsing and field-count validation.
- `security_log_pipeline.py`: combined parsing, classification, and display.

Run from this directory:

```sh
python3 security_log_pipeline.py
```

The pipeline accepts `date|event|user|source_ip`, normalizes event names with `strip().lower()`, skips records without exactly four fields, and produces three events with severities HIGH, LOW, and MEDIUM. Source IP output uses the parsed `source_ip` field.

An event containing `failed` is HIGH when the username starts with `admin`, otherwise MEDIUM. All other events are LOW. Username matching is case-sensitive. Validation checks field count, not date or IP validity or empty fields; earlier exercises intentionally introduce these concepts one at a time.
