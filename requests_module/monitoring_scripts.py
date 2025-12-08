import requests
import subprocess
import json

def monitor_system():
    print(f"DevOps System Monitor")
    print("=" * 30)

    # 1. Check local Docker
    try:
        result = subprocess.run(['docker', 'ps'], capture_output=True, text=True)
        containers = len(result.stdout.strip().split('\n')) - 1
        print(f" Docker: {containers} containers running")
    except:
        print("Docker : Not Available")

    # 2. Check Github API
    try:
        response = requests.get('https://api.github.com/status')
        if response.status_code == 200:
            print("Github API is Available")
        else:
            print("Github API: Issues detected")
    except:
        print("Github API is Not Available")
    
    # 3. Check Internet connectivity
    try:
        response = requests.get('https://google.com' , timeout=3)
        print("Internet: Connected")
    except:
        print("Internet: No connection")
    


monitor_system()


"""
EXPECTED OUTPUT is as follows:
DevOps System Monitor
==============================
 Docker: 0 containers running
Github API is Available
Internet: Connected

"""
