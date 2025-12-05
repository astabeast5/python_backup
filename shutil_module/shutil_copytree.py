import os 
import shutil

os.makedirs('my_project/src', exist_ok=True)
os.makedirs('my_project/docs', exist_ok=True)

with open("my_project/README.md", 'w') as f:
    f.write("# My Project")

with open("my_project/src/main.py", 'w') as f:
    f.write("print('Hello World!')")

print(" Sample Project created")

shutil.copytree("my_project", "my_project_backup")

print("Backup Created")

print("Contents of backup: ")
for item in os.listdir("my_project_backup"):
    print(f" --- {item}")


"""
EXPECTED OUTPUT is as follows:
 Sample Project created
Backup Created
Contents of backup: 
 --- README.md
 --- src
 --- docs

 

"""
