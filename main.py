from Account import Account
from DatabaseModel import DatabaseModel
import csv

# Create an instance of the database model
db = DatabaseModel()

# welcome message
print("******************************************")
print("* Welcome to the Bank Management Service *")
print("*                                        *")
print("******************************************")
print("")
print("Please Enter Your Account # and Pass")

# Pulls input for login
account_number = input("Account #: ")
password = input("Pass: ")
print("")

# Calls login functions
def __Login(num, password) :
    account = db.LoginToAccount(num, password)
    if(account != None) :
        print(f"Welcome back, {account.GetHolderFirstName()}")
        print("")
        __LoadUserOptions(account)
    else :
        print("Invalid Details. Please Try again.")

# Prints all of the menu options for the user
def __LoadUserOptions(account) :
    print("****************************")
    print("* Please Select An Option: *")
    print("*                          *")
    print("* 1. View Account Balance  *")
    print("* 2. Withdraw              *")
    print("* 3. Deposit               *")
    print("* 4. Transfer              *")
    print("* 5. Exit                  *")
    print("****************************")
    print("")

    player_choice = input("Enter Option: ")

    if(player_choice == "1"):
        print(db.ViewAccountBalance(account))
    elif(player_choice == "2"):
        amount = input("Please Enter Withdrawal Amount: ")
        print(db.WithdrawFromAccount(account, amount))
    elif(player_choice == "3"):
        amount = input("Please Enter a Deposit Amount: ")
        print(db.DepositIntoAccount(account, amount))
    elif(player_choice == "4"):
        amount = input("Please Enter the Amount to Transfer: ")
        destinationAccountNumber = input("Please Enter the Destination Account Number: ")
        print(db.Transfer(account, amount, db.ValidateAccount(destinationAccountNumber)))
    elif(player_choice == "5"):
        exit()
    else :
        print("Please enter a valid option.")
    
    print("")
    print("****************************")
    print("")

    __LoadUserOptions(account)

# Calls login from the database model
__Login(account_number, password)




