import os
os.makedirs('documents',exist_ok=True)

os.makedirs('images',exist_ok=True)

os.makedirs('scripts',exist_ok=True)

print(f"Document Folder: {os.listdir('documents')}")

print(f"Images Folder: {os.listdir('images')}")

print(f"Scripts Folder: {os.listdir('scripts')}")

# How to check if folder has files or not ?
if len(os.listdir('documents')) > 0:
    print("Document folder has files! ")
else:
    print("Document folder is empty")
