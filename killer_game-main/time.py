import datetime
import os

now = datetime.datetime.now()
fmt = "%Y-%m-%d %H:%m"

print ("The Date and time are "+ now.strftime(fmt))
os.system("python3 Killer.py")