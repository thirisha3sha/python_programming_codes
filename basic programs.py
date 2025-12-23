"""#1.python program that accepts a filename from the user and prints the extension of the file
filename=input("enter the filename with extension:")
filename.split(".",maxsplit=-1)
print("the extension of the input file is ",filename)


#method 2:
filename=input("enter the filename with extension:")
filename.rsplit(sep=".",maxsplit=-1)
print("the extension of the input file is ",filename)"""


"""#2.python program to display the first and last colors from the user input list
colors=int(input("enter the number of colors in the list:"))
color_list=[]
for i in range(colors):
    colornames=input("enter the colorname %i:"%i)
    print()
    color_list.append(colornames)
print("first color in list:",color_list[0])
print("last color in list:",color_list[-1])"""

"""#method 2:
def first_last_color(list):
    first_color=list[0]
    last_color=list[-1]
    return first_color,last_color
while True:
    try:
        size=int(input("enter the size of the color list:"))
        if size<=0:
            print("Invalid input.please enter the valid size!!!")
        else:
            break
    except ValueError:
        print("Invalid input.Please enter the valid input!!!")
list=[]
for i in range(size):
    while True:
        try:
            colornames=input("enter the color names:")
            list.append(colornames)
            break
        except ValueError:
            print("Invalid input.Please enter the valid input")
print("first and last color in the list:",first_last_color(list))"""

"""#3.python program to display the examination schedule(extract the date from exam_st_date
import datetime

def starting_day_exam(exam_dates):
    starting_date = min(exam_dates)
    ending_date = max(exam_dates)
    print("Your exam will start on", starting_date.strftime("%d/%m/%Y"))
    print("Your exam will end on", ending_date.strftime("%d/%m/%Y"))

def valid_date(exam_dates):
    valid_dates = []
    for i in exam_dates:
        try:
            date= datetime.datetime.strptime(i, "%d/%m/%Y")
            valid_dates.append(date)
        except ValueError:
            print(Invalid input. Please enter a valid date!")
            return False
    starting_day_exam(valid_dates)
    return True

while True:
    try:
        size = int(input("Enter the total number of exam days: "))
        if size <= 0:
            print("Invalid input. Please enter a valid size.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid input.")

exam_dates = []
for i in range(size):
    while True:
        date = input(f"Enter the date for exam {i+1} (DD/MM/YYYY): ")
        try:
            datetime.datetime.strptime(date, "%d/%m/%Y")
            exam_dates.append(date)
            break
        except ValueError:
            print("Invalid date format. Please enter the date in DD/MM/YYYY format.")
valid_date(exam_dates)"""
"""# python program that accepts an integer n and computes the value of the series n+nn+nnn:
def series(n,term_in_series):
    series_sum=0
    current_term=0
    for i in range(n):
        current_term=current_term * 10 + term_in_series
        series_sum +=current_term
        print(f"{current_term}",end='   ')
    return series_sum

def main():
    while True:
        try:
            size=int(input("Enter the num of terms in the series:"))
            if size<=0:
                print("Invalid input.Please enter a valid size!!!")
            else:
                terms=int(input("\nenter the term you want in series:"))
                print(f"series of {terms} with {size} terms:")
                result=series(size,terms)
                print(f"\nthe value of the series is:{result}")
                break
        except ValueError:
            print("Invalid Input.Please enter the valid input!!!")
if __name__ == "__main__":
    main()"""
"""#python program to print calender
def main():
        try:
            year=int(input("enter the year:"))
            month=int(input("enter the month:"))
            if(month <=0 or month>12):
                print("Invalid Input.Please enter the valid input!!!")
            else:
                import calendar
                print(f"calender for {year} year and {month}th month:")
                print(calendar.month(year,month))
        except ValueError:
            print("Invalid INput.Please enter the valid input!!!!")
if __name__== "__main__":
    main()"""
"""#guess the word
secret_word="hello"
guess=""
guess_count=0
guess_limit=3
out_of_guess=False
while guess!=secret_word and not(out_of_guess):
    if guess_count<guess_limit:
        guess=input(f"Enter the guessing word(try {guess_count}):")
        guess_count +=1
    else:
        out_of_guess=True
if out_of_guess:
    print("out of guesses!!.YOU LOSE!!")
else:
    print("You won!!!!!!")"""

#

"""#calculating num of days between two dates
def days_in_month(month,leap_year):
    days={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    if month==2 and leap_year:
        days[2]=29
    return days[month]
def main():
        try:
            year1=int(input("enter the first year:"))
            month1=int(input("enter the first month(1-12):"))
            day1=int(input("enter the day2(1-31):"))
            year2 = int(input("enter the second year:"))
            month2 = int(input("enter the second month(1-12):"))
            day2 = int(input("enter the day2(1-31)"))
            if not(1<=month1<=12 and 1<=day1 <= days_in_month(month1,False)):
                print("Invalid first date format.Please enter valid dates.")
                continue
            if not (1 <= month2 <= 12 and 1 <= day2<= days_in_month(month2, False)):
                print("Invalid  second date format.Please enter valid dates.")
                continue
        except ValueError:
            print("Invalid input.Please enter the valid input")
if __name__ =="__main__":
    main()"""