def fibonacci(n):
    fibo=[0,1]
    while len(fibo)<n:
        fibo.append(fibo[-1]+fibo[-2])
    return fibo[:n]
def get_input():
    while True:
        try:
            n=int(input("Enter the number of terms:"))
            if n<=0:
                print("Please enter positive number")
            else:
                return n
        except ValueError:
            print("Invalid Input! Please enter an integer value")
def main():
    n=get_input()
    series=fibonacci(n)
    print(f"Fibonacci series for {n} terms:{series}")
if __name__=="__main__":
    main()
#methpd 2
print("method 2")
n=int(input("Enter the number of terms:"))
a,b=0,1
count=0
if n<=0:
    print("PLease enter a positive integer")
elif n==1:
    print(f"fibonacci series for {n} term:{a}")
else:
    print(f"fiboancci series {a}",end=" ")
    while count<n:
        c=a+b
        a=b
        b=c
        count+=1
        print(c ,end=" ")