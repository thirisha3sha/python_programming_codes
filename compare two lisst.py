#comparing two list
def compare_lists(list1, list2):
    if list1 == list2:
        return True
    else:
        return False
n1=int(input("entern the size of list1:"))
n2=int(input("enter the size of list2:"))
print("enter elements for list1:")
for i in range(n1):
    list1=list(map(int,input().split()))
print("enter elements for list2:")
for i in range(n2):
    list2=list(map(int,input().split()))
if compare_lists(list1, list2):
    print("Lists are equal")
else:
    print("Lists are not equal")
"""
#method2
def compare_list(list1,list2):
    return sorted(list1)==sorted(list2)
n1=int(input("enter the size of list1:"))
n2=int(input("enter the size of list2:"))
l1=[]
l2=[]
print("enter elements for list1:")
for i in range(n1):
    elements1=int(input(f"enter element {i+1} for list1:"))
    l1.append(elements1)
print("enter elements for list2:")
for i in range(n2):
    elements2=int(input(f"enter element {i+1} for list2:"))
    l2.append(elements2)
if compare_list(l1, l2):
    print("Lists are equal (ignoring order)")
else:
    print("Lists are not equal (ignoring order)")"""