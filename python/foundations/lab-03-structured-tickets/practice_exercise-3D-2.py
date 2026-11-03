instances = []

instance_count = int(input("How many Instances are you creating: "))

for _ in range(instance_count):
	instance = {}
	instance["instance_id"] = input("What is the Instance ID: ")
	instance["environment"] = input("What is the Environment: ")
	instance["state"] = input("What is the instance state: ")
	instance["owner"] = input("Who is the instance owner: ")
	instances.append(instance)

for instance in instances:
	print(f"Instance ID: {instance['instance_id']}")
	print(f"Instance Environment: {instance['environment']}")
	print(f"Instance State: {instance['state']}")
	print(f"Instance Owner: {instance['owner']}")
