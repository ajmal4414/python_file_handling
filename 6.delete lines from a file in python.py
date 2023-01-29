with open('samplefile.txt','r') as fp:
    lines=fp.readlines()
with open('samplefile.txt','w') as fp:
    for line in lines:
        if line.strip("\n")!="hello":
            fp.write(line)
