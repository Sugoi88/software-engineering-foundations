events = []

def parse_log(line):
	parts = line.split("|")
	if len(parts) != 4:
		return None
	event = {
		"date": parts[0],
		"event": parts[1].strip().lower(),
		"user": parts[2],
		"source_ip": parts[3]
		}
	return event

def classify_event(event):
	if "failed" in event['event'] and event['user'].startswith("admin"):
		return "HIGH"
	elif "failed" in event['event']:
		return "MEDIUM"
	else:
		return "LOW"

try:
	with open("security.log", "r") as file:
		for line in file:
			line = line.strip()
			event = parse_log(line)
			if event is not None:
				event['severity'] = classify_event(event)
				events.append(event)

except FileNotFoundError:
	print("security.log file could not be found.")
except PermissionError:
	print("This file cannot be accessed.")

with open("processed_events-capstone.txt", "w") as file:
	for event in events:
		file.write(f"User: {event['user']} | Event: {event['event']} | Source IP: {event['source_ip']} | Severity: {event['severity']}\n")
