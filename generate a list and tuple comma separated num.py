#generating a list and a tuple of user input
def conversion_list_tuple(a):
    conversion_list=list(a)
    conversion_tuple=tuple(conversion_list)
    print("LIST:", conversion_list)
    print("Tuple:",conversion_tuple)
while True:
    try:
        size = int(input("Enter the size of the list and tuple:"))
        if size<=0:
            print("Invalid input.Please enter the valid size")
        else:
            break
    except ValueError:
        print("Invalid input.Please enter the integer input")
a=[]
for i in range(size):
    while True:
        try:
            values = input("enter the elements:")
            a.append(values)
            break
        except ValueError:
            print("Invalid input.Please enter the valid input")
result=conversion_list_tuple(a)

#method 2
values=input("enter the elements:")
list1=values.split(",")
tuple=tuple(list1)
print("list:",list1)
print("tuple:",tuple)