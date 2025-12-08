import requests
import json

def get_github_user(username):
    url = f"https://api.github.com/users/{username}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            user_data = response.json()  # Parse JSON
            print(f"User {user_data['name']}")
            print(f"Repos: {user_data['public_repos']}")
            print(f"Followers: {user_data['followers']}")
        else:
            print(f" User not found {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")


# Test with the real Github 
users = ['torvalds','gvanrossum','astabeast5']

for user in users:
    print(f"\n Checking {user}")
    get_github_user(user)


"""
EXPECTED OUTPUT is as follows:

 Checking torvalds
User Linus Torvalds
Repos: 9
Followers: 263511

 Checking gvanrossum
User Guido van Rossum
Repos: 27
Followers: 25302

 Checking astabeast5
User ASEA5
Repos: 5
Followers: 0

"""

