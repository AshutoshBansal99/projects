'''Documentation
We will prompt end user to select account type?
1.Saving Account 
2.Current Account 


1.Saving Account:
    Applicant Name
    Initial balance

2.current Account:
    Company Name
    Initial balance
    
validation: Initial Balance >= 0
                else prompt again,3 times
                then Exit.

We have to create a random account number and with that accont number required account should be created

Every Transaction Should be logged.
    And we will store every thing in some dictionary.
        addlog()
        
Related to Account :
    A/C No
    Name
    Balance
    Min_balance
    Withdrow()
    deposit()
    getStatement()
    getMiniStatement() #only last 3 Transaction.
    getAccountInfo()
    balanceEnquery()
    
Limit the Number of transaction: 5
If more than 5 for every tranction 10Rs charge
    
Withdrow():
    Should be multiple of 100
    withdraw limit is 10000 per transaction
    
'''
from abc import ABC, abstractclassmethod
import datetime
from random import *
import sys


class Utill:
    history = []

    @staticmethod
    def accountnum():
        sum = ""
        for i in range(12):
            a = str(randint(0, 9))
            sum = sum+a
        return sum

    @classmethod
    def addEntry(cls, msg):
        Utill.history.append(msg)

    @staticmethod
    def createAccount(accountType):
        if accountType == "Savings":
            name = input("Enter Customer Name: ")
        else:
            name = input("Enter Company Name: ")

        balance = eval(input("Enter the Initial Balance: "))

        xyz = balance
        while balance < 0:
            balance = eval(input(
                "You have Enter the balance less than the minimum balance! pls provide the balance > 0: "))
        if accountType == "Savings":
            account = SavingAccount(name, balance)
        else:
            account = CurrentAccount(name, balance)

        Utill.addEntry('{}:-{} - {} account got created Successfully with A/C NO:{} and With initial balance: {} '.format(
            datetime.datetime.now(), name, accountType, account.account_number, account.balance))
        print("Congratulation,Your {} Account Is been Created With a Account no: {} ".format(
            accountType, account.account_number))

        return account

    @classmethod
    def detailedStatement(self):
        print(self.history[0])
        print('Your Last {} Transaction are : '.format(len(self.history)-1))
        print('#'*102)
        no = 1
        for transaction in self.history[1:]:
            print('{}.  {}'.format(no, transaction))
            no += 1
        print()

    @classmethod
    def miniStatement(self):
        print(self.history[0])
        if (len(self.history[0])-1) <= 5:

            print('Your Last {} Transaction are : '.format(len(self.history)-1))
            print('#'*102)
            no = 1
            for transaction in self.history[1:]:
                print('{}.  {}'.format(no, transaction))
                no += 1
        else:
            print('Your Last 5 Transaction are : ')
            print('#'*102)
            no = 1
            for transaction in self.history[-5:]:
                print('{}.  {}'.format(no, transaction))
                no += 1
        print()


class Account(ABC):
    Bank_Name = "Ashutosh World Bank"
    tlimit = 0
    max_Withdraw_Limt = 20000
    withdraw_amount = 0

    def __init__(self, name, balance, min_balance):
        # genrate  random account number.
        self.account_number = Utill.accountnum()
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    @abstractclassmethod
    def balanceEnquiry(self): pass

    @abstractclassmethod
    def getAccountInformation(self): pass

    def deposit(self):

        amount = eval(input('Enter Ammount to Deposit: '))
        while amount < 0:
            amount = eval(input('Plz Enter Valid Ammount to Deposit: '))
        self.balance += amount
        account.tlimit += 1
        if account.tlimit > 5:
            self.balance -= 10
            print("Additional Charge as The Number of Transaction Exceeds")

        Utill.addEntry('{}: {} Account Credited (Deposit) With Amount :{} '.format(
            datetime.datetime.now(), self.name, amount))
        print('After Deposit, Your Account Balance Is : ', self.balance)
        print()

    def withdraw(self):
        amount = eval(input('Enter Ammount to Withdraw: '))
        while amount < 0 or amount % 100 != 0:
            amount = eval(
                input('Plz Enter Valid Ammount,In multiple of 100 only  to Withdraw: '))

        if self.balance - amount >= self.min_balance:
            if self.withdraw_amount + amount <= self.max_Withdraw_Limt:
                self.balance -= amount
                self.withdraw_amount += amount
                account.tlimit += 1
                if account.tlimit > 5:
                    self.balance -= 10
                    print("Additional Charge as The Number of Transaction Exceeds")
                Utill.addEntry('{}: {} Account debited (Withdraw) With Amount :{} '.format(
                    datetime.datetime.now(), self.name, amount))
                print('After Withdrawl, Your Account Balance Is : ', self.balance)
                print()
            else:
                print("You have Exeeded the withdrawal abount!!!")

        else:
            print("Insufficent Funds !!!")
            print()


class SavingAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, 0)

    def balanceEnquiry(self):
        print("Hello {} ,  Balance in your Saving's Account With Account Number XXXXXXXX{},Is : {} /-".format(
            self.name, self.account_number[8:], self.balance))
        print()

    def getAccountInformation(self):
        print('Your Savings Account Information !! ')
        print('Account Number: ', self.account_number)
        print('Customer Name: ', self.name)
        print('Current balance: ', self.balance)
        print()


class CurrentAccount(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, -1000)

    def balanceEnquiry(self):
        print("Hello {} ,  Balance in your Current Account With Account Number XXXXXXXX{},Is : {} /-".format(
            self.name, self.account_number[8:], self.balance))

    def getAccountInformation(self):
        print('Your Current Account Information !! ')
        print('Account Number: ', self.account_number)
        print('Customer Name: ', self.name)
        print('Current balance: ', self.balance)
        print()
# main function..... start From Hear.


print("Welcome to", Account.Bank_Name)
print('Coose Your Required Account Type:\n 1. Saving Account --- S \n 2. Current Account --- C \n')
option = input('Choose Your Otion:').lower()
count = 1
while option not in ['s', 'c']:
    if count >= 3:
        print("Sorry!! you Reach the maximum Atempt ,Try after some Time.")
        sys.exit()
    option = input('plese Select the valid option[S|C]').lower()
    count = count+1
if option == 's':
    account = Utill.createAccount('Savings')
    print()

else:
    account = Utill.createAccount('Current')
    print()

while True:
    print(' B   --- Balance Enquery \n D   --- Deposit \n W   --- Withdraw \n MS  --- Mini statement \n DS  --- Detailed statement \n GAI --- Get Account Information \n E   --- Exit')
    print()
    option = input('Choose your Option: ').lower()
    count = 1
    while option not in ['b', 'd', 'w', 'ms', 'ds', 'gai', 'e']:
        if count >= 3:
            print("Sorry!! you Reach the maximum Atempt ,Try after some Time.")
            sys.exit()
        option = input(
            "Invalid choice !!!. Choose your Option from: ['b'|'d'|'w'|'ms'|'ds'|'gai'|'e']:-  ").lower()
        count = count+1

    if option == 'b':
        account.balanceEnquiry()
    elif option == "gai":
        account.getAccountInformation()
    elif option == "d":
        account.deposit()
    elif option == "w":
        account.withdraw()
    elif option == "ms":
        Utill.miniStatement()
    elif option == "ds":
        Utill.detailedStatement()
    else:
        print('Thanks for using {} '.format(account.Bank_Name))
        sys.exit()
    print()
