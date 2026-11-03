tickets = []
ticket_count = 0

while True:
	try:
		ticket_count = int(input("How many tickets do you want to enter? "))
		if ticket_count >= 1:
			print(f"You entered: {ticket_count}.")
			break
		else:
			print("Ticket count must be greater than 0.")
	except ValueError:
		print("Please enter a valid number.")

for _ in range(ticket_count):
	ticket = input("Enter ticket: ")
	tickets.append(ticket)

high_count = 0
medium_count = 0
low_count = 0

for ticket in tickets:
	if ticket == "VPN failure" or  ticket == "Email outage":
		priority = "HIGH"
		high_count = high_count + 1

	elif ticket == "Password reset" or ticket == "Account locked":
		priority = "MEDIUM"
		medium_count = medium_count + 1

	else:
		priority = "LOW"
		low_count = low_count + 1

	print(f"Processing ticket: {ticket}")
	print(f"{ticket}: {priority}")

count = len(tickets)

print(f"HIGH: {high_count}")
print(f"MEDIUM: {medium_count}")
print(f"LOW: {low_count}")
print(f"Total Tickets: {count}")
