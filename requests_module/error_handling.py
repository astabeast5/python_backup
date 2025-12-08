import requests

def  check_service(url):
    try:
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            print(f" {url} --OK")
        else:
            print(f" {url} --Status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f" {url} --Error: {e}")

# Testing multiple endpoints
services = [
    'https://httpbin.org/status/200',
    'https://google.com',
    'https://github.com'
]

print(" Service Health Check ")
for service in services:
    check_service(service)


"""
EXPECTED OUTPUT is as follows:
 Service Health Check 
 https://httpbin.org/status/200 --Status: 503
 https://google.com --OK
 https://github.com --OK

"""
