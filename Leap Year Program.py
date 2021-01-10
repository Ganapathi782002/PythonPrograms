n=int(input("Enter a Year: "))
if n%400 == 0:
    print(n,"is a leap year")
elif n%100 == 0:
    print(n,"is not a leap year")
elif n%4 == 0:
    print(n,"is a leap year")
else:
    print(n,"is not a leap year")            