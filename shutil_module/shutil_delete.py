import os 
import shutil

# Create a test folder with files
os.makedirs('temp_folder/subfolder',exist_ok=True)
with open('temp_folder/file1.txt','w') as f:
    f.write('test')

with open('temp_folder/subfolder/file2.txt','w') as f:
    f.write('test2')

print("Before deleting: ")

print(f"Folders: {[d for d in os.listdir('.') if os.path.isdir(d)]}")

# Delete entire folder and everything inside
shutil.rmtree('temp_folder')

print("After deleting")

print(f"Folders: {[d for d in os.listdir('.') if os.path.isdir(d)]}")

print("temp_folder has been removed completely")

"""
EXPECTED OUTPUT is as follows: 
Before deleting: 
Folders: ['temp_folder']
After deleting
Folders: []
temp_folder has been removed completely
"""
