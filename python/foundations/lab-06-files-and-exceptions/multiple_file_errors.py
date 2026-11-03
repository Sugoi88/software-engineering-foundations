try:
	with open("missing.log", "r") as file:
		contents = file.read()
	print(contents)
except FileNotFoundError:
	print("File not found.")
except PermissionError:
	print("Permission denied while trying to read security.log")
