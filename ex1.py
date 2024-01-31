class bank:
    def __init__(self,n="nil",l="nil"):
        self.name=n
        self.location=l
    def display(self):
        print("Name:",self.name)
        print("Location:",self.location)

class insurance(bank):
    def __init__(self,n="nil",l="nil",amt=0):
        super().__init__(n,l)
        self.__amount=amt

    def display(self):
        super().display()
        print("Insurance amount:",self.__amount)

    def __le__(self,other):
        if(self.__amount<=other.__amount):
            print("Amount 1 is lesser")
        else:
            print("Amount 2 is lesser")
         #return(self.__amount<=other.__amount)


bname=input("Enter the bank name:")
bloc=input("Enter the bank location:")
iamt1=int(input("Enter insurance amt 1:"))
iamt2=int(input("Enter insurance amt 2:"))

in1=insurance(bname,bloc,iamt1)
in2=insurance(bname,bloc,iamt2)
in1.display()
in2.display()
in1<=in2
#print("Two insurance amount are less than or equal",in1<=in2)
