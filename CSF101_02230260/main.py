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
from account_manager import create_account, login, delete_account, load_accounts, update_accounts_file

def main():
    accounts = load_accounts() 
    while True:
        print("Welcome to Bank")
        print("1. Create Account")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print("Choose the account:")
            print("1. Personal")
            print("2. Business")
            account_type_choice = input("Enter 1 or 2: ")
            account_type = 'Personal' if account_type_choice == '1' else 'Business' if account_type_choice == '2' else None
            if account_type:
                account_number, password = create_account(account_type)
                print(f"Account has been created successfully, Your account.NO is {account_number} and password is {password}")
            else:
                print("Invalid account type")

        elif choice == '2':
            account_number = input("Enter account.NO: ")
            password = input("Enter your password: ")
            account = login(account_number, password)
            if account:
                while True:
                    print("1. Check Balance")
                    print("2. Deposit")
                    print("3. Withdraw")
                    print("4. Transfer")
                    print("5. Delete Account")
                    print("6. Logout")
                    choice = input("Choose an option form given: ")

                    if choice == '1':
                        print(f"Your current balance is: {account.balance}")

                    elif choice == '2':
                        amount = float(input("Enter the amount to deposit: "))
                        if account.deposit(amount):
                            print("Deposit successful")
                            accounts[account.account_number] = account
                            update_accounts_file(accounts)
                        else:
                            print("Invalid amount")

                    elif choice == '3':
                        amount = float(input("Enter the amount to withdraw: "))
                        if account.withdraw(amount):
                            print("Withdrawal successful")
                            accounts[account.account_number] = account
                            update_accounts_file(accounts)
                        else:
                            print("Insufficient funds currently")

                    elif choice == '4':
                        target_account_number = input("Enter the target account.NO: ")
                        amount = float(input("Enter the amount to transfer: "))
                        target_account = accounts.get(target_account_number)
                        if target_account and account.transfer(target_account, amount):
                            print("Transfer has been successful")
                            accounts[account.account_number] = account
                            accounts[target_account.account_number] = target_account
                            update_accounts_file(accounts)
                        else:
                            print("Transfer has failed.")

                    elif choice == '5':
                        if delete_account(account.account_number):
                            print("Account has been deleted successfully")
                            break
                        else:
                            print("Account deletion failed")

                    elif choice == '6':
                        print(" Successfully Logged out")
                        break

                    else:
                        print("Invalid option")
            else:
                print("Invalid account number or password")

        elif choice == '3':
            print("Thank you for using this Terminal Bank")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
