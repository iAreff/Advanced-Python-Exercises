from datetime import date
from khayyam import JalaliDate


input_date = input("Enter Date (Example: 1399-06-20): ")
year, month, day = input_date.split('-')

jalali_date = JalaliDate(year,month,day)
gregorian_date = jalali_date.todate()

print(gregorian_date)
print(jalali_date)
print('Days difference from today:',(date.today()-gregorian_date).days)