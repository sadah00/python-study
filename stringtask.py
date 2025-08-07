my_name="JOHn"
clean_name=my_name.lower()
print(clean_name)

text="The Dog Breed is German Shepherd"
result1=text[8:23]
print(result1)

text="Defeat for the Clinton forces,this was her moment of truimph"
start=text.find("Clinton")
end=text.find("forces")+len("forces")
result=text[start:end]
print(result)

text="The lazy dog,ran so fast;it hit the wall."
parts=text.split(";")
print(parts)
print(len(parts))

first_name="John"
second_name="Do,e"
first_name=first_name.strip()
second_name=second_name.replace(",","").replace("","").strip()
second_name=second_name.replace("Do e","Doe")
full_name=first_name+" "+second_name
print(full_name)

r= '["E","W","C"]'
r=r.replace('[','')
r=r.replace('"','')
r=r.replace(',','')
r=r.replace(']','')
print(r)


