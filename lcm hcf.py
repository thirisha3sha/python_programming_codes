def hcf(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    hcf_value=hcf(a,b)
    return abs(a*b)//hcf_value
def main():
    try:
        n1=int(input("enter the num1:"))
        n2=int(input("enter the num2:"))
        HCF=hcf(n1,n2)
        LCM=lcm(n1,n2)
        print(f"HCF of {n1} and {n2} is {HCF}")
        print(f"LCM of {n1} and {n2} is {LCM}")
    except ValueError as ve:
        print("error occured.{ve}")
if __name__=="__main__":
    main()
'''#method2
def lcm(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while True:
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater+=1
    return lcm
n1=int(input("enter the num1:"))
n2=int(input("enter the num2:"))
print(f"LCM of {n1} and {n2} is {lcm(n1,n2)}")
'''