class bank:
    def __init__(self,acc_no="Empty",acc_na="Empty",acc_t="Empty",acc_b=0):
        self.acc_number=acc_no
        self.acc_name=acc_na
        self.acc_type=acc_t
        self.acc_balance=acc_b

    def deposit(self,damt=0):
        self.acc_balance=self.acc_balance+damt

    def withdraw(self):
        if self.acc_balance==0:
            print("\nZero balance")
        else:
            wamt=int(input("Enter the amount to withdraw:"))
            if(self.acc_balance-wamt)<0:
                print("\nNo sufficient balance")
            else:
                self.acc_balance=self.acc_balance-wamt

    def showdetails(self):
        print("\n*******your account*******\n")
        print("Account holder:",self.acc_name)
        print("Account type:",self.acc_type)
        print("Account balance:",self.acc_balance)


name=input("Enter name\n")
number=input("Enter account number\n")
acctype=input("Enter account type\n")

b=bank(number,name,acctype)
b.showdetails()
while(True):
    print("\n\n1.Deposit\n2.Withdraw\n3.Accountdetails\n4.Exit\n")
    n=int(input("Enter choice:"))
    if n==1:
        d=int(input("Enter amount:"))
        b.deposit(d)
    elif n==2:
        b.withdraw()
    elif n==3:
        b.showdetails()
    else:
        print("Exited")
        break
