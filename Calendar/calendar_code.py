import calendar

my_calendar = calendar.TextCalendar()
my_calendar.prmonth(2020, 4)

leaps = calendar.leapdays(1900,2020)
print(leaps)

year = int(input("Provide the year: "))
print(calendar.prcal(year))

for i in my_calendar.itermonthdays(2020, 4):
    print(i)

for name in calendar.month_name:
    print(name)

for day in calendar.day_name:
    print(day)