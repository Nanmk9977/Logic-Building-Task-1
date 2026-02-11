logs = ["INFO", "ERROR", "WARNING", "ERROR"]

error_count = 0

# Checking each log entry
for entry in logs:
    if entry == "ERROR":
        error_count += 1

print("System Log Analysis")
print(" ")
print("Total ERROR entries : ", error_count)
print(" ")