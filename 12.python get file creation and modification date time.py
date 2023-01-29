import datetime
import os
path=(r'C:\Users\dell\PycharmProjects\filehandling\samplefile.txt')
modfy_time=os.path.getmtime(path)
date_modify=datetime.datetime.fromtimestamp(modfy_time)
print('modified on',date_modify)
current_time=os.path.getctime(path)
date_create=datetime.datetime.fromtimestamp(current_time)
print('created on',date_create)
