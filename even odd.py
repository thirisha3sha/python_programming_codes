#Python program that determines whether a given number (accepted from the user) is even or odd, and prints an appropriate message to the user.
num=int(input("enter a number:"))
mod=num%2
if(mod>0):
    print(num,"is odd number")
else:
    print(num,"is even number")
