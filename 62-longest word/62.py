#lengthiest line in a file

inputfile=False
try:
    inputfile=open("input62.txt")
    inputf=list(set(inputfile.read().split()))
    inputf.sort(key=len,reverse=True)
    print(inputf)
    print("\nLongest word(s)\n")
    for i in inputf:
        if len(i)==len(inputf[0]):
            print(i)
        
except Exception as e:
    print(e)
finally:
    if inputfile:inputfile.close()
