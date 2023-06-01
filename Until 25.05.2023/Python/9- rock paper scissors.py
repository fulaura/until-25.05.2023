import random


a=random.randint(1,3)
b=int(input("1-3"))


while b>3 or b<1:
    b=int(input("1-3"))
if a>b or a==1 and b==3:

    print("you lost")

elif a==b:
        
    print("draw")

else:
        
    print("you win")


if a==1:
    a="scissors"
elif a==2:
    a="rock"
else:
    a="paper"
if b==1:
    b="scissors"
elif b==2:
    b="rock"
else:
    b="paper"
print("opponent chose",a)
print("your choice is",b)
