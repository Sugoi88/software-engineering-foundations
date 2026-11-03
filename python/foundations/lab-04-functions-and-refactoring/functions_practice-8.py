tickets = [{
	"issue": "Forgotten Password",
	"affected_users": 36,
	"security_related": "No"
	},
	{
	"issue": "VPN Failure",
	"affected_users": 17,
	"security_related": "No"
        },
	{
	"issue": "Email Outage",
	"affected_users": 3,
	"security_related": "No"
        }]
	
def classify_ticket(ticket):
	if ticket["security_related"] == "Yes":
		return "CRITICAL"
	elif ticket["affected_users"] >= 30:
		return "HIGH"
	elif ticket["affected_users"] >= 15:
		return "MEDIUM"
	else:
		return "LOW"

def display_ticket(ticket):
	print(f"Issue: {ticket['issue']}")
	print(f"Affected Users: {ticket['affected_users']}")
	print(f"Security Related: {ticket['security_related']}")
	print(f"Priority: {ticket['priority']}")

def process_tickets(tickets):
	for ticket in tickets:
		ticket["priority"] = classify_ticket(ticket)
		display_ticket(ticket)

process_tickets(tickets)
