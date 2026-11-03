tickets = [
    {
        "issue": "Email outage",
        "affected_users": 30,
        "security_related": "No"
    },
    {
        "issue": "Suspicious login",
        "affected_users": 1,
        "security_related": "Yes"
    },
    {
        "issue": "Printer offline",
        "affected_users": 3,
        "security_related": "No"
    }
]

def classify_ticket(ticket):
        if ticket["security_related"] == "Yes":
                return "CRITICAL"
        elif ticket["affected_users"] >= 20:
                return "HIGH"
        elif ticket["affected_users"] >= 5:
                return "MEDIUM"
        else:
                return "LOW"

for ticket in tickets:
	ticket["priority"] = classify_ticket(ticket)

for ticket in tickets:
	print(f"Issue: {ticket['issue']}")
	print(f"Affected Users: {ticket['affected_users']}")
	print(f"Security related: {ticket['security_related']}")
	print(f"Priority: {ticket['priority']}")

