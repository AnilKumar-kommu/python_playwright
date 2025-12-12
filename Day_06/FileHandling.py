f1=open("file_1.txt","a+")
#print(f1.read())
f1.write("++hello world...")
f1.seek(0)
print(f1.read())
#f1.write("Hello World...")

