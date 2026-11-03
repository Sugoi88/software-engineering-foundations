tickets = [{
        "issue": "Email outage",
        "priority": "HIGH",
        "status": "Open",
        "user": "Alex"
        },
	{"issue": "VPN Failure",
	"priority": "MEDIUM",
	"status": "Open",
	"user": "Stacy"
	},
	{"issue": "Password reset",
	"priority": "LOW",
	"status": "Closed",
	"user": "The same person that called yesterday about the same issue, and the day before that..."
	}]

def display_ticket(ticket):
        print(f"Ticket Issue: {ticket['issue']}")
        print(f"Ticket Priority: {ticket['priority']}")
        print(f"Ticket Status: {ticket['status']}")
        print(f"Ticket User: {ticket['user']}")

for ticket in tickets:
	display_ticket(ticket)
