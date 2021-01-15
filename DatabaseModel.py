from Account import Account
import csv

 # A class that handles all of the backend functions, to keep data as safe as possible
class DatabaseModel :
    def __init__(self) :
        self.__accountsList = []

    # Writes everything to a csv file
    def __WriteToCsv(self,accountsList) :
        with open("account_data.txt", "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')

            for a in accountsList:
                a.AddToWriteable(csv_writer)

    # reads everything from a csv file
    def __ReadCsv(self):
        with open("account_data.txt", "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0

            for row in csv_reader:
                if(row == "") :
                    next(csv_reader)
                else :
                    self.__accountsList.append(
                        Account(
                            int(row[0].strip()), 
                            row[1].strip(), 
                            float(row[2].strip()), 
                            row[3].strip(), 
                            row[4].strip()
                        )
                    )

                    line_count += 1
    
    # checks an account number exists, and then returns the account if it does
    def ValidateAccount(self,accountNumber):
        for x in self.__accountsList :
            if(x.GetAccountNum() == int(accountNumber)):
                return x
                break

    # Logs in to an account
    def LoginToAccount(self, accountNumber, Password) :
        self.__ReadCsv()
        for x in self.__accountsList :
            account = x.Login(accountNumber, Password)
            if(account != None):
                return account
                break

    # returns the current balance of an account
    def ViewAccountBalance(self,account) :
        return "$" + str(account.GetAccountBalance())

    # Withdraws money from an account
    def WithdrawFromAccount(self,account, amount):
        withdrawMessage = account.WithdrawFromAccount(float(amount))
        self.__WriteToCsv(self.__accountsList)
        return withdrawMessage
        
    # Deposits money into an account
    def DepositIntoAccount(self,account, amount):
        depositMessage = account.DepositToAccount(float(amount))
        self.__WriteToCsv(self.__accountsList)
        return depositMessage
    
    # Transfers money from one account to another
    def Transfer(self, account, amount, destinationAccount):
        withdrawMessage = account.WithdrawFromAccount(float(amount))
        depositMessage = destinationAccount.DepositToAccount(float(amount))
        self.__WriteToCsv(self.__accountsList)

        return f"{amount} successfully transferred to {destinationAccount.GetHolderFirstName()}"
