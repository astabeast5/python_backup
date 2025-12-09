import json

# Read the config file 
with open('app_config.json', 'r') as file:
    config = json.load(file)

print(" Original config: ")
print("App Name: ", config['app-name'])
print("Port: ", config['port'])
print("Debug: ", config['debug'])

# Modifying the config file:
config['port'] = 9000
config['environment'] = 'production'
config['debug'] = False

# Write the modified config back to the file
with open('app_config.json', 'w') as file:
    json.dump(config, file, indent=4)

print("\nConfig updated! New values:")
print("Port:", config['port'])
print("Environment:", config['environment'])
print("Debug Mode:", config['debug'])


"""
EXPECTED OUTPUT is as follows:
 Original config: 
App Name:  my-app
Port:  8000
Debug:  True

Config updated! New values:
Port: 9000
Environment: production
Debug Mode: False
"""
