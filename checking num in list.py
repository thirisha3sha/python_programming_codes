#Write a Python pr3ogram that checks whether a specified value is contained within a group of values.

'''Test Data:
3 -> [1, 5, 8, 3] : True
-1 -> [1, 5, 8, 3] : False'''
def check(list1,num):
    for i in list1:
        if num==i:
            return True
    return False
n=int(input("enter the number to check in list:"))
list1=list(map(int,input("enter the elements in list:").split()))
print(check(list1,n))
