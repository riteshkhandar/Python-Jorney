# Atm mini project using loops
# Balance: 5000
# Enter deposit/withdraw/quit: deposit


balance = 5000
action = ""

while action != "quit":

    print(f"your balance: {balance}")
    action = input("Enter deposit/withdraw/quit: ")

    if action == "deposit":
        amount = int(input("enter amount: "))
        balance = balance + amount
        print(f"your balance is {balance}")

    elif action == "withdraw":
        withdraw = int(input("enter amount: "))
        if withdraw > balance:
            print("insufficient balance!")
        else:
            balance = balance - withdraw
            print(f"your balance is {balance}")  

    elif action == "quit":   
        print(f"final balance: {balance}")
        break