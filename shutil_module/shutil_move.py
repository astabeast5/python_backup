import os
import shutil

os.makedirs('documents',exist_ok=True)
with open('report.txt', 'w') as f:
    f.write("This is a Report Data")

print("Before moving")

print(f"Current folder: {os.getcwd()}")

print(f"Listing Files {os.listdir('.')}")

print(f"Document Folder: {os.listdir('documents')}")

# Moving file to documents folder
shutil.move('report.txt', 'documents/')

print("\n After Moving")

print(f"Listing Files {os.listdir('.')}")

print(f"Document Folder: {os.listdir('documents')}")

"""
EXPECTED OUTPUT is as follows:
Before moving
Current folder: shutil_module/
Listing Files ['shutil_move.py', 'documents', 'report.txt',]
Document Folder: []

 After Moving
Listing Files ['shutil_move.py', 'documents']
Document Folder: ['report.txt']
"""
