import os

# Parent directory Creation 
os.makedirs('log', exist_ok=True)

# Checking the log folder esistance 
if os.path.exists('log'):
    print('log folder exist')
else:
    print("creating log folder")
    os.makedirs('log')

# Creating subfolders
os.makedirs('log/error',exist_ok=True)
os.makedirs('log/debug',exist_ok=True)
os.makedirs('log/info',exist_ok=True)

def count_files_in_folder(folder_path):
    if os.path.exists(folder_path):
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        return len(files)
    return 0

# Display the log structure
print(f"LOG FOLDER {count_files_in_folder('log')}")

print("Log Directory Structure:")
print(f"├── log/ ({count_files_in_folder('log')} files)")
print(f"    ├── error/ ({count_files_in_folder('log/error')} files)")
print(f"    ├── debug/ ({count_files_in_folder('log/debug')} files)")
print(f"    └── info/ ({count_files_in_folder('log/info')} files)")
