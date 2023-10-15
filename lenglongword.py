strg=input("Enter a string:")
strg=strg.split(' ')
strg.sort(key=len,reverse=True)
print("Length of longest word:",len(strg[0]))
if len(strg[0])==len(strg[1]):
    print('BINGO')
