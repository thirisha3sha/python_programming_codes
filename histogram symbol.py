#Write a Python program to create a histogram from a given list of integers.
def histogram(items,symbol):
    for i in items:
        hist=""
        while i>0:
            hist+=symbol
            i=i-1
        print(hist)
symbol=str(input("enter the symbol for histogram:"))
items=list(map(int,input("enter the  data values:").split()))
histogram(items,symbol)
