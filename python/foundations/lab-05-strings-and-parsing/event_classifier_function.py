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

def classify_event(event):
	if "failed" in event["event"] and event["user"].startswith("admin"):
		return "HIGH"
	elif "failed" in event["event"]:
		return "MEDIUM"
	else:
		return "LOW"

for event in events:
	event["severity"] = classify_event(event)

for event in events:
	print(f"User: {event['user']}")
	print(f"Event: {event['event']}")
	print(f"Severity {event['severity']}")
