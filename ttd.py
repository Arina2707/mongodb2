import datetime

date_entry = input('Enter a date (i.e. 2017,7,1)')
year, month, day = map(int, date_entry.split(','))
date = datetime.datetime(year, month, day)

print(date)