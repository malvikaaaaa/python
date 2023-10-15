s=input("Enter a string:")
if len(s)==2:
    new=s*2
elif len(s)>2:
    new=s[:2]+s[-2:]
else:
    new=' '
print("The string is:",new)
