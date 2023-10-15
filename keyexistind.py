d={1:23,2:34,3:11,4:5}
print(d)
key=input("Enter key:")
print(key," is in d:",key in d)
if key in d:
    print("Key already exist in d")
else:
    print("Key do not exist")
