s=input("Enter numbers:\n")
snew=list(map(int,s.split(',')))
counto=counte=0
for i in snew:
    if i%2:
        counto+=1
    else:
        counte+=1
print('Even :',counte,'Odd :',counto)
