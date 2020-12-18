def iseven(n):
    if n == 0:
        print("Enter a non-zero number")

    if n > -1:
        if n%2==0:
            print("It is an Even Number")
        else:
            print("It is an Odd Number")    

n=-1

while n == -1:
    inputfromuser = input("Enter a number")
    try:
        n = abs(int(inputfromuser))
    except:
        print('Input should be a number')

iseven(n)


