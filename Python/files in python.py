#f=open ('test.txt')
# or you can type f=open("C:/.../.../test.txt")

# "r" read
# "W" open file for writing, creates new if file does not exist
# "x" Open file for exclusive creation, if the file already exists operation fails
# "a" append
# "t" open in text mode
# "b" open i nbinary mode
# "+" open file for updating (reading and writing)

#f=open('test.txt',"a")
#f=open('test.txt', mode='r',encoding='utf-8')

f=open('test.txt','r')
print(f.read())
f.close()
