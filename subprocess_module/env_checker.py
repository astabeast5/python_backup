import subprocess
import sys

def check_tool(tool_name, command):
    # Check if a DevOps tool is installed
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        version = result.stdout.strip().split('\n')[0]  # First line only
        print(f" {tool_name}: {version}")
        return True
    except (subprocess.CalledProcessError , FileNotFoundError):
        print(f" {tool_name}: Not installed")
        return False
    
print(" DevOps Environment Check ")
print("=" * 30)

# Check essential DevOps tools

tools = [
    ("Python", [sys.executable, "--version"]),
    ("Docker", ["docker", "--version"]),
    ("Git", ["git", "--version"]),
    ("AWS CLI", ["aws", "--version"])
]

installed = 0
for tool_name, command in tools:
    if check_tool(tool_name, command):
        installed +=1

print(f"\n Result: {installed}/{len(tools)} tools ready")
if installed == len(tools):
    print(" Environment ready for DevOps")
else:
    print("Some tools are missing")


"""
EXPECTED OUTPUT is as follows:
 DevOps Environment Check 
==============================
 Python: Python 3.12.0
 Docker: Docker version 24.0.5, build 12345
 Git: git version 2.41.0
 AWS CLI: aws-cli/2.14.5 Python/3.12.0 ...

 Result: 4/4 tools ready
 Environment ready for DevOps

"""
