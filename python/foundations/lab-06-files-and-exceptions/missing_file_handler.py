try:
	with open("security.log", "r") as file:
		contents = file.read()
except FileNotFoundError:
	print("security.log was not found.")
