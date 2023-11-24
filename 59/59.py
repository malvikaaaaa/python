#count the number of lines
inputfile=False
try:
    inputfile=open("input59.txt",'r')
    inputf=inputfile.readlines()
    #print(inputf)

    print("Number of lines in the file :",len(inputf))

except Exception:
    print("No such file")
finally:
    if inputfile:inputfile.close()
