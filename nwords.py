words=input("Enter the list of words:")
wordslist=words.split(',')
num=int(input("\nEnter a number:"))
print("Number longer than ",num,"is:")
for i in wordslist:
    if(len(i)>num):
        print(i)
