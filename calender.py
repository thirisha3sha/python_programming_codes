#Python program that prints the calendar for a given month and year.
import calendar
year=int(input("enter the year:"))
month=int(input("enter the month:"))
print(calendar.month(year,month))
