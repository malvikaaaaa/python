def rev_name(name):
    for word in name[::-1]:
        print(word,end=" ")

n=input('Enter full name:').split()
rev_name(n)
