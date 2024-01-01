class bank:
    def __init__(self,n="Empty",l="Empty"):
        self.name=n
        self.location=l

class insurance(bank):
    def __init__(self,n,l,amt=0):
        super().__init__(n,l)
        self.__amount=amt

    def display(self):
        print("Bank name: ",self.name)
        print("Bank location: ",self.location)
        print("Insurance amount:",self.__amount)

    def __le__(self,other):
        return(self.__amount<=other.__amount)


bname=input("Enter the bank name:")
bloc=input("Enter the bank location:")
iamt1=input("Enter insurance amt 1:")
iamt2=input("Enter insurance amt 2:")

in1=insurance(bname,bloc,iamt1)
in2=insurance(bname,bloc,iamt2)
in1.display()
in2.display()
print("Two insurance amount are less than or equal",in1<=in2)

