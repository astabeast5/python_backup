import yaml

with open('docker-compose.yml', 'r') as file:
    compose = yaml.safe_load(file)

print("Services in Docker Compose/:")
for service_name, config in compose['services'].items():
    print(f"- {service_name}: {config['image']}")


"""
EXPECTED OUTPUT is as follows:
Services in Docker Compose/:
- web: nginx
- database: pstgres
"""
