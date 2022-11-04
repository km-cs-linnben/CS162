
def is_year_leap(year):
    if year %4 != 0:
        return False
    elif year %100 != 0:
        return True
    elif year %400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    days = [31, 28, 31, 30, 30, 31, 30, 31, 30, 31, 30, 31]
    if is_year_leap(year):
        if month == 2:
            return 29

    return days[month - 1]

def day_of_year(year, month, day):
    #Validate
    if day > 31 or day < 1:
        return none
    if month > 12 or month < 1:
        return none
        
    tdays = day
    month = month - 1
    while month > 0:
        tdays += days_in_month(year,month)
        month -= 1
    return tdays

print(day_of_year(2000, 12, 31))
