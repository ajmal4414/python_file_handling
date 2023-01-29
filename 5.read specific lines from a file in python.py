with open(r'C:\Users\dell\PycharmProjects\filehandling\samplefile.txt')as fp:
    line_numbers=[1,2]
    lines=[]
    for i, line in enumerate(fp):
        if i in line_numbers:
            lines.append(line.strip())
        elif i>5:
            break
print(lines)
