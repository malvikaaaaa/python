n=int(input("Enter a number:"))
result='Even' if not n%2 else 'Odd'
print("The number is",result)

l=input("Enter a list:")
l=l.split(',')
value=input("Enter a value:")
l=list(map(str,l))
result1='Available' if value in l else 'Not available'
print(value,"is",result1,"in list")
