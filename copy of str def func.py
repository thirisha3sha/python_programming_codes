#Python program that returns a string that is n (non-negative integer) copies of a given string.
def copy(text,n):
    result=" "
    for i in range(n):
        result=result+" "+text
    return result
text=str(input("enter the text:"))
n=int(input("enter the number of copies:"))
print(copy(text,n))
