import shutil
import datetime
import os 

def backup_files(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file_name.replace('.tar.gz', ''), 'gztar', source)



source = "path of the files you want to take backup of"

destination = "path where you want to store your compressed backup file"

backup_files(source,destination)
