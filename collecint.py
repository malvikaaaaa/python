s1=input("Enter 1st set of numbers:")
s1=set(map(int,s1.split(',')))
s2=input("Enter 2nd set of numbers:")
s2=set(map(int,s2.split(',')))

s1leng=len(s1)
s2leng=len(s2)

print("The length of sets are same:",bool(s1leng==s2leng))

s1sum=sum(s1)
s2sum=sum(s2)

print("The sums of sets are same:",bool(s1sum==s2sum))

print("Any common elements occur in both:",bool(len(s1&s2)))
