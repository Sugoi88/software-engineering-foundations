
tickets = []

ticket = {
	"issue": "Email outage",
	"priority": "HIGH",
	"status": "Open",
	"user": "Alex"
	}

def display_ticket(ticket):
	print(f"Ticket Issue: {ticket['issue']}")
	print(f"Ticket Priority: {ticket['priority']}")
	print(f"Ticket Status: {ticket['status']}")
	print(f"Ticket User: {ticket['user']}")

display_ticket(ticket)
