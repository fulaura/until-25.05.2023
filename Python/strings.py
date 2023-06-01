#string method #1
#default
a="ahahaahahhahahahahhaahaah"
print(a[1:])

print(a[0])

print(a[1:2])

a="ahahahaha"
b="hohohoohoh"
print(a+b)

#capitalize string and lower

a="ahahah"
a_cap=a.capitalize()
print(a_cap)

a="HAHAHAHAHAHAH"
a_lower=a.lower()
print(a_lower)

a="HAHAHAHAHAHAH"
a_upper=a.upper()
print(a_upper)


#startswith 

a='a is a'
print(a.startswith("a is"))
print(a.startswith("a hahahahha"))

#ends with

print(a.endswith("is a"))
print(a.endswith("aahahaah"))

#string find

a="u hahahahahahahah"
print(a.find("u"))
print(a.find("k"))



#string method #2

#string count(
    #count finds substrings in the strings
        #a.count(substring,start=...,end=...)

a="haha, a"
print(a.count("a"))

#string replace
    #a.replace(old,new,count)
    
a="cold, old, bold, weather is cold"
print(a.replace("cold","hot"))
print(a.replace("cold","hot",1))

#strip, means(to remove)

a=" haha orange haha"
print(a.strip("haha e"))