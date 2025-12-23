#Python program to test whether a passed letter is a vowel or not.
def vowel(character):
    vowels="aeiouAEIOU"
    return character in vowels
a=input("enter a alphabet:")
if(len(a)==1):
    print(vowel(a))
else:
    print("enter a single character")
