import datetime
class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name
    def Deposit(self, deposit_amount):
        self.balance += deposit_amount
        
    def Witdraw(self, withdrawal_amount):
        if withdrawal_amount > self.balance:
            print("\nInsufficient balance please top up and try again!")
            print(f"Your current balance is {self.balance}\n")
        else:
            self.balance -= withdrawal_amount
            print(f"\nYou have successfully withdrawn {withdrawal_amount} and your current balance is {self.balance}\n")
            
    def Check_balance(self):
        print(f"\nDear {self.customer_name}")
        print(f"Your current balance is {self.balance}\n")

    def customer_details(self):
        print(f'\nCustomer name: {self.customer_name}')
        print(f"Account number: {self.account_number}")
        print(f'Your current balance is {self.balance}')
        print(f'Account opened on {self.date_of_opening}')
        print("Thank you for banking with us!\n")
        

print("********* WELCOME TO OUR BANKING SYSTEM ************")
account_number = int(input("Enter your account number: "))
balance = float(input("Enter your initial balance: "))
date_of_opening = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
customer_name = input("Enter your name: ")

account = BankAccount(account_number, balance, date_of_opening, customer_name)

while True:
    print("Selece:\n1. To Depoit \n2. To withdraw \n3. Check balance \n4. To View Customer details \n0. To exit")
    selection = int(input("Input selection: "))
    if selection == 1:
        print("Welcome kindly input the ammount you want to deposit")
        deposit_amnt = int(input("Amount: "))
        account.Deposit(deposit_amnt)
        print(f"You have successfully deposited {deposit_amnt} and your current balance is {account.balance}\n")
    elif selection == 2:
        print("Kindly input the ammount you wish to withdraw")
        withdrawal= int(input("Amount: "))
        account.Witdraw(withdrawal)
    elif selection == 3:
        account.Check_balance()
    elif selection == 4:
        account.customer_details()
    elif selection == 0:
        print("\n***Thank you for banking with us!***")
        break
    else:
        print("Invalid selection Try again or press 0 to exit!")
