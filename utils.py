import os
import datetime

# Below command will not work in window system but will word with Linux as df -h is a linux command.
# It is just for knowledge purpose to understand the import and library function 
# Here Os is the library and system is the function under that library
# This below example show the utilisation of OS library, same way we can utilise different library
#print(os.system("df -h")) 
print (os.system('systeminfo')) # This command will work, as 'systeminfo' is for window command


