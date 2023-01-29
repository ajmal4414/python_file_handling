import os
myfile=('C:\Users\dell\path\New folder')
if os.path.isfile(myfile):
    os.remove(myfile)
else:
    print("error %s file not found"%myfile)