import yaml
import json

def generate_deployment_config(app_name, env , replicas):
    # Kubernetes- Style deployment
    k8s_config = {
        'apiVersion' : 'apps/v1',
        'kind' : 'Deployment',
        'metadata' : {'name' : f'{app_name}---{env}'},
        'spec' : {
            'replicas' : replicas,
            'selector' : {'matchLabels' : {'app' : app_name}},
            'template' : {
            'metadata' : {'labels' : {'app' : app_name}},
            'spec' : {
                'containers' : [{
                    'name' : app_name,
                    'image' : f'{app_name}:latest',
                    'ports' : [{'containerPort' : 8000}]
                }]
            }
        }
    }
}

    # Save as YAML
    with open(f'{app_name}--{env}-deployment.yaml', 'w') as file:
        yaml.dump(k8s_config, file, default_flow_style=False, indent=2)

    print(f"✅ Created {app_name}-{env}-deployment.yaml")
    print(f"📦 App: {app_name} | Environment: {env} | Replicas: {replicas}")

# Generate configs for different environments
generate_deployment_config("myapp", "dev", 1)
generate_deployment_config("myapp", "prod", 3)


""""
EXPECTED OUTPUT is as follows:
✅ Created myapp-dev-deployment.yaml
📦 App: myapp | Environment: dev | Replicas: 1
✅ Created myapp-prod-deployment.yaml
📦 App: myapp | Environment: prod | Replicas: 3
"""
