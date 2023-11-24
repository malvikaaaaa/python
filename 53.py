n=int(input("Number of steps:"))
for i in range(n):
    for k in range(i,n):
        print(end=' ')
    for j in range(i+1):
        print(i+1,end=' ')
    print()
