#Python program to calculate the difference between a given number and 17. If the number is greater than 17, return twice the absolute difference.
def diff(n1,n2):
    if(n1<=n2):
        return n2-n1
    else:
        return (n1-n2)*2
n1=int(input("enter the num1:"))
n2=int(input("enter the num2:"))
print(diff(n1,n2))
