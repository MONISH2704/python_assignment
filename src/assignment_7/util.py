import calendar

def find(month, date, year):
    day=calendar.weekday(year, month, date)
    result=calendar.day_name[day]
    return result