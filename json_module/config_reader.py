import json

# Read the config file 
with open('app_config.json', 'r') as file:
    config = json.load(file)

print("App Name: ", config['app-name'])
print("Port: ", config['port'])
print("Debug: ", config['debug'])


"""
EXPECTED OUTPUT is as follows:
App Name:  my-app
Port:  8000
Debug:  True

"""
