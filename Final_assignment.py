import random


class Bank:
    def __init__(self, bank_name) -> None:
        self.bank_name = bank_name
        self._users = []
        self._admins = []
        self._total_balance = 0
        self.total_loan_amount = 0
        self.loan_feature_enabled = True

    def create_user_account(self, name, email, address, account_type):
        user = User(name, email, address, account_type)
        user.author = "user"
        self._users.append(user)
        return user

    def create_admin_account(self, name, email, address, account_type):
        admin = Admin(name, email, address, account_type)
        admin.author = "admin"
        self._admins.append(admin)
        return admin

    def show_users(self):
        for user in self._users:
            print(
                f"Name: {user._name} --> Email: {user._email} --> Acc-Number: {user._account_number} --> Acc-Type: {user.account_type}"
            )


class User:
    def __init__(self, name, email, address, account_type) -> None:
        self._name = name
        self.author = None
        self._email = email
        self.address = address
        self.account_type = account_type
        self._account_number = random.randint(1000, 10000)
        self.__balance = 0
        self.loan_taken = 0
        self.transections = []

    def deposit(self, amount):
        if amount <= 0:
            print("\nInvalid Amount")
        else:
            self.__balance += amount
            bank._total_balance += amount
            self.transections.append(f"Deposited ${amount}")
            print(f"\nAmount ${amount} deposited successfully.")

    def withdraw(self, amount):
        if self.__balance == 0:
            print("\nThe bank is bankrupt")
        elif amount > self.__balance:
            print("\nWithdrawal amount exceeded.")
        else:
            self.__balance -= amount
            bank._total_balance -= amount
            self.transections.append(f"Withdrawn ${amount}")
            print(f"\nWithdrawn ${amount} successfully")

    def check_balance(self):
        print(f"\nAvailable balance: $ {self.__balance}")

    def check_transection_history(self):
        if len(self.transections) > 0:
            return self.transections
        else:
            return "\nNot transection yet\n"

    def take_loan(self, amount):
        if bank.loan_feature_enabled == False:
            print(
                "\nThe Loan Feature is OFF by the bank author. Please contact with him\n"
            )
        elif amount > 4000:
            print("\nUnable to take a loan. You can loan maximum 4000 tk\n")
        elif self.loan_taken == 2:
            print("\nYou can't take more than two loans.\n")
        elif self.loan_taken < 2:
            self.loan_taken += 1
            bank.total_loan_amount += amount
            bank._total_balance += amount
            self.__balance += amount
            self.transections.append(f"Took a loan of ${amount}")
            print(f"\nLoan of ${amount} taken successfully.\n")

    def transfer_balance(self, amount, account_email):
        isAccountExist = False

        if self.__balance == 0:
            isAccountExist = True
            print("\nThe bank is bankrupt\n")
        elif amount > self.__balance:
            isAccountExist = True
            print("\nInsufficient Balance\n")
        else:
            for user in bank._users:
                if user._email == account_email:
                    isAccountExist = True
                    user.__balance += amount
                    self.__balance -= amount
                    self.transections.append(
                        f"Trasferred $ {amount} to account number: {user._account_number}"
                    )
                    print(
                        f"{amount} tk successfully transfered to the Account number: {user._account_number}"
                    )
        if isAccountExist == False:
            print("\nAccount does not exist. Please try with a valid account\n")

    def display_account_info(self):
        print(
            f"Name: {self._name} --> Email: {self._email} --> Account Number: {self._account_number} --> Account Type: {self.account_type} --> Balance: ${self.__balance}"
        )


class Admin(User):
    def __init__(self, name, email, address, account_type) -> None:
        super().__init__(name, email, address, account_type)

    def delete_user_account(self, email):
        for account in bank._users:
            if account._email == email:
                bank._users.remove(account)
                print(
                    f"\nAccount Number: {account._account_number} is deleted successfully"
                )

    def display_all_user_accounts(self):
        print("\n -------------All User Account Info ---------------")
        if len(bank._users) == 0:
            print("No user Account Fond\n")
        else:
            for user in bank._users:
                user.display_account_info()

    def get_total_available_balance(self):
        print(f"Total Available Balance: {bank._total_balance}")

    def get_total_loan_amount(self):
        print(f"Total Loan Amount: {bank.total_loan_amount}")

    def toggle_loan_feature(self):
        if bank.loan_feature_enabled == True:
            print("\nYou successfully OFF the bank loan feature")
        else:
            print("\nYou successfully ON the bank loan feature")

        bank.loan_feature_enabled = not bank.loan_feature_enabled


# create a bank
bank = Bank("Rupali Bank Ltd")
