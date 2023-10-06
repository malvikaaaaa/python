words=input("Enter the list of words:")
wordslist=words.split(',')
num=int(input("\nEnter a number:"))
for i in wordslist:
    if(len(i)>num):
        print(i)
