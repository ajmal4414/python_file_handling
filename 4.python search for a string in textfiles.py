word='hello'
with open(r'C:\Users\dell\PycharmProjects\filehandling\samplefile.txt') as fp:
    lines=fp.readlines()
    for line in lines:
        if line.find(word)!=-1:
            print(word,'string exists in file')
            print('line number:',lines.index(line))
            print('line:',line)