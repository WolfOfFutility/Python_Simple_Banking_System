from Account import Account
from DatabaseModel import DatabaseModel
import csv
import tkinter as tk

# Create an instance of the database model
db = DatabaseModel()

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

# Calls login functions
def __Login() :
    account = db.LoginToAccount(account_num_field.get().strip(), password_field.get().strip())
    if(account != None) :
        print(f"Welcome back, {account.GetHolderFirstName()}")
        print("")
        __LoadUserOptions(account)
    else :
        print("Invalid Details. Please Try again.")

window = tk.Tk(className="Ceejay's Banking System")
window.geometry("900x600")

main_frame = tk.Frame(window, bg="#333333")
main_frame.place(relheight=1, relwidth=1)
greeting = tk.Label(main_frame,text="Hello there!")
greeting.place(relheight=0.1, relwidth=0.1, relx=0.45)

login_frame = tk.Frame(main_frame, bg="#CCCCCC")
login_frame.place(relheight=0.3, relwidth=0.4, relx=0.3, rely=0.35)

account_num_frame = tk.Frame(login_frame, bg="#CCCCCC")
account_num_frame.place(relheight=0.2, relwidth=0.9, rely=0.05, relx=0.05)
account_num_label = tk.Label(account_num_frame, text="Account #: ", bg="#CCCCCC")
account_num_label.place(relheight=1, relwidth=0.4)
account_num_field = tk.Entry(account_num_frame, bg="#CCCCCC")
account_num_field.place(relheight=1, relwidth=0.6, relx=0.4)

password_frame = tk.Frame(login_frame, bg="#CCCCCC")
password_frame.place(relheight=0.2, relwidth=0.9, rely=0.35, relx=0.05)
password_label = tk.Label(password_frame, text="Password: ", bg="#CCCCCC")
password_label.place(relheight=1, relwidth=0.4)
password_field = tk.Entry(password_frame, bg="#CCCCCC")
password_field.place(relheight=1, relwidth=0.6, relx=0.4)

login_button = tk.Button(login_frame, bg="#1E90FF", fg="#FFFFFF", text="Login", command = __Login)
login_button.place(relheight=0.2, relwidth=0.5, rely=0.7, relx=0.25)

window.mainloop()

# welcome message
print("******************************************")
print("* Welcome to the Bank Management Service *")
print("*                                        *")
print("******************************************")
print("")
print("Please Enter Your Account # and Pass")

# Pulls input for login
# account_number = input("Account #: ")
# password = input("Pass: ")
# print("")




