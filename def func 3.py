#Python program to get a newly-generated string from a given string where "Is" has been added to the front. Return the string unchanged if the given string already begins with "Is".
def txt(a):
    if ((len(a)>=2) and (a[:2]=="IS")):
        return a
    else:
        return "IS" +a
a=str(input("enter the text:"))
print(txt(a))
