#c0-4(using option)
#create a bank account with member account, name,type of account and balemnce write a constructor and method to deposit at bank and amount from bank
class bankaccount:
    def __init__(self,acnum,acname,actype,acbalence):
        self.accountname=acname
        self.accountnumber=acnum
        self.accounttype=actype
        self.accountbalence=acbalence
    def deposit(self,amount):
        self.accountbalence+=amount
        print("current balence:",self.accountbalence)
        print("deposited amount",amount)
    def withdraw(self,amount):
        if amount>self.accountbalence:
            print("insuffient balence")
        else:
            self.accountbalence-=amount
            print("withdrawn",amount," .....current balence is....",self.accountbalence)
            
    def accountinfo(self):
        print("Account number",self.accountnumber)
        print("Account name",self.accountname)
        print("Account type",self.accounttype)
        print("Account balence",self.accountbalence)
        
acnum=int(input("enter account num"))
acname=input("enter the account name")
actype=input("enter account type")
acbalence=float(input("enter account balence"))

print("1. View Account Info")
print("2. Deposit Amount")
print("3. Withdraw Amount")
option = int(input("Enter your option (1/2/3): "))
obj=bankaccount(acnum,acname,actype,acbalence)

if option==1:
   print("Amount info:",obj.accountinfo())
elif option==2:
   acamount=int(input("enter the amount to deposit"))
   print("Deposit amount",obj.deposit(acamount))
elif option==3:
   withdraw=int(input("enter the amount to withdraw"))
   print("Amount",obj.withdraw(withdraw))
else:
   print("invalid")







