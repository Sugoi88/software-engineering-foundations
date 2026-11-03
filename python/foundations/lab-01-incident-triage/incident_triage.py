service_name = input("Service Name: ")
affected_users = int(input("Affected Users: "))
service_down = input("Service Down: yes/no ")
security_related = input("Security related: yes/no ")

if security_related == "yes" or (service_down == "yes" and affected_users >= 50):
	severity = "CRITICAL"

elif service_down == "yes" or affected_users >= 20:
	severity = "HIGH"

elif affected_users >= 5:
	severity = "MEDIUM"

else:
	severity = "LOW"

print("--- Incident Summary ---")
print(f"Service: {service_name}")
print(f"Affected Users: {affected_users}")
print(f"Service Down: {service_down}")
print(f"Security Related: {security_related}")
print(f"Severity: {severity}")
