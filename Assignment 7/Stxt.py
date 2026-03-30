#Write To File
file=open("myfile.txt","w") 
file.write("Hello students")
file.close()
#Append To File
file=open("myfile.txt","a") 
file.write("\n Welcome to python")
file.close()
#Read TO File
file=open("myfile.txt","r") 
data=file.read()
print(data)
file.close()