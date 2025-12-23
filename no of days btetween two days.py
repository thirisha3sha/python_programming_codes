#Python program to calculate the number of days between two datesf
from datetime import date
year1,month1,date1=map(int,input("enter the day1(yyyy,mm,dd):").split())
year2,month2,date2=map(int,input("enter the day2(yyyy,mm,dd):").split())
day1=date(year1,month1,date1)
day2=date(year2,month2,date2)
difference=(day2-day1).days
print("the number of days betweeen day1",day1,"day2",day2,"is",abs(difference))
