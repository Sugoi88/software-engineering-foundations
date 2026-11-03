instance_id = input("Enter the Instance ID: ")
environment = input("Enter the Environment: ")

instance = {}

instance["instance_id"] = instance_id
instance["environment"] = environment

print(f"Instance_ID: {instance['instance_id']}")
print(f"Environment: {instance['environment']}")



tickets = []

ticket_count = int(input("How many tickets are you entering? "))

for ticket in range(ticket_count): 
	ticket = {

	}
	ticket["issue"] = input("What is the issue you're having? ")
	ticket["priority"] = input("Ticket priority: ")
	ticket["status"] = input("Ticket Status: ")
	ticket["user"] = input("Who is the user experiencing the issue? ")
	tickets.append(ticket)

for ticket in tickets:
	print(ticket["issue"])
	print(ticket["priority"])
	print(ticket["status"])
	print(ticket["user"])
