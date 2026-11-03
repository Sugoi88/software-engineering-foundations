logs = [
    "2026-10-26|FAILED_LOGIN|admin|10.0.0.25",
    "2026-10-26|LOGIN_SUCCESS|morgan|10.0.0.14",
    "2026-10-26|FAILED_LOGIN|root|10.0.0.88",
    "2026-10-26|FAILED_LOGIN|admin",
    "BROKEN_LOG"
]

events = []

def parse_log(log):
	parts = log.split("|")
	if len(parts) != 4:
		return None
	else: event = {
			"date": parts[0],
			"event": parts[1].strip().lower(),
			"user": parts[2],
			"source_ip": parts[3]
			}
	return event

def classify_event(event):
	if "failed" in event["event"] and event["user"].startswith("admin"):
		return "HIGH"
	elif "failed" in event["event"]:
		return "MEDIUM"
	else:
		return "LOW"

for log in logs:
	event = parse_log(log)
	if event is not None:
		event["severity"] = classify_event(event)
		events.append(event)

for event in events:
	print(f"Date: {event['date']}")
	print(f"Event: {event['event']}")
	print(f"User: {event['user']}")
	print(f"Source IP: {event['source_ip']}")
	print(f"Severity: {event['severity']}")
