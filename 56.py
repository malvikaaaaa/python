s=input("Enter words:\n").split(',')
snew=[]
for i in s:
    if i not in snew:
        snew.append(i)
print(sorted(snew))
