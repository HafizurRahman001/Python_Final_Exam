from Final_assignment import bank


def main():
    currentUser = None

    while True:
        if currentUser == None:
            print("\nNo user logged in !")
            ch = input("\nRegister/Login (R/L) : ")

            if ch == "R":
                print("\nChoose Your Options: ")
                print("1. Resister as Admin")
                print("2. Resister as User")

                ch = int(input("Your Option: "))

                if ch == 2:
                    name = input("Your Name: ")
                    email = input("Enter Email: ")
                    address = input("Enter Address: ")
                    account_type = input("Saving account or Current account (S/C): ")
                    if account_type == "S":
                        currentUser = bank.create_user_account(
                            name, email, address, "saving"
                        )
                    else:
                        currentUser = bank.create_user_account(
                            name, email, address, "current"
                        )
                if ch == 1:
                    name = input("Your Name: ")
                    email = input("Enter Email: ")
                    address = input("Enter Address: ")
                    account_type = input("Saving account or Current account (S/C): ")
                    if account_type == "S":
                        currentUser = bank.create_admin_account(
                            name, email, address, "saving"
                        )
                    else:
                        currentUser = bank.create_admin_account(
                            name, email, address, "current"
                        )
            else:
                print("\nYour Options:")
                print("1. LogIn as Admin")
                print("2. LogIn as User")

                ch = int(input("Your Option: "))

                if ch == 2:
                    email = input("Your Email: ")
                    for account in bank._users:
                        if account._email == email:
                            currentUser = account
                            break
                else:
                    email = input("Your Eamil: ")
                    for account in bank._admins:
                        if account._email == email:
                            currentUser = account
                            break

        elif currentUser.author == "user":
            print(f"\nWelcome {currentUser._name} !\n")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Available balance")
            print("4. Transection history")
            print("5. Take a loan from bank")
            print("6. Transfer balance")
            print("7. Logout")
            # print("8. show all users\n")

            ch = int(input("Enter your option: "))

            if ch == 1:
                amount = int(input("Amount: "))
                currentUser.withdraw(amount)
            elif ch == 2:
                amount = int(input("Amount: "))
                currentUser.deposit(amount)
            elif ch == 3:
                currentUser.check_balance()
            elif ch == 4:
                print("----------Your Transection History -------------")
                print(currentUser.check_transection_history())
            elif ch == 5:
                amount = int(input("Amount: "))
                currentUser.take_loan(amount)
            elif ch == 6:
                amount = int(input("Amount: "))
                email = input("Email of account: ")
                currentUser.transfer_balance(amount, email)
            elif ch == 7:
                currentUser = None
            # elif ch == 8:
            #     bank.show_users()

        elif currentUser.author == "admin":
            print(f"\nWelcome {currentUser._name} !")
            print("1. Create an account for user")
            print("2. Delete user account")
            print("3. All user account list")
            print("4. Total available balance")
            print("5. Total loan amount")
            print("6. On/Off loan feature")
            print("7. Logout")

            ch = int(input("Your Option: "))

            if ch == 1:
                name = input("User Name: ")
                email = input("User Email: ")
                address = input("User Address: ")
                account_type = input("Saving account or Current account (S/C): ")
                if account_type == "S":
                    bank.create_user_account(name, email, address, "saving")
                else:
                    bank.create_user_account(name, email, address, "current")

            if ch == 2:
                email = input("Enter user email: ")
                currentUser.delete_user_account(email)
            if ch == 3:
                currentUser.display_all_user_accounts()
            if ch == 4:
                currentUser.get_total_available_balance()
            if ch == 5:
                currentUser.get_total_loan_amount()
            if ch == 6:
                currentUser.toggle_loan_feature()
            if ch == 7:
                currentUser = None


if __name__ == "__main__":
    main()
