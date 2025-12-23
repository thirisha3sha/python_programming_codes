#simple calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        return "error!division by zero"
def get_input():
    while True:
        try:
            a=float(input("enter a num1:"))
            b=float(input("enter a num2:"))
            return a,b
        except ValueError:
            print("Invalid input!.PLEASE ENTER  A INTEGER")
def main():
    print("select operation:")
    print("1.Add \n 2.Sub \n 3.Multiply \n 4. Division")
    while True:
        choice=input("enter the choice:")
        if choice in('1','2','3','4'):
            a,b=get_input()
            if choice=='1':
                print(f"{a}+{b}={add(a,b)}")
            elif choice=='2':
                print(f"{a}-{b}={sub(a,b)}")
            elif choice=='3':
                print(f"{a}*{b}={multiply(a,b)}")
            elif choice=='4':
                print(f"{a}/{b}={divide(a,b)}")
            break
        else:
            print("Invalid input!enter the valid choice")
if __name__=="__main__":
    main()

#method 2
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        a = float(input("Enter num1: "))
        b = float(input("Enter num2: "))

        if choice == '1':
            result = a + b
            print(f"{a} + {b} = {result}")
        elif choice == '2':
            result = a - b
            print(f"{a} - {b} = {result}")
        elif choice == '3':
            result = a * b
            print(f"{a} * {b} = {result}")
        elif choice == '4':
            if b != 0:
                result = a / b
                print(f"{a} / {b} = {result}")
            else:
                print("Error! Division by zero")
        break
    else:
        print("Invalid input! Enter a valid choice")
