y=int(input())
if(y%4==0):
    if(y%100==0):
        if(y%400==0):
            print('leap year')
        else:
            print('not a leap year')
    else:
        print('leap year')
else:
    print('not a leap year')
