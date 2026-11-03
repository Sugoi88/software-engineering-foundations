
tickets = []

ticket_count = int(input("How many tickets do you want to enter? "))

for _ in range(ticket_count):
	ticket = {}
	ticket["issue"] = input("What is the issue: ")
	ticket["priority"] = input("What is the priority: ")
	ticket["status"] = input("What is the status: ")
	ticket["user"] = input("who is the user: ")
	tickets.append(ticket)

for ticket in tickets:
	print(f"Issue: {ticket['issue']}")
	print(f"Priority: {ticket['priority']}")
	print(f"Status: {ticket['status']}")
	print(f"User: {ticket['user']}")

print(tickets)
