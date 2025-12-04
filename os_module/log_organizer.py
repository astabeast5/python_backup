import os

# Parent Folder Log creation
os.makedirs('log',exist_ok=True)

# Checking the log folder existance
if os.path.exists('log'):
    print('log folder already exists')
else:
    print("Creating log Folder")
    os.makedirs('log')

# Creating subfolders
os.makedirs('log/error',exist_ok=True)
os.makedirs('log/info',exist_ok=True)
os.makedirs('log/debug', exist_ok=True)

print(f"{os.listdir('log')}")

for folder in ['error','info','debug']:
    folder_path = f'log/{folder}'
    file_count = len(os.listdir(folder_path))
    print(f"{folder} folder has {file_count} files")
