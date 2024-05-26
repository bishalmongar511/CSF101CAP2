################################
# Your Name:Bishal Mongar
# Your Section : Mechanical Engineering 
# Your Student ID Number : 02230260
################################
# REFERENCES
#Advapay. (2023, March 21). Web banking and Mobile apps - Core Banking platform | Advapay. https://advapay.eu/functionality-core-banking/web-banking-and-mobile-banking-applications/
#Juyal, P. (2022, December 30). What is a Mobile Banking Application? Know Everything About it! A Comprehensive Guide to Money Transfer, Recharges, Bill Payments and Other Digital Payments | Paytm Blog. https://paytm.com/blog/net-banking/what-is-mobile-banking-application/
#Lloyds Bank Mobile Banking - apps on Google Play. (n.d.). https://play.google.com/store/apps/details?id=com.grppl.android.shell.CMBlloydsTSB73&hl=en
#Petelko, E., & Petelko, E. (2024, February 7). How to Create a Banking Application from Idea to Ready Product? https://existek.com/blog/how-to-create-a-banking-application/




import random
import string


class Account:
    def __init__(self, account_number, password, account_type, balance=0):
        self.account_number = account_number
        self.password = password
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def transfer(self, target_account, amount):
        if self.withdraw(amount):
            target_account.deposit(amount)
            return True
        return False

class PersonalAccount(Account):
    def __init__(self, account_number, password, balance=0):
        super().__init__(account_number, password, 'Personal', balance)

class BusinessAccount(Account):
    def __init__(self, account_number, password, balance=0):
        super().__init__(account_number, password, 'Business', balance)

def generate_account_number():
    return ''.join(random.choices(string.digits, k=10))

def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))
