a=int(input("year"))
b=int(input('month'))

if b==2:
    if a%4==0:
        print('there are 29 days in this month')
    else:
        print('there are only 28 days in this month')
        
if b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12:
    print('there are 31 days in this month')
else:
    print('there are 30 days in this month')
