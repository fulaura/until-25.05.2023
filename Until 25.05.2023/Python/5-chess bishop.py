'''x=input().split()
y=input().split()

a=['a','b','c','d','e','f','g','h']


if x[0] != a[0] or x[0]!=a[1] or x[0]!=a[2] or x[0]!=a[3] or x[0]!=a[4] or x[0]!=a[5] or x[0]!=a[6] or x[0]!=a[7]:
    print('error')
if x[1] != 1 or x[1]!=2 or x[1]!=3 or x[1]!=4 or x[1]!=5 or x[1]!=6 or x[1]!=7 or x[1]!=8:
    print('error')
else:
    print('good')'''


x=int(input('a-h in num'))
while x>8 or x<1:
    x=int(input('a-h in num'))
    
y=int(input('num coordinates'))
while y>8 or y<1:
    y=int(input('num coordinates'))

c=1
d=0
p=[]
q=[]
while (x<8 and x>0) or (y<8 and y>0):
    d +=2
    x=x+c
    y=y+c
    p.append(x)
    q.append(y)
    print(x,y)
    c +=2
    x=x-d
    y=y-d
    p.append(x)
    q.append(y)
    print(x,y)
    
    if x+c>8 or y+c>8 or x-d<0 or y-d<0:
        break
if x+c>0 or y+c>0 and x-d>0 or y-d>0:
    while x>0 or y>0:
        x=x-1
        y=y-1
        p.append(x)
        q.append(y)
        print(x,y)
        if x-1<1 or y-1<1:
            break
print(p)
print(q)
'''   if x+c>8 or y+c>8 or x-d<0 or y-d<0:
        if x+c>0 or y+c>0 and x-d>0 or y-d>0:
            while x-d>0 or y-d >0:
                x=x-1
                y=y-1
                print(x,y)

    if x+c>8 or x-d<0 and y+c>8 or y-d<0:
        break'''

