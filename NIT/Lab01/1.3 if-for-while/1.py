account = str(input("Enter your account name: "))
trueAccount = "zhou"
turePassword = 123
if account == trueAccount:
    password = int(input("Enter your password: "))
    if password == turePassword:
        print("Congratulations!Log in successfully!")
    elif password != turePassword:
        print("Wrong password")
else:
    print("Wrong account")
