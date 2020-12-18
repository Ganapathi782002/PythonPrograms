start = int(input('Enter an starting number - '))
end = int(input('Enter an ending number - '))

if end <= start:
    print('End should not be lesser than Start')
else:
    for currentnumber in range(start, end):
        if currentnumber > 1:
            for divisiblenum in range(2, currentnumber):
                if currentnumber % divisiblenum == 0:
                    break
            else:
                print(currentnumber)
