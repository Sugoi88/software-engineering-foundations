log = "web-server-01|WARNING|Disk usage above 80%"

parts = log.split("|")

hostname = parts[0]
level = parts[1].lower()
message = parts[2]

print(f"Hostname: {hostname}")
print(f"Level: {level}")
print(f"Message: {message}")
