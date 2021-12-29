#Date : 29.12.21


#Unpacking charachters

language='Python'
a,b,*c=language
print(a)
print(b)
print(c)

a,b,*c,d=language
print(a)
print(b)
print(c)
print(d)

a,b,*c,d,e=language
print(a)
print(b)
print(c)
print(d)
print(e)

language='Python'

#format code 
first_name="Bob"
last_name="Marley"
job="Unemployed"
country="India"
sentence="I am {}. I am currently {}. The country i live in is {}.".format(first_name+" "+last_name,job,country)
print(sentence)

#Join method
mystr=['Java ',' Python ',' C++ ']
result='#'.join(mystr)
print(result)

#Lists
fruits=['Bannana','Apple','Orange','Grapes']
print("\nFruits available are :-",fruits)
print("No of fruits are :- ",len(fruits))
#accesing items using index
print(fruits[0])
print(fruits[1])
print(fruits[3])
print(fruits[-1])

#unpacking list items 
first,second,*rest=fruits
print(first)
print(second)
print(rest)
print(fruits[::2])
print()