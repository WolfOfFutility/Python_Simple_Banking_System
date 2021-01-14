class Account:
    def __init__(self, acc_num, password, account_balance, holder_first_name, holder_sirname):
        self.__acc_num = acc_num
        self.__password = password
        self.__account_balance = account_balance
        self.__holder_first_name = holder_first_name
        self.__holder_sirname = holder_sirname
    
    def Login(self, accountNumber, password):
        if(self.__acc_num == int(accountNumber) and (self.__password == password)):
            return self
        else :
            return None

    def GetAccountBalance(self) :
        return self.__account_balance

    def GetAccountNum(self) :
        return self.__acc_num

    def GetHolderFirstName(self) :
        return self.__holder_first_name

    def DepositToAccount(self, amount) :
        self.__account_balance += amount
        self.__account_balance = round(self.__account_balance, 2)
        return "Deposited " + str(round(amount,2)) + " to account, new total is " + str(round(self.__account_balance, 2))

    def WithdrawFromAccount(self, amount):
        self.__account_balance -= amount
        self.__account_balance = round(self.__account_balance, 2)
        return "Withdrew " + str(round(amount,2)) + " from account, new total is " + str(round(self.__account_balance, 2))
    
    def ForWriter(self):
        return [self.__acc_num, self.__password, self.__account_balance, self.__holder_first_name, self.__holder_sirname]
