#Copy one file to another
inputfile=False
outputfile=False
try:
    inputfile=open("input1.txt",'r')
    #inputf=inputfile.read()
    #print(inputf)

    outputfile=open("output1.txt",'w+')
    outputf=outputfile.write(inputfile.read())
    outputfile.seek(0,0)
    outputf=outputfile.read()
    print(outputf)
except Exception as e:
    print(e)
finally:
    if inputfile:inputfile.close()
    if outputfile:outputfile.close()
    
###Result==>Rewrite the output file
