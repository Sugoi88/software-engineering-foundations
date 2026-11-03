ticket = {
	"issue": "Email outage",
	"affected_users": 30,
	"security_related": "No",
	}

def classify_ticket(ticket):
	if ticket["security_related"] == "Yes":
		return "CRITICAL"
	elif ticket["affected_users"] >= 20:
		return "HIGH"
	elif ticket["affected_users"] >= 5:
		return "MEDIUM"
	else:
		return "LOW"

priority = classify_ticket(ticket)

print(f"Priority: {priority}")
