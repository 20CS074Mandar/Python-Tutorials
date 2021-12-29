#arithmetic operators
x=2
y=3
print(x+y)
print(x*y)
#assignment operator
x=x+2
print(x)
x+=2
print(x)
x,y=10,7
print(x,y)
#unary Operator 
n=7
print(n)
n=-n
print(n)

#Relational operators
ans=(x>y)
print(ans)
ans=(x==y)
print(ans)
ans=(x>=y)
print(ans)
ans=(x!=y)
print(ans)

#Logical Operators
a=5
b=10
print(a<9 and b<11)
print(a<10 and b<2)
print(a<10 or b<2)
x=True
print(x)
x=not x
print(x)

#conversion funtions
print("\n",bin(25))
print(oct(25))
print(hex(25))

#Bitwise Operators
"""->Complement
   ->"""
a=12
print(~a)
print(12&13)
print(12|13)
print(12^13)
print(10<<2)#left shift
print(10>>2)#right Shift

#Membership Operators
list=[1,3,2,23,53,6,8]
print(22 not in list)
print(2 in list)
