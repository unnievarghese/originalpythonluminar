class Bank:
    def create_account(self,account_no,name,min_balnce,bank_name):
        self.account_no=account_no
        self.name=name
        self.min_balance=min_balnce
        self.bank_name=bank_name
    def deposit(self,amount):
        self.min_balance+=amount
        print("your acoount",self.account_no,"has been credited with,",amount,'\ncurrent balance is:',self.min_balance)
    def withdrawal(self,amount):
        if amount>self.min_balance:
            print("sorry,order not processed due to insufficient balane.",'\navailable balance is:',self.min_balance,
                  "\nThe amount requested is",amount)
        else:
            self.min_balance-=amount
            print('order succefully processed.Available balance is:',self.min_balance)
    def balance_enquiry(self):
        print('For account number',self.account_no,'\nThe available balance is',self.min_balance)
atm=Bank()
print('create an account:')
acc=input('Enter Bank acoount number:')
nam=input('Enter the Name:')
minba=int(input('Enter minimum balance:'))
bnk=input('Enter bank name:')
atm.create_account(acc,nam,minba,bnk)
print('Choose any operation given below:\n\t1.Make deposit\t2.Make withdrawal\n\t3.Balance enquiry')
flag=int(input())
if flag==1:
    dep=int(input('Enter the deposit amount:'))
    atm.deposit(dep)
elif flag==2:
    withdraw=int(input('Enter the amount to withdraw:'))
    atm.withdrawal(withdraw)
elif flag==3:
    atm.balance_enquiry()