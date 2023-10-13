line=input("Enter sentence:")
words={}
for i in line.split():
    words[i]=words.get(i,0)+1
print("Frequency of words:",words)
