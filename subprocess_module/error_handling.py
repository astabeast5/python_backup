import subprocess

# Trying a command that might fail 
try:
    result = subprocess.run(['ls', 'nonexistent_file'],
                            capture_output=True, 
                            text=True, check=True)
    print("Success", result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Command failed")
    print(f"Exit code: {e.returncode}")
    print(f"Error: {e.stdout}")

# Checking if a service is running or not 
result = subprocess.run(['which', 'docker'], capture_output=True, text=True)
if result.returncode == 0:
    print("Docker is installed")
else:
    print("Docker not found ")

"""
EXPECTED OUTPUT is as follows:
Command failed
Exit code: 2
Error: 
Docker is installed
"""
