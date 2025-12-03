import os
import datetime
#

command = "uptime"
command = "date"
"""
#def check_cpu(command): # defining the function
#    print(os.system(command))
"""

def run_command(command):
    return os.system(command)

def show_date():
    return datetime.datetime.today()

today= show_date()
print(today)
print(today.strftime("%Y-%m-%d %H:%M"))