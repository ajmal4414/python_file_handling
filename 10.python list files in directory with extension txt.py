import os
res=[]
for root,directory,files in os.walk(r'C:\Users\dell\path'):
    for file in files:
        if file.endswith('.txt'):
            res.append(os.path.join(root,file))
print(res)
