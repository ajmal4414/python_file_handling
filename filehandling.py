#read
file=open("samplefile.txt","r")
print(file.read())

#write
file=open("samplefile.txt","w")
file.write("hello welcome")
file.write("to class")
file.close()

#read
file=open("samplefile.txt","r")
print(file.read())

# append
file=open("samplefile.txt","a")
file.write("hello world")
file.close()

