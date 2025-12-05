import shutil 

# Checking th edisk usage of current directory
usage = shutil.disk_usage(".")

# Converting bytes to GB for easier reading
total_gb = usage.total / (1024**3)
used_gb = usage.used / (1024**3)
free_gb = usage.free / (1024**3)

print("Disk Usage:")
print(f"Total: {total_gb: .2f} GB")
print(f"Used: {used_gb: .2f} GB")
print(f"Free: {free_gb: .2f} GB")

# Checking if the space is enough or not 
if free_gb > 800:
    print("You got Enough Space")
else:
    print("Low disk Space")


"""
EXPECTED OUTPUT is as follows:
Disk Usage:
Total:  1006.85 GB
Used:  23.11 GB
Free:  932.53 GB
You got Enough Space

"""
