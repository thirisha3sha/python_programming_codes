#Python program to count the number n in a given list.
def find(num,n):
    count=0
    for i in num:
        if(i==n):
            count+=1
    return count
num=list(map(int,input("enter numbers:").split()))
n=int(input("enter the number to count:"))
print(find(num,n))
