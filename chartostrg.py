char=input("Enter the list of character:")
charlist=char.split(",")
str=""
for i in charlist:
    str=str+i
print("The string is",str)
