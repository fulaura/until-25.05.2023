a=int(input())
b=int(input())
c=int(input())
if a<b:
    if a<c:
        print('a is the smallest')
    if a>c:
        print("c is the smallest")
    if a==c:
        print("a and c are the smallest")
if a>b:
    if c>b:
        print("b is the smallest")
    if c==b:
        print("b and c are the smallest")
if a<c or b<c:
    if a==b:
        print("a and b are the smallest")
if a==b and b==c:
    print('all equal')
