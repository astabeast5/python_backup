import os

print (f"{os.getcwd()}")

print(f"{os.listdir(os.path.expanduser("~"))}")

os.makedirs('my-practice', exist_ok=True)

print(f"Folder Created")
