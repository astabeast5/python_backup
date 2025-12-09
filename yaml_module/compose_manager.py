import yaml

# Read existing file
with open('docker-compose.yml', 'r') as file:
    compose = yaml.safe_load(file)

print("original services: ")
for service in compose['services']:
    print(f"- {service}")

# Add a new service 
compose['services']['redis'] = {
    'image': 'redis:alpine',
    'ports': ['6379:6379']
}

# Modify existing service
compose['services']['web']['ports'] = ['8080:80']

#Write the file
with open('docker-compose.yml', 'w') as file:
    yaml.dump(compose, file, default_flow_style=False, indent=2)

print("\nUpdated services:")
for service_name, config in compose['services'].items():
    image = config['image']
    ports = config.get('ports', 'No ports')
    print(f"- {service_name}: {image} | Ports: {ports}")

"""
EXPECTED OUTPUT is as follows:
original services: Before making any change in the docker-compose.yml file
- database
- redis
- web

Updated services:  Changes after running the compose_manager.py
- database: pstgres | Ports: No ports
- redis: redis:alpine | Ports: ['6379:6379']
- web: nginx | Ports: ['8080:80']
"""
