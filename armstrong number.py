n=int(input("enter a number:"))
num_digits=len(str(n))
sum_of_digits=0
temp=n
while temp>0:
     digit=temp%10
     sum_of_digits +=digit**num_digits
     temp//=10
if n==sum_of_digits:
    print(f"{n} is armstrong number")
else:
    print(f"{n} is not a armstrong number")
#method2
def armstrong(n):
    num_digits = len(str(n))
    sum_of_digits = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        sum_of_digits += digit ** num_digits
        temp //= 10
    return sum_of_digits==n
def main():
    try:
        n=int(input("enter a number:"))
        if n<0:
            print("please enter a positive integer")
        else:
            if armstrong(n):
                print(f"{n} is armstrong num")
            else:
                print(f"{n} is not a armstrong num")
    except ValueError as ve:
        print(f"error occured {ve}")
if __name__=="__main__":
    main()