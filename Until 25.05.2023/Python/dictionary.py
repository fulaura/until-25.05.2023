d1=dict()
print(type(d1))

d2={}
print(type(d2))


d1=dict(Ayan="manager", Maksat="worker")
print(d1)

d1={"Kazakhstan":"Astana","USA":"Washington"}
d1["Japan"]="Tokyo"
print(d1)

#del a dict

d2={ "A1":"123", "A2":"456"}
del d2["A1"]
print(d2)

#working with a dict
d2= {"A1":"123", "A2":"123454321"}
if "A1" in d2:
    True


#Dict methods
#a.clear()
#a.get()
d2= {"A1":"123", "A2":"123454321"}
print(d2)
print(d2.get("A1"))
print(d2.clear())

#keys
d2= {"A1":"123", "A2":"123454321"}
print(d2.keys())

#Update
#a.update({key:value})
d2= {"A1":"123", "A2":"123454321"}
d2.update({"A1":"1234", "A3":"haahahahahah"})
print(d2)
