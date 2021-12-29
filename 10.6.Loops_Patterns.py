#This file consists of the solution of the patterns of the link given below
# https://www.javainterviewpoint.com/number-pattern-programs-in-java/

#Pattern 1
from os import pipe, terminal_size
from types import SimpleNamespace


print("\n Pattern 1\n")
rows=5
for i in range(1,rows+1):
        for j in range(1,i+1):
                print(j,end=" ")
        print()

#Pattern 4
print("\n Pattern 4\n")
rows =5
for i in range(rows,1,-1):
        for j in range(1,i+1,1):
                print(j,end=" ")
        print()
rows=5
for i in range(1,rows+1):
        for j in range(1,i+1):
                print(j,end=" ")
        print()


#patter 5
print("\nPattern 5\n")
rows=5
for i in range(0,rows+1):
        for j in range(rows-i,0,-1):
                print(j,end=" ")
        print()
for i in range(0,rows+1):
        for j in range(i,0,-1):
                print(j,end=" ")
        print()

#Pattern 6
print("\nPattern 6\n")
rows=5
m=8
for i in range(1,rows+1):
        for j in range(1,m):
                print(end=" ")
        m-=1
        for j in range(1,i+1):
                print(j,end=" ")
        print(" ")

#Pattern 7
print("\nPattern 7\n")
rows=5
for i in range(1,rows+1):
        for j in range(rows,i-1,-1):
                print(j,end=" ")
        print()

#Pattern 8 
print("\nPattern 8\n")
rows=5
for i in range(rows,0,-1):
        for j in range(rows,i-1,-1):
                print(j,end=" ")
        print()

#Pattern 9
print("\nPattern 9\n")
rows=5
for i in range(rows,0,-1):
        for j in range(1,i+1):
                print(j,end=" ")
        print()

#Pattern 10
print("\nPattern 10\n")
k=1
for i in range(0,5):
        for j in range (0,i+1):
                print(k,end=" ")
                k+=1
        print()
print()

#Pattern 11
print("\nPattern 11\n")
rows=5
for i in range(1,rows+1):
        for j in range(i,0,-1):
                print(j,end=" ")
        print()

print()

#Pattern 12
rows=5
print("\nPattern 13\n")
for i in range(1,rows+1):
        temp=i
        for j in range(i,0,-1):
                print(temp,end=" ")
                temp+=5
        print()

print()

#Pattern 13
print("\nPattern 13\n")

#Pattern 14
print("\nPattern 14\n")
rows=5
for i in range(1,rows+1):
        for j in range(1,i+1):
                print(j,end=" ")
        for k in range(i-1,0,-1):
                print(k,end=" ")
        print()

print()

#Pattern 15
print("\nPattern 15\n")
rows=5
m=2*rows-2
for i in range(rows,0,-1):
        for j in range(m,1,-1):
                print(end=" ")
        m+=1
        for k in range(1,i+1):
                print(k,end=" ")
        print()

#Pattern 16
print("\n Pattern 16")
rows=5
m=2*rows-2
for i in range(1,rows+1):
        for j in range(1,m+1):
                print(end=" ")
        m-=1
        for k in range(1,i+1):
                print(k,end=" ")
        print() 


#Pattern 18
print("\nPattern 18\n")
rows=5
for i in range(1,rows+1):
        for j in range(1,i+1):
                print(end=" ")
        for k in range(i,rows+1):
                print(k,end=" ")
        print()

for i in range(rows,0,-1):
        for j in range(1,i+1):
                print(end=" ")
        for k in range(i,rows+1):
                print(k,end=" ")
        print()

#Pattern 19
print("\nPattern 19\n")
rows=5
for i in range(rows,0,-1):
        for k in range(1,i+1):
                print(end=" ")
        for j in range(i,rows+1):
                print(j,end=" ")
        print()

#Pattern 20
print("\nPattern 20\n")
rows=5
#for pattern generation
for i in range(1,rows+1):

        #for space
        for j in range(1,rows+1-i):
                print(' ',end=" ")  
        #for increasing pattern 
        for k in range(1,i+1):
                print(k,end=" ")
        #for decresasing pattern
        for l in range(i-1,0,-1):
                print(l,end=" ")

        print()

#Pattern 21
print("\nPattern 21\n")
rows=5
for i in range(1,rows+1):
        for j in range(1,i+1):
                if(j%2==0):
                        print("0",end=" ")
                else:
                        print("1",end=" ")
        print()


#Pattern 22
print("\nPattern 22\n")
rows=5
for i in range(1,rows+1):
        for j in range(1,i):
                print("0",end=" ")
        print(i,end=" ")
        for k in range(i,rows+1):
                print("0",end=" ")
        print()

#Pattern 23
print("\nPattern 23\n")
rows=5
for i in range(1,rows+1):
        for j in range(rows,i-1,-1):
                print(1,end=" ")
        for k in range (1,i+1):
                print(i,end=" ")
        print()
        
#Pattern 24
print("\nPattern 24\n") 
rows=5
for i in range(1,rows+1):
        for j in range(i,rows+1):
                print(j,end=" ")
        for k in range(rows,i-1,-1):
                print(k,end=" ")
        print()

#Pattern 25
print("\nPattern 25\n")
rows=5
for i in range(1,rows+1):
        for j in range(rows,i-1,-1):
                print(end=" ")
        for k in range(1,i+1):
                print(i,end=" ")
        print()


#Pattern 26
print("\nPattern 26\n")
rows=5 
for i in range(rows,0,-1):
        for k in range(i,rows+1):
                print(k,end=" ")
        for j in range(rows-i,rows):
                print(5,end=" ")
        print()

#Pattern 27
print("\nPattern 27\n")
rows=5
for i in range (1,rows+1):
        temp=i
        for j in range(1,i+1):
                print(temp,end=" ")
                temp=temp+rows-j
        print()


#Pattern 28
print("\nPattern 28\n")
rows=5
for i in range(1,rows/2+1):
        temp=i
        for j in range(1,i+1):
                print(temp,end=" ")
                temp+=i

        print()


#Pattern 29
print("\nPattern 29\n")


#Pattern 30

print("\nPattern 30\n")
