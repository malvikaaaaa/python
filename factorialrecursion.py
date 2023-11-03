#factorial of a number(normal)

def factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact*=i
    return fact

n=int(input("Enter a number:"))
print("Factorial of",n,"is",(n,factorial(n))) if n>0 else print("Factorial not found")

#using recursion

def facto(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return n*facto(n-1)
n=int(input("Enter the number:"))
print("Factorial of",n,"=",factorial(n))
