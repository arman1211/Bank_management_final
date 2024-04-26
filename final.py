class Bank:
    def __init__(self) -> None:
        self.users = {}
        self.loan_allow = True
        self.is_bankrupt = False
        self.total_balance = 0
        self.total_loan = 0

class Admin(Bank):
    def __init__(self) -> None:
        super().__init__()
    def create_account(self,name,email,address,account_type):
        account_no = len(self.users)+1
        user_acount = User(name,email,address,account_type)
        self.users[account_no] = user_acount
    def delete_account(self,account_no):
        if account_no in self.users:
            del self.users[account_no]
        else:
            print(f"Sorry, account no {account_no} does not exists")
    def account_list(self):
        if len(self.users>0):
            print(f'account no\tname\temail\taddress\taccount type')
            for acc_no,user in self.users.items():
                print(f'{acc_no}\t{user.name}\t{user.email}\t{user.address}\t{user.account_type}')
        else:
            print('Sorry, no user exists')
    def total_bank_balance(self):
        print(self.total_balance)
    def total_loan_amount(self):
        print(self.total_loan)
    def change_loan_feature(self):
        if self.loan_allow:
            self.loan_allow = False
            print("Loan feature is now turned off")
        else:
            self.loan_allow = True
            print("loan feature is now turned on")
    def change_bankrupt(self):
        if self.is_bankrupt:
            self.is_bankrupt = False
            print("Bank is ok")
        else:
            self.is_bankrupt = True
            print("Bank is bankrupt")


class User(Bank):
    def __init__(self,name,email,address,account_type) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.balance = 0
        self.loan = 0
        self.loan_cnt = 0
        self.transaction_history = {}
        super().__init__()

    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            transaction_id = len(self.transaction_history)+101
            self.transaction_history[transaction_id] = ["deposit",amount]
            print(f"Succesfully deposited {amount} tk")
        else:
            print("Sorry, the amount can't be negative")

    def withdraw(self,amount):
        if self.is_bankrupt:
            print("Sorry, Your bank is bankrupt")
        else:
            if 0< amount< self.balance:
                self.balance -= amount
                transaction_id = len(self.transaction_history)+101
                self.transaction_history[transaction_id] = ["withdraw",amount]
                print(f"Succesfully withdrawed {amount} tk")
            else:
                print("Withdrawl amount exceded")

    def check_balance(self):
        print(f"Your available balance is {self.balance + self.loan}")

    def check_transaction_history(self):
        if len(self.transaction_history)>0:
            print('--------------------------------------------------')
            print("Transaction Id\tTransaction Type\tAmount")
            print('--------------------------------------------------')
            for t_id,history in self.transaction_history.items():
                print(f'{t_id}\t\t{history[0]}\t\t\t{history[1]}')
        else:
            print("No transaction history available")
    def take_loan(self,amount):
        if self.loan_cnt <2 and self.loan_allow:
            self.loan += amount
            self.loan_cnt += 1
            transaction_id = len(self.transaction_history)+101
            self.transaction_history[transaction_id] = ["loan",amount]
            print(f'Succesfully taken loan amount {amount}')
        elif self.loan>=2:
            print("Maximul loan limit exceeded")
        elif self.loan_allow == False:
            print("Sorry, You  do not have permission to take loan")
        else:
            print("Something went wrong")
    def transfer_money(self,account_no,amount):
        if account_no in self.users:
            if amount < self.balance:
                self.users[account_no].balance += amount
                self.balance -= amount
                transaction_id = len(self.transaction_history)+101
                self.transaction_history[transaction_id] = ["transfer",amount]

                transaction_id = len(self.users[account_no].transaction_history)+101
                self.users[account_no].transaction_history[transaction_id] = ["recieved",amount]
            else:
                print("Insufficient balance")
        else:
            print("Sorry,account does not exists")


admin = Admin()

user1 = User("Arman","sh@gmail.com","ctg","savings")
user2 = User("raihan","sh@gmail.com","ctg","savings")
user1.deposit(50000)
user1.withdraw(2000)
user2.deposit(20000)
user1.take_loan(6000)
user1.transfer_money(2,4000)
user1.check_transaction_history()  
user2.check_transaction_history()  
user1.check_balance() 


        