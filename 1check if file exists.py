import os.path

file_path=r'C:\Users\dell\PycharmProjects\filehandling\samplefile.txt'
flag=os.path.isfile(file_path)
if flag:
    print(f"the file {file_path} exists")
else:
    print(f"the file{file_path}doesnot exist")