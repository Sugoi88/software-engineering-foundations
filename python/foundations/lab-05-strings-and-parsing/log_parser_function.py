logs = [
	"2026-10-26|FAILED_LOGIN|admin|10.0.0.25",
	"2026-10-26|LOGIN_SUCCESS|morgan|10.0.0.14",
	"2026-10-26|FAILED_LOGIN|root|10.0.0.88",
	]

events = []

def parse_log(log):
	parts = log.split("|")
	event = {
		"date": parts[0],
		"event": parts[1].strip().lower(),
		"user": parts[2],
		"source_ip": parts[3],
		}
	return event

for log in logs:
	event = parse_log(log)
	events.append(event)

for event in events:
	print(f"Date: {event['date']}")
	print(f"Event: {event['event']}")
	print(f"User: {event['user']}")
	print(f"Source IP: {event['source_ip']}")
