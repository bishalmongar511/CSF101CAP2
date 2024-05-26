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





import os
from account import Account, PersonalAccount, BusinessAccount, generate_account_number, generate_password

ACCOUNTS_FILE = 'accounts.txt'

def save_account(account):
    with open(ACCOUNTS_FILE, 'a') as f:
        f.write(f'{account.account_number},{account.password},{account.account_type},{account.balance}\n')

def load_accounts():
    accounts = {}
    if os.path.exists(ACCOUNTS_FILE):
        with open(ACCOUNTS_FILE, 'r') as f:
            for line in f:
                account_number, password, account_type, balance = line.strip().split(',')
                balance = float(balance)
                if account_type == 'Personal':
                    accounts[account_number] = PersonalAccount(account_number, password, balance)
                elif account_type == 'Business':
                    accounts[account_number] = BusinessAccount(account_number, password, balance)
    return accounts

def update_accounts_file(accounts):
    with open(ACCOUNTS_FILE, 'w') as f:
        for account in accounts.values():
            f.write(f'{account.account_number},{account.password},{account.account_type},{account.balance}\n')

def create_account(account_type):
    account_number = generate_account_number()
    password = generate_password()
    if account_type == 'Personal':
        account = PersonalAccount(account_number, password)
    elif account_type == 'Business':
        account = BusinessAccount(account_number, password)
    accounts = load_accounts()
    accounts[account_number] = account
    save_account(account)
    return account_number, password

def delete_account(account_number):
    accounts = load_accounts()
    if account_number in accounts:
        del accounts[account_number]
        update_accounts_file(accounts)
        return True
    return False

def login(account_number, password):
    accounts = load_accounts()
    account = accounts.get(account_number)
    if account and account.password == password:
        return account
    return None
