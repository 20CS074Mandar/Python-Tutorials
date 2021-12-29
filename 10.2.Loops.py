from typing import ItemsView


x=['Mandar',65,2.5]
for i in x:
        print(i)

x="MANDAR"
for i in x:
        print(i)

print()
for i in range(1,40):
        print(i,end=" ")
for i  in range(40,0,-1):
        print(i,end=" ")

print("\n")
#print numbers from 1 to 100 skipping divisible of 3 and 5
for i in range (1,101):
        if i%3==0 or i%5==0 :
                continue
        print(i,end=" ")




print()

list1=['Brahma','Vishnu','Mahesh']
for god in list1:
        print(god)
list1=[["Brahma",1],["Vishnu",2],["Mahesh",3]]
for god in list1:
        print(god)
for god,lok in list1:
        print(god,lok)

dict1=dict(list1)
print(dict1)

for god,lok in dict1.items():
        print(god,lok)

items=[int,float,"Lord",5,3,6,7,2,5,64,35,3,2,5,18,8]
for item in items:
        if str(item).isnumeric() and item>6:
                print(item,end=" ")