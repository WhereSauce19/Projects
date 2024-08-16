import useful_func as func

accounts = {}
is_running = True
# Reading accounts from text file.
with open("Accounts.txt", 'r') as file:
    for line in file.readlines():
        line = line.strip()
        name, bal = line.split('|')
        bal = float(bal)
        # Adding name and balance to a Dictionary.
        accounts[name] = bal
    
while is_running:
    # User inputs username.
    username = input("Enter username: ")
    if not(username in accounts.keys()):
        print("User does not exist.\n")
        continue
    balance = accounts[username]
    # Printing options.
    print("1.View account balance.\n" + "2.Deposit money.\n" + "3.Withdraw money.\n")
    match input("What would you like to do?: "):
        # Checking account balance.
        case '1':
            print(f"Your account balance is {balance}\n")
        # Depositing money.
        case '2':
            deposit = input("How much would you like to deposit?: ")
            print()
            if not(func.is_number(deposit)):
                print("Invalid amount.\n")
                continue
            deposit = float(deposit)
            accounts[username] = balance + deposit
        # Withdrawing money.
        case '3':
            withdraw = input("How much would you like to withdraw?: ")
            print()
            if not(func.is_number(withdraw)):
                print("Invalid amount.\n")
                continue
            withdraw = float(withdraw)
            # Checking if amount can be withdrawn.
            if (balance - withdraw) < 0:
                print("Your account balance is too low.\n")
                continue
            accounts[username] = balance - withdraw
        # If option isn't valid.
        case _:
            print("Invalid choice.\n")

    # Rewriting text file with new balances.
    with open("Accounts.txt", 'w') as file:
        for name, bal in accounts.items():
            file.write(f"{name}|{bal}\n")
    
    # Checking if user wants to run file again.
    is_running = input("Go again(Y/N)?: ").lower()
    print()
    if is_running == 'y':
        is_running = True
    else:
        is_running = False