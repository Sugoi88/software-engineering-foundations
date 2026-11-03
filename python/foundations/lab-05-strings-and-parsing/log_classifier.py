events = [
    {
        "date": "2026-10-26",
        "event": "failed_login",
        "user": "admin",
        "source_ip": "10.0.0.25"
    },
    {
        "date": "2026-10-26",
        "event": "login_success",
        "user": "morgan",
        "source_ip": "10.0.0.14"
    },
    {
        "date": "2026-10-26",
        "event": "failed_login",
        "user": "root",
        "source_ip": "10.0.0.88"
    }
]

for event in events:
	if "failed" in event["event"] and event["user"].startswith("admin"):
		severity = "HIGH"
	elif "failed" in event["event"]:
		severity = "MEDIUM"
	else:
		severity = "LOW"
	event["severity"] = severity

for event in events:
	print(f"User: {event['user']}")
	print(f"Event: {event['event']}")
	print(f"Severity {event['severity']}")
