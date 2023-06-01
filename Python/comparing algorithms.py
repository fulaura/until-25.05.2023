arr=[2,4,-3,5,2,-5,2]
best=0
n=len(arr)
for a in range(n):
    for b in range(n):
        s=0
        for k in range(a,b):
            s+=arr[k]
    best=max(best,s)
print(best)