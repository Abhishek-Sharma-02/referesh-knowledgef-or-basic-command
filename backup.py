import shutil
import datetime
import os


def backup_file(source, destination):
    today= datetime.date.today()
    #Below 2 line and next 2 line after that, except we have used tar.gz name and replacing them in next line
    # Both condition are correct and work as expected    
    #backup_file_name = os.path.join(destination, f"backup_{today}.tar.gz") 
    #shutil.make_archive(backup_file_name.replace(".tar.gz",''),'gztar', source)
    backup_file_name = os.path.join(destination, f"backup-{today}")
    shutil.make_archive(backup_file_name,'gztar', source)

source=r"D:\Python practice\practice"
destination=r"D:\Python practice\practice\backup"
backup_file(source,destination)
