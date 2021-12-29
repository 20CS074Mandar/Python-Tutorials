mystr="This is Python Tutorial"

print("\nLength of my str",len(mystr))
print("mystr= ",mystr[0:5])
print("mystr[0:5:2] : ",mystr[0:5:2])
print("mystr[::] : ",mystr[::])
print("mystr[-1:0] :",mystr[-1:0])
print("mystr[-1:] :",mystr[-1:])
print("mystr[15:17] :",mystr[15:17])
print("mystr[::-2] :",mystr[::-2])

print("\nmystr.isalnum() : ",mystr.isalnum())
print("mystr.endswith() : ",mystr.endswith("Tutorial"))
print("mystr.count() to count T in mystr: ",mystr.count("T"))
print("mystr.find() : ",mystr.find("is"))
print(mystr.lower())
print(mystr.upper())
print(mystr.replace("is","are"),"\n")

print("10".isnumeric())
print(mystr.expandtabs(4))
