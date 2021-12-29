#printing first 50 fibonacci numbers 
from math import sqrt
a=0
b=1
print(a)
print(b)
for i in range(2,50):
        c=a+b
        a=b
        b=c
        print(c,end=" ")

print("\n")
#check wether the entered number is prime or not 
n=int(input("Enter a numebr :- "))
if(n<=1):
        print("Not a prime")

for i in range(2,int(sqrt(n)+1)):
        if(n%i==0):
                print("NOt a prime")
                break