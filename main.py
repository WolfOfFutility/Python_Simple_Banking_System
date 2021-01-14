from Account import Account
import csv

__accountsList = []

def __WriteToCsv() :
    with open("account_data.txt", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',')

        for a in __accountsList:
            csv_writer.writerow(a.ForWriter())


def __ReadCsv():
    with open("account_data.txt", "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0

        for row in csv_reader:
            if(row == "") :
                next(csv_reader)
            else :
                __accountsList.append(
                    Account(
                        int(row[0].strip()), 
                        row[1].strip(), 
                        float(row[2].strip()), 
                        row[3].strip(), 
                        row[4].strip()
                    )
                )

                line_count += 1

__ReadCsv()

print("******************************************")
print("* Welcome to the Bank Management Service *")
print("*                                        *")
print("******************************************")
print("")
print("Please Enter Your Account # and Pass")

account_number = input("Account #: ")
password = input("Pass: ")
print("")

def __ValidateAccount(accountNumber):
    for x in __accountsList :
        if(x.acc_num == int(accountNumber)):
            return x
            break

def __LoginToAccount(accountNumber, Password) :
    for x in __accountsList :
        account = x.Login(accountNumber, Password)
        if(account != None):
            print(f"Welcome back, {account.GetHolderFirstName()}")
            print("")
            __LoadUserOptions(account)
            break

def __ViewAccountBalance(account) :
    print("$" + str(account.GetAccountBalance()))

def __WithdrawFromAccount(account, amount):
    print(account.WithdrawFromAccount(float(amount)))
    __WriteToCsv()

def __DepositIntoAccount(account, amount):
    print(account.DepositToAccount(float(amount)))
    __WriteToCsv()

def __Transfer(account, amount, destinationAccount):
    withdrawMessage = account.WithdrawFromAccount(float(amount))
    depositMessage = destinationAccount.DepositToAccount(float(amount))
    __WriteToCsv()

    print(withdrawMessage)

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
        __ViewAccountBalance(account)
    elif(player_choice == "2"):
        amount = input("Please Enter Withdrawal Amount: ")
        __WithdrawFromAccount(account, amount)
    elif(player_choice == "3"):
        amount = input("Please Enter a Deposit Amount: ")
        __DepositIntoAccount(account, amount)
    elif(player_choice == "4"):
        amount = input("Please Enter the Amount to Transfer: ")
        destinationAccountNumber = input("Please Enter the Destination Account Number: ")
        __Transfer(account, amount, __ValidateAccount(destinationAccountNumber))
    elif(player_choice == "5"):
        exit()
    else :
        print("Please enter a valid option.")
    
    print("")
    print("****************************")
    print("")

    __LoadUserOptions(account)

__LoginToAccount(account_number, password)




