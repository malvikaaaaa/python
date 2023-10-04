num=input("enter the numbers:")
numlist=num.split()
small=int(numlist[0])
large=int(numlist[0])
for i in numlist:
    if(int(i)>large):
        large=int(i)
    elif(int(i)<small):
        small=int(i)
print("the list is\n",numlist)
print("maximum number is",large,"\nminimum number is",small)
    
