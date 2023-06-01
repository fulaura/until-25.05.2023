a=[5,4,8,7,4,6,5,4,1,5,2,0]

'''print("unsorted",a)
a.sort()
print('sorted',a)
a.sort(reverse=True)
print('descending order',a)'''

#alternative
n=len(a)
for i in range (n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(sorted,a)