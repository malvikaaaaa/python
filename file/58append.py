#Append one file to another
inputfile=False
outputfile=False
try:
    inputfile=open("input2.txt",'r')
    #inputf=inputfile.read()
    #print(inputf)

    outputfile=open("output2.txt",'a+')
    outputf=outputfile.write('\n'+inputfile.read())
    outputfile.seek(0,0)
    outputf=outputfile.read()
    print(outputf)
except Exception as e:
    print(e)
finally:
    if inputfile:inputfile.close()
    if outputfile:outputfile.close()
    

##Result==> Append to the output file
