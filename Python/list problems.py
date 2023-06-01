import random
a=[]
b=int(input("enter how many numbers will be in the list"))
for i in range(0,b):
    
    c=random.randint(0,99)
    a.append(c)
print(a)
print('these are the elements in the list')
d=int(input("enter number"))
print('lets check, has there the chosen number')
if (d in a):
    print("yes")
else:
    print("no")