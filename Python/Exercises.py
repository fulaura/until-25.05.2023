# #1
'''a=input("enter your name")
print("Hello {a},nice to meet you".format(a= a))

a=input("enter your name")
print("Hello {},nice to meet you".format(a))'''

# #2
#write program that will read the string and prints each letter doubled
#input: info    #output: iinnffoo
'''a=input('write any word:')
b=""

for i in range(len(a)):
    b=b+(2*a[i])
    
print(b)'''

# #3
'''a=input("input any word")
print(a[:((len(a)+1)//2)])'''

# #4
#Write the program that will read two equal length strings
# and prints merged product of that string
#input: abcde       output:Afbgchdkel
#       fghkl
'''a=input("enter char for a,length should be equal")
b=input("enter char for b,length should be equal")
c=""
while len(a)!=len(b):
    a=input("enter char for a again,length should be equal")
    b=input("enter char for b again, length should be equal")
for i in range (len(a)):
    c=c+a[i]
    c=c+b[i]
print(c)'''

# #5 Write the program that will read two string and 
# print them in this form short+long+short
#input: azhe       output:ataazheata
#       ata
'''a=input("type anything")
b=input("type anything")
print('we will do(short+long+short)')
if len(a)>len(b):
    print(b+a+b)
else:
    print(a+b+a)'''
    
# #6 Write the program that will read a string and print 
# the number of "hi" inside that string
#input: hihihello       output:2
'''a=input("type anything")

print("there is/are {} 'hi's".format(a.count("hi")))'''

# #7 Complete the code below so that check_string function will 
# check if string contain a letter Y,if it contains return true
#def check_string(s):
#.
#.
#.
#s=input()
#print(check_string(s))
#input:Yellow       output:True
'''def check_string(s):
    s.lower()
    if s.count("y")>0:
        return True
    else:
        return False
s=input()
print(check_string(s))'''

# #8 What is the output of this following code?
#s="Leaders are solving problem!"
#for letter in s:
#    if letter=="a":
#        print("@",end="")
#    else:
#        print(letter,end="")
#    print("-",end="")
#solve then check!

# #9 What is the output of the following code?
#s="Astana city"
#for i in s:
#    for j in s:
#        print(i,j,i,j)
#solve then check!

# #10 Given the number N. Write a program to generate and 
# prints a dictionary that contains (i,i*i) between 1 
# and N (both included)
#input:8       output:{1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64}
'''n=int(input("enter the number of dicts"))
a={}
for i in range(1,n+1):
    a.update({i:i*i})
print(a)'''

