class Account:
    def __init__(self, acc_num, password, account_balance, holder_first_name, holder_sirname):
        self.__acc_num = acc_num
        self.__password = password
        self.__account_balance = account_balance
        self.__holder_first_name = holder_first_name
        self.__holder_sirname = holder_sirname
    
    # Logs in to an account
    def Login(self, accountNumber, password):
        if(self.__acc_num == int(accountNumber) and (self.__password == password)):
            return self
        else :
            return None

    # returns the account balance of the account
    def GetAccountBalance(self) :
        return self.__account_balance

    # Returns the account number of the account
    def GetAccountNum(self) :
        return self.__acc_num

    # returns the account holders first name
    def GetHolderFirstName(self) :
        return self.__holder_first_name

    # deposits money into the account
    def DepositToAccount(self, amount) :
        self.__account_balance += amount
        self.__account_balance = round(self.__account_balance, 2)
        return "Deposited " + str(round(amount,2)) + " to account, new total is " + str(round(self.__account_balance, 2))

    # withdraws money from the account
    def WithdrawFromAccount(self, amount):
        self.__account_balance -= amount
        self.__account_balance = round(self.__account_balance, 2)
        return "Withdrew " + str(round(amount,2)) + " from account, new total is " + str(round(self.__account_balance, 2))
    
    # Adds the account to the list, read to be written back into the csv
    def AddToWriteable(self, csv_writer):
        csv_writer.writerow([self.__acc_num, self.__password, self.__account_balance, self.__holder_first_name, self.__holder_sirname])
