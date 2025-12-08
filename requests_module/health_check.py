import requests

# Health Check example
response = requests.get('https://httpbin.org/status/200')
print(f"Status: {response.status_code}")

"""
EXPECTED OUTPUT is as follows:
if the site is accessible then the output will come as follows:
Status: 200

if the site is not accessible then the output will come as follows:
Status: 503
"""
