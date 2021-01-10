n=int(input("Enter a Number: "))
temp=n
sum=0

while (n > 0) :
    remainder = n % 10
    sum = sum * 10 + remainder
    n = n // 10


if (temp == sum) :
    print(temp,"is a Palindrome number")
else :
    print(temp,"is not a Palindrome number")         