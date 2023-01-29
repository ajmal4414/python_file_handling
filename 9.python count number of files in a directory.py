import os
count=0
filepath=os.listdir(r'C:\Users\dell\path')
for path in os.listdir(r'C:\Users\dell\path'):
    if os.path.isfile(r'C:\Users\dell\path'):
        count+=1
print('file count is' ,count)