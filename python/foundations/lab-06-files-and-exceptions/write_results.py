events = [
	{
		"user": "admin",
		"event": "failed_login",
		"severity": "HIGH"
	},
	{
		"user": "morgan",
		"event": "login_success",
		"severity": "LOW"
	},
	{
		"user": "root",
		"event": "failed_login",
		"severity": "MEDIUM"
	}
]

with open("processed_events.txt", "w") as file:
	for event in events:
		file.write(f"User: {event['user']} | Event: {event['event']} | Severity: {event['severity']}\n")
