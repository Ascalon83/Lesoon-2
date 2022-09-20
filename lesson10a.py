n = int(input("введите свой возраст"))
if 10<n< 21:
    print("мне",n,"лет")
elif 2<=n<=4 or 22<=n<=24 or 32<=n<=34 or 42<=n<=44 or 52<=n<=54 or 62<=n<=64 or 72<=n<=74 or 82<=n<=82 or 92<=n<=94:
    print("мне",n,"года")
elif n==1 or n==21 or n==31 or n==41 or n==51 or n==61 or n==71 or n==81 or n==91:
    print("мне",n,"год")
else:
    print("мне",n,"лет")
