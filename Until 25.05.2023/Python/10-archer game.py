import random

a=random.randint(1,10)
b=int(input("enter where will you locate your sign"))

while b>10 or b<1:
    b=int(input("enter where will you locate your sign"))
if a>b:
    print("opponent missed. opponents arrow gone ahead by",a-b,"meters")
elif b>a:
    print("opponent missed. opponents arrow have",b-a,"meters to reach")
else:
    print("opponent hit")
print(a)
print(b)
