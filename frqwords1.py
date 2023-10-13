word=input("Enter a word:")
letters={}
for l in word:
    letters[l]=letters.get(l,0)+1
print("The letters are:",letters)
