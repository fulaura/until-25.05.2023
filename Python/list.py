a= [5,4,6,7]

#search element in a list by using loop
'''
for i in a:
    if i == 4:
        print ("aaaa")'''


#search by using "in"
'''
if (4 in a):
    print('aaaaa')'''

'''a=set(a)
if 4 in a:
    print('aaa')'''

'''a.append(10)

a.insert(3,1)
#3= position   1=value

#delete
a.pop(0)

print(a)'''

#the difference between append() and extend()

'''
a=[1]
b=[1]
a.append(1)
a.append(4)
print(a)
b.extend([1,5,4,5,6,4,])
print(b) '''

#how to swap elements
'''x,y=21,25
print(x,y)
x,y=y,x
print(x,y)'''

#in the list

'''a=[4,5,6,7,8]
print(a)
a[1],a[2]=a[2],a[1]
print(a)'''

#remove elements in the list

a=["Red","Blue","Black","Green","White"]
print(a)
a=a.pop(3)
print("{0} was removed".format(a))
