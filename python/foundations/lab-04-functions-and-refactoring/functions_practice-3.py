def get_priority(ticket):
	return ticket["priority"]
	
ticket = {
	"issue": "Email outage",
	"priority": "HIGH",
	"status": "Open",
	"user": "Stacy"
	}

priority = get_priority(ticket)

print(f"Priority: {priority}")
