"""
Create a smart backup script that:
1. Checks if you have enough free space (at least 1GB)
2. Only creates backup if there's space
3. Uses timestamp in backup name
"""

import os
import shutil
import datetime

# Checking the space first
usage = shutil.disk_usage(".")
free_gb = usage.free / (1024**3)

if free_gb > 1:
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    shutil.copytree(".", f"backup_{timestamp}")
    print(f"Backup Created successfully backup_{timestamp}")
else:
    print("Not enough space for backup")

"""
EXPECTED OUTPUT is as follows:
Backup Created successfully backup_20251205_153922
"""
