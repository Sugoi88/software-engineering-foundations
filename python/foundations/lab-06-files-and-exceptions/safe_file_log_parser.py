events = []

def parse_log(line):
	parts = line.split("|")
	if len(parts) != 4:
		return None
	else:
		event = {
			"date": parts[0],
			"event": parts[1].strip().lower(),
			"user": parts[2],
			"source_ip": parts[3]
			}
	return event

try:
	with open("security.log", "r") as file:
		for line in file:
			line = line.strip()
			event = parse_log(line)
			if event is not None:
				events.append(event)
except FileNotFoundError:
	print("File not found.")

for event in events:
	print(f"Date: {event['date']}")
	print(f"Event: {event['event']}")
	print(f"User: {event['user']}")
	print(f"Source IP: {event['source_ip']}")
