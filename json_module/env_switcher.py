import json
import sys

def start_app(env):
    config_file = f"config_{env}.json"

    try:
        with open(config_file, 'r') as file:
            config = json.load(file)

        print(f"🚀 Starting {config['app_name']} in {config['environment']} mode")
        print(f"📡 Server running on port {config['port']}")
        print(f"🗄️  Database: {config['database']['host']}:{config['database']['port']}")
        print(f"🐛 Debug mode: {'ON' if config['debug'] else 'OFF'}")

    except FileNotFoundError:
        print(f"❌ Configuration file not found: {config_file}")
        
# Usage:
if len(sys.argv) > 1:
    env = sys.argv[1]
    start_app(env)
else:
    print("Usage: Python app_launcher.py <dev|prod>")

"""
EXPECTED OUTPUT is as follows:
First you will run the application 
                                         python env_switcher.py
you will get the following output 
                                Usage: Python app_launcher.py <dev|prod>
this shows you got two files you will run them one at a time to get response which is as follows:
                                       
COMMAND:                                python app_launcher.py dev
OUTPUT:
                                  🚀 Starting devops-app in dev mode
                                  📡 Server running on port 8000
                                  🗄️  Database: localhost:5432
                                  🐛 Debug mode: ON

COMMAND:                                python app_launcher.py prod
OUTPUT:
                                  🚀 Starting devops-app in prod mode
                                  📡 Server running on port 80
                                  🗄️  Database: prod-db.company.com:5432
                                  🐛 Debug mode: OFF
"""
