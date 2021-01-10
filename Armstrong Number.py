number=int(input("Enter a number which you want to check: "))
sum=0
temp=number
while temp>0 :
    remainder = temp%10
    sum = sum + remainder * remainder * remainder
    temp = temp // 10
    

if number == sum :
    print(number,"is an armstrong number")
else :
    print(number,"is not an armstrong number")                