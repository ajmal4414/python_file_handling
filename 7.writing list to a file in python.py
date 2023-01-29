list=['tom','john','sajin']

with open(r'C:\Users\dell\PycharmProjects\filehandling\samplefile.txt','w')as fp:
    for item in list:
        fp.write('%s\n'% item)
        print(fp)
    print('done')