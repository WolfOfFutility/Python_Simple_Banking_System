from Account import Account
from DatabaseModel import DatabaseModel
import csv
import tkinter as tk

account = []

# Create an instance of the database model
db = DatabaseModel()

# Handles viewing account balance
def __HandleViewAccount(account, content_frame) :
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    content_header_label = tk.Label(content_frame, bg="lightgreen", text="View Account Balance", anchor="w", font="Arial 20 bold")
    content_header_label.place(relheight=0.1, relwidth=0.9, relx=0.05)

    account_amount_label = tk.Label(content_frame, bg="lightgreen", text = "Account Balance: " + db.ViewAccountBalance(account), anchor="w")
    account_amount_label.place(relheight=0.1, relwidth=0.9, relx=0.05, rely=0.15)

# Handles withdrawal and prints it to the GUI
def __HandleWithdrawal(account, amount, content_frame):
    withdraw_message_label = tk.Label(content_frame, bg="lightgreen", text=db.WithdrawFromAccount(account, amount), anchor="w")
    withdraw_message_label.place(relheight=0.1, relwidth=0.9, relx=0.05, rely=0.4)
    
# Opens the withdrawal screen
def __OpenWithdrawal(account, content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    content_header_label = tk.Label(content_frame, bg="lightgreen", text="Withdrawal", anchor="w", font="Arial 20 bold")
    content_header_label.place(relheight=0.1, relwidth=0.9, relx=0.05)

    withdrawal_amount_frame = tk.Frame(content_frame, bg="lightgreen")
    withdrawal_amount_frame.place(relheight=0.1, relwidth=0.5, relx=0.05, rely=0.15)
    withdrawal_amount_label = tk.Label(withdrawal_amount_frame, bg="lightgreen", text="Withdrawal Amount: ")
    withdrawal_amount_label.place(relheight=1, relwidth=0.5)
    withdrawal_amount_entry = tk.Entry(withdrawal_amount_frame, bg="white")
    withdrawal_amount_entry.place(relheight=1, relwidth=0.5, relx=0.5)

    withdraw_button = tk.Button(content_frame, bg="midnightblue", fg="white", text="Withdraw", command = lambda: __HandleWithdrawal(account, withdrawal_amount_entry.get().strip(), content_frame))
    withdraw_button.place(relheight=0.1, relwidth=0.2, rely=0.3, relx=0.05)

# Handles the deposits and prints message to gui
def __HandleDeposit(account, amount, content_frame):
    deposit_message_label = tk.Label(content_frame, bg="lightgreen", text=db.DepositIntoAccount(account, amount), anchor="w")
    deposit_message_label.place(relheight=0.1, relwidth=0.9, relx=0.05, rely=0.4)

# Opens deposit screen
def __OpenDeposit(account, content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    content_header_label = tk.Label(content_frame, bg="lightgreen", text="Deposit", anchor="w", font="Arial 20 bold")
    content_header_label.place(relheight=0.1, relwidth=0.9, relx=0.05)

    deposit_amount_frame = tk.Frame(content_frame, bg="lightgreen")
    deposit_amount_frame.place(relheight=0.1, relwidth=0.5, relx=0.05, rely=0.15)
    deposit_amount_label = tk.Label(deposit_amount_frame, bg="lightgreen", text="Deposit Amount: ")
    deposit_amount_label.place(relheight=1, relwidth=0.5)
    deposit_amount_entry = tk.Entry(deposit_amount_frame, bg="white")
    deposit_amount_entry.place(relheight=1, relwidth=0.5, relx=0.5)

    deposit_button = tk.Button(content_frame, bg="midnightblue", fg="white", text="Deposit", command = lambda: __HandleDeposit(account, deposit_amount_entry.get().strip(), content_frame))
    deposit_button.place(relheight=0.1, relwidth=0.2, rely=0.3, relx=0.05)

# Handles transfer and puts a message on GUI
def __HandleTransfer(account, amount, recipient, content_frame):
    transfer_message_label = tk.Label(content_frame, bg="lightgreen", text=db.Transfer(account, amount, db.ValidateAccount(recipient)), anchor="w")
    transfer_message_label.place(relheight=0.1, relwidth=0.9, relx=0.05, rely=0.5)    

# Puts transfer screen on the GUI
def __OpenTransfer(account, content_frame):
    for widget in content_frame.winfo_children():
        widget.destroy()

    content_header_label = tk.Label(content_frame, bg="lightgreen", text="Deposit", anchor="w", font="Arial 20 bold")
    content_header_label.place(relheight=0.1, relwidth=0.9, relx=0.05)

    transfer_amount_frame = tk.Frame(content_frame, bg="lightgreen")
    transfer_amount_frame.place(relheight=0.1, relwidth=0.5, relx=0.05, rely=0.15)
    transfer_amount_label = tk.Label(transfer_amount_frame, bg="lightgreen", text="Transfer Amount: ")
    transfer_amount_label.place(relheight=1, relwidth=0.5)
    transfer_amount_entry = tk.Entry(transfer_amount_frame, bg="white")
    transfer_amount_entry.place(relheight=1, relwidth=0.5, relx=0.5)

    transfer_to_frame = tk.Frame(content_frame, bg="lightgreen")
    transfer_to_frame.place(relheight=0.1, relwidth=0.5, relx=0.05, rely=0.25)
    transfer_to_label = tk.Label(transfer_to_frame, bg="lightgreen", text="Transfer To (Acc #): ")
    transfer_to_label.place(relheight=1, relwidth=0.5)
    transfer_to_entry = tk.Entry(transfer_to_frame, bg="white")
    transfer_to_entry.place(relheight=1, relwidth=0.5, relx=0.5)

    transfer_button = tk.Button(content_frame, bg="midnightblue", fg="white", text="Transfer", command = lambda: __HandleTransfer(account, transfer_amount_entry.get().strip(), transfer_to_entry.get().strip(), content_frame))
    transfer_button.place(relheight=0.1, relwidth=0.2, rely=0.4, relx=0.05)


# Prints all of the menu options for the user
def __LoadUserOptions(account, menu_frame, content_frame):
    view_account_balance_button = tk.Button(menu_frame, bg="midnightblue", fg="white", text="View Account Balance", command = lambda: __HandleViewAccount(account, content_frame))
    view_account_balance_button.place(relheight=0.05, relwidth=0.9, relx=0.05, rely=0.05)

    withdraw_menu_button = tk.Button(menu_frame, bg="midnightblue", fg="white", text="Withdraw Money", command = lambda: __OpenWithdrawal(account, content_frame))
    withdraw_menu_button.place(relheight=0.05, relwidth=0.9, relx=0.05, rely=0.11)

    deposit_menu_button = tk.Button(menu_frame, bg="midnightblue", fg="white", text="Deposit Money", command = lambda: __OpenDeposit(account, content_frame))
    deposit_menu_button.place(relheight=0.05, relwidth=0.9, relx=0.05, rely=0.17)

    transfer_menu_button = tk.Button(menu_frame, bg="midnightblue", fg="white", text="Transfer Money", command = lambda: __OpenTransfer(account, content_frame))
    transfer_menu_button.place(relheight=0.05, relwidth=0.9, relx=0.05, rely=0.23)


# Calls login functions
def __Login(login_frame, menu_frame, content_frame) :
    account = db.LoginToAccount(account_num_field.get().strip(), password_field.get().strip())
    if(account != None) :
        print(f"Welcome back, {account.GetHolderFirstName()}")
        print("")
        login_frame.lower(None)
        __LoadUserOptions(account, menu_frame, content_frame)
    else :
        print("Invalid Details. Please Try again.")

## Initialising the Tkinter GUI

window = tk.Tk(className="Ceejay's Banking System")
window.geometry("900x600")

main_frame = tk.Frame(window, bg="#333333")
main_frame.place(relheight=1, relwidth=1)
greeting = tk.Label(main_frame,text="Hello there!")
greeting.place(relheight=0.1, relwidth=0.1, relx=0.45)

menu_frame = tk.Frame(main_frame, bg="lightblue")
menu_frame.place(relheight=1, relwidth=0.3)

content_frame = tk.Frame(main_frame, bg="lightgreen")
content_frame.place(relheight=1, relwidth=0.7, relx=0.3)

login_frame = tk.Frame(main_frame, bg="#CCCCCC")
login_frame.place(relheight=0.3, relwidth=0.4, relx=0.3, rely=0.35)

account_num_frame = tk.Frame(login_frame, bg="#CCCCCC")
account_num_frame.place(relheight=0.2, relwidth=0.9, rely=0.05, relx=0.05)
account_num_label = tk.Label(account_num_frame, text="Account #: ", bg="#CCCCCC")
account_num_label.place(relheight=1, relwidth=0.4)
account_num_field = tk.Entry(account_num_frame, bg="white")
account_num_field.place(relheight=1, relwidth=0.6, relx=0.4)

password_frame = tk.Frame(login_frame, bg="#CCCCCC")
password_frame.place(relheight=0.2, relwidth=0.9, rely=0.35, relx=0.05)
password_label = tk.Label(password_frame, text="Password: ", bg="#CCCCCC")
password_label.place(relheight=1, relwidth=0.4)
password_field = tk.Entry(password_frame, bg="white")
password_field.place(relheight=1, relwidth=0.6, relx=0.4)

login_button = tk.Button(login_frame, bg="#1E90FF", fg="#FFFFFF", text="Login", command = lambda: __Login(login_frame, menu_frame, content_frame))
login_button.place(relheight=0.2, relwidth=0.5, rely=0.7, relx=0.25)

window.mainloop()



