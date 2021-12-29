i=1
while i<=5:
        print("Python ",i)
        i+=1


#print numbers from 1 to 100 skipping divisible of 3 and 5
i=1
while i<=100:
        if(i%3==0 or i%5==0):
                i+=1
        else:
                print(i,end=" ")
                i+=1

print()

#pattern 

r=1
c=1
while r<=4:
        c=1
        while c<=5:
                print("#",end="")
                c+=1
        r+=1
        print()