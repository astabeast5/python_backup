import os 
import shutil

# Step 1: Create a simple text file 
with open('my_file.txt','w') as f:
    f.write('Hello World')

print("File created named as my_file.txt")

# Step 2: Copy the file 
shutil.copy('my_file.txt', 'my_file_copy.txt')

print("Copied File")

print(f"Files in directory: {os.listdir('.')}")


print(f"{os.listdir('.')}")

"""
EXPECTED OUTPUT is as follows: 
File created named as my_file.txt
Copied File
Files in directory: ['my_file_copy.txt', 'my_file.txt', 'shutil_practice.py']
['my_file_copy.txt', 'my_file.txt', 'shutil_practice.py']
"""
