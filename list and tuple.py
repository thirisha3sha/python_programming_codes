#Python program that accepts a sequence of comma-separated numbers from the user and generates a list and a tuple of those numbers.
a=input("enter values:")
list=a.split(" ")
tuple=tuple(list)
print("list=",list)
print("tuple=",tuple)
