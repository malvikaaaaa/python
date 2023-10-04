num=input("Enter the numbers:")
numlist=num.split(',')
even=[i for i in numlist if int(i)%2==0]
print("List of even numbers are",even)
