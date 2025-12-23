# Python program that accepts a filename from the user and prints the extension of the file.
file=input("enter the file name:")
extension=file.split(".")
print("extension of the given file is:",extension[-1])
#print("extension of the given file is:"+repr(extension[-1]))
