import json

def load_config(env):
    filename = f"config_{env}.json"
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Config file {filename} not found!")
        return None

def create_env_config(env, port, debug_mode):
    config = {
        "app_name": "devops-app",
        "environment": env,
        "port": port,
        "debug": debug_mode,
        "database": {
            "host": "localhost" if env == "dev" else "prod-db.company.com",
            "port": 5432
        }
    }

    filename = f"config_{env}.json"
    with open(filename, 'w') as file:
        json.dump(config, file, indent=2)

    print(f"Created {filename}")

# Create configs for different environments
create_env_config("dev", 8000, True)
create_env_config("prod", 80, False)

# Load and display dev config
dev_config = load_config("dev")
if dev_config:
    print(f"\nDev Environment - Port: {dev_config['port']}, Debug: {dev_config['debug']}")

"""
EXPECTED OUTPUT is as follows:
Created config_dev.json
Created config_prod.json

Dev Environment - Port: 8000, Debug: True
"""
