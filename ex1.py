class bank:
    def __init__(self,n="nil",l="nil"):
        self.name=n
        self.location=l
    def display(self):
        print("Bank Name:",self.name)
        print("Bank Location:",self.location)

class insurance(bank):
    def __init__(self,n="nil",l="nil",amt=0):
        super().__init__(n,l)
        self.__amount=amt
        
    def display1(self):
        super().display()
        
    def display2(self):
        print("Insurance amount:",self.__amount)

    def __le__(self,other):
        #if(self.__amount<=other.__amount):
            #print("Amount 1 is lesser")
        #else:
            #print("Amount 2 is lesser")
        return(self.__amount<=other.__amount)


bname=input("Enter the bank name:")
bloc=input("Enter the bank location:")
iamt1=int(input("Enter insurance amt 1:"))
iamt2=int(input("Enter insurance amt 2:"))

in1=insurance(bname,bloc,iamt1)
in2=insurance(bname,bloc,iamt2)
in1.display1()
in1.display2()
in2.display2()
if(in1<=in2):
    print("Amount 1 is lesser")
else:
    print("Amount 2 is lesser")
    
#print("Two insurance amount are less than or equal",in1<=in2)
