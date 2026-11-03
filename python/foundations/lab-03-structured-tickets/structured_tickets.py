###issue = input("Issue: ")
###priority = input("Priority: ")
###status = input("Status: ")
###user = input("User: ")

tickets = [{
	"issue": "VPN failure",
	"priority": "HIGH",
	"status": "Open",
	"user": "Morgan"
	},
	{
	"issue": "Password reset",
	"priority": "MEDIUM",
	"status": "Open",
	"user": "Jordan"
	}
]

for ticket in tickets:
        print(f"Issue: {ticket['issue']}")
        print(f"Priority: {ticket['priority']}")
        print(f"Status: {ticket['status']}")
        print(f"User: {ticket['user']}")


###print(f"Issue: {ticket['issue']}")
###print(f"Priority: {ticket['priority']}")
###print(f"Status: {ticket['status']}")
###print(f"User: {ticket['user']}")
