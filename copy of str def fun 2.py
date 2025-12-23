#Python program to get n (non-negative integer) copies of the first 2 characters of a given string. Return n copies of the whole string if the length is less than 2.
def copy(text,n):
    len1=2
    if(len1>len(text)):
        len1=len(text)
    newtext=text[:len1]
    result=""
    for i in range(n):
        result=result+newtext
    return result
text=str(input("enter the string:"))
n=int(input("enter the no of copies:"))
print(copy(text,n))
