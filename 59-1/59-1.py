#count the number of lines
inputfile=False
try:
    inputfile=open("input59.txt",'r+')
    print(inputfile.read())
    inputfile.seek(0,0)
    inputf=inputfile.readlines()
    print("Number of lines in the file :",len(inputf))

except Exception as e:
    print(e)

finally:
    if inputfile:inputfile.close()
