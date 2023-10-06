num=input("Enter numbers\n")
numlist=num.split(',')
numlist=[int(i) for i in numlist]
numlist=sorted(numlist)

print("Second smallest element is",numlist[1])
