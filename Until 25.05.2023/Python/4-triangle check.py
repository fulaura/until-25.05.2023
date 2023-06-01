a=int(input("side length 1"))
b=int(input("side length 2"))
c=int(input("side length 3"))
if (a**2)+(b**2)==(c**2) or (a**2)+(c**2)==(b**2) or (b**2)+(c**2)==(a**2):
    print("true")
else:
    print("false")
