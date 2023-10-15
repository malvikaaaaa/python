strng=input("Enter the string:")
if strng.lower().endswith("ing"):
    strng=strng+"ly"
else:
    strng=strng+"ing"
print("The string is:",strng)
