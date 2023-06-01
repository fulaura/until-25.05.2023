print("admission to take exam")
a=int(input("number of classes held"))
b=int(input("number of classes attended"))
d=a*b/100
e="y"
f="n"
while d>1 or d<0:
        a=int(input("number of classes held"))
        b=int(input("number of classes attended"))
  
    
if d>0.75 and d<=1:
    print("you are allowed")

if d<0.75 and d>=0:
    c=input("was ill? y/n")
    if not c ==e or not c ==f:
        print("error, please type vailid char")
    if c=="y":
        print("we give our permissions")
    if c=="n":
        print('sorry, no')
