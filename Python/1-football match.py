a=int(input("number of matches"))
x=[]

for b in range(a):
    b=int(input("team a's acores"))
    x.append(b)
    
v=[]
for d in range(a):
    d=int(input("team b's acores"))
    v.append(d)
k=0
m=0
m=m+x[k]

while k<a:
    k +=1
    m=m+x[k]

    if a-1==k:
        break
k=0
z=0
z=z+v[k]
while k<a:
    k +=1
    z=z+v[k]

    if a-1==k:
        break

if m>z:
    print('team 1 wins')
elif m==z:
    print("draw")
else:
    print("team 2 wins")


