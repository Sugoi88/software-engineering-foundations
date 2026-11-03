log = "2026-10-26|FAILED_LOGIN|admin|10.0.0.25"

parts = log.split("|")

event = {
	"date": parts[0],
	"event": parts[1].lower(),
	"user": parts[2],
	"source_ip": parts[3]
}

print(f"Date: {event['date']}")
print(f"Event: {event['event']}")
print(f"User: {event['user']}")
print(f"Source IP: {event['source_ip']}")
