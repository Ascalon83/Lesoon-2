y1=int(input("введите год рождения1 "))
y2=int(input("введите год рождения2 "))
m1=int(input("введите месяц рождения1 "))
m2=int(input("введите месяц рождения2 "))
d1=int(input("введите день рождения1 "))
d2=int(input("введите день рождения2 "))
if y1<y2:
    print("пользователь 1 страше")
elif y1==y2 and m1<m2:
    print("пользователь 1 страше")
elif y1==y2 and m1==m2 and d1<d2:
    print("пользователь 1 страше")
elif y1==y2 and m1==m2 and d1==d2:
    print("ровесники")
else:
    print("старше пользователь 2")
