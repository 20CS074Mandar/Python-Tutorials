r=1
for r in range(0,5):
        c=1
        for c in range(r):
                print("#",end=" ")
        print()
print()

r=1
for r in range(0,5):
        c=1
        for c in range(5-r):
                print("#",end=" ")
        print()


print()


k=1
for i in range(0,5):
        for j in range (0,i+1):
                print(k,end=" ")
                k+=1
        print()
print()


rows=5
for i in range(0,rows+1):
        for j in range(rows-i,0,-1):
                print(j,end=" ")        
        print()


rows=5
for i in range(1,rows+1):
        j=i
        for j in range(j,rows,1):
                print(j,end=" ")        
        print()