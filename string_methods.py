text="python class"
text_cap=text.capitalize()
print(text_cap)
print(text.count('s'))
text_tit=text.title()
print(text_tit)

print(text.find('c'))
print(text.index('c'))

text_rev=text[::-1]

text=" learn python "
text_str=text.strip()
text_t=text.title()
text2=text.replace(" ","_")

print(text[10:14])

chat="hello"
chat_re=chat[::-1]
print(chat_re)

sent="good habits are hard to break!"
sent1=sent.replace("good","BAD")
print(sent1)

email="  John.Doe@GMAIL.com "
str=email.strip()
rep=str.lower()
print(rep)
print(rep[9:18])

first="john"
first_cap=first.capitalize()
print(first_cap)
last="DOE"
last_cap=last.capitalize()
print(last_cap)
hobby=" Reading Books "
hobby_str=hobby.strip()
print(hobby_str)
chat=f"My name is {first_cap} {last_cap} and I love {hobby_str}."
print(chat)

sente=input('Enter a sentence:')
sente2=sente.split(' ')
print(sente2)
print(len(sente2))

sente_tit=sente.title()
print(sente_tit)

sente_rev=sente[::-1]
print(sente_rev)