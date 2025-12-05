import subprocess

# Run a simple command
result = subprocess.run(['ls', '-l'], capture_output=True, text=True)

print("Command Output:")

print(result.stdout)

print(f"Exist code: {result.returncode}")

"""
EXPECTED OUTPUT is as follows:
Command Output:
total 4
-rw-r--r-- 1 OASTA OASTA 354 Dec  5 16:04 subprocess_run.py

Exist code: 0
"""
