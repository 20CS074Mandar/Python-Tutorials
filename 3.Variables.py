var1="Python Tutorials"
print("\n",var1)
var2=19
var3=10.20

print("\n var1= ",var1," type of var1 : ",type(var1))
print("var2+var3 = ",(var2+var3))
print("\n",type(var3+var2))

#printing mulitple times
print(10*"Hello World\n")
print(10*str(int (var2)+int (var2)))

print("\nEnter a numebr to add it with ten :- ",end="")
num=input()
print("\nAnswer :- ",int(num)+10)


print("\nEnter two numbers to give there arithmetic results :- ")

print("\nEnter the first number :-",end="")
n1=input()

print("\nEnter the Second number :-",end="")
n2=input()

print("\nSum of two numbers :- ",int(n1)+int(n2))
print("\nDifference of two numbers :- ",int(n1)-int(n2))
print("\nProduct of two numbers :- ",int(n1)*int(n2))
print("\nDivision of two numbers :- ",int(n2)/int(n1))


num=5
print("\nid of num :- ",id(num))
name="Maddy"
print("\nid of name :- ",id(name))
a=20 
b=a
print("a= ",a," b= ",b)
print("id of a :- ",id(a))
print("id of b :- ",id(b))
#here a and b both will have same address because in python if two variable have same data they
#both will point to the same box 
print("id of value 20 :- ",id(20))


print("\n\tData Types ")
print("\nTypes of data types in python are :-")
print("None\nNumeric \n\tint\n\tfloat\n\tcomplex\n\tbool \nList\nTuple\nSet\nString\nRange\nDictionary\n")

rng=range(0,10)
print(rng)
lst=list(range(10))
print(lst)
lst=list(range(2,10,2))
print(lst)

#swaping two number in python
a=5
b=6
print(a,b)
a,b=b,a
print(a,b)

#formulae for swapping numbers
a=1
b=2
print(a,b)
a=a+b
b=a-b
a=a-b
print(a,b)