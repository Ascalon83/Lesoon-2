years=int(input("введите год рождения "))
month=int(input("введите месяц рождения "))
day=int(input("введите день рождения "))
years_n=int(input("введите текущий год "))
month_n=int(input("введите текущий месяц "))
day_n=int(input("введите текущий день "))
age_y=years_n-years # полных лет
if month_n>month:
    print(age_y)
elif month_n==month and day_n>=day:
    print(age_y)
else:
    print(age_y-1)



