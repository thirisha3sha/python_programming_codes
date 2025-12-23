#Python program to calculate the sum of three given numbers. If the values are equal, return three times their sum.
def action(n1,n2,n3):
    sum=n1+n2+n3
    if(n1==n2==n3):
        sum=sum*3
    return sum
n1=int(input("enter the num1:"))
n2=int(input("enter the num2:"))
n3=int(input("enter the num3;"))
print(action(n1,n2,n3))

             
