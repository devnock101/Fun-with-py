# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
    if year % 4 == 0:
        if  year % 100 != 0 or year % 400 == 0:
            return True
    return False

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = 0
    years = y2 - 1
    days_in_years = 0
    while years >= y1:
        if isLeapYear(years):
            days_in_years += 366
        else:
            days_in_years += 365
        years -= 1
    days += days_in_years
    months_to_add = m2 - 1
    days_in_month_to_add = 0
    for month in daysOfMonths[:months_to_add]:
        days_in_month_to_add += month
    days += days_in_month_to_add
    days += d2 - d1
    months_not_to_add = m1 - 1
    days_in_month_not_to_add = 0
    for month in daysOfMonths[:months_not_to_add]:
        days_in_month_not_to_add += month
    days -= days_in_month_not_to_add
    if days >= 0:
        return days
    return 'undefined'

print(daysBetweenDates(1900,1,1,1999,12,31))