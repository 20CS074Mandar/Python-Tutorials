nums=[25,12,36,95,14]
print(nums)
print("nums[0] ",nums[0])
print("nums[2:] ",nums[2:] )

values=[9.5,"Maddy",25]
print("\nValues :- ",values)

combo=[nums,values]
print("Combination of both :- ",combo,"\n")

#Lists are Mutable so we can change the values in it
nums.append(45)
print(nums)

nums.insert(2,37)
print(nums)

nums.remove(45)


print(nums)

nums.pop()#willremove the last element
print(nums)

del nums[2:3]
print(nums)

nums.extend([29,12,14,45])
print(nums)

print(min(nums))
print(max(nums))
nums.sort()
print(nums)
nums.reverse()
print(nums)
nums.reverse()

print("\n\tTupple")
#Tupples are immutable
tup=(21,36,83)
print(tup)

print("\n\tSet")
s={22,43,53,14,83}
print(s)
s={22,22,43,53,13,83}
#When ever we print a set we get random values its because set uses concept of hash 
#which is used to fetc vaulues as fast as poissible 

#we cant use indexing in set
#print(s[2])

print()

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
