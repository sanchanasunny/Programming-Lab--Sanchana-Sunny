#Accept a file name from user and print extension of that.
file= input("Enter filename : ")
f=file.split(".")
print("Extension of the file is : " + f[-1])