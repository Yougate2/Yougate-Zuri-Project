import random
database = {
    4307925082:["Yusuf", "Babs", "yusu@gmail.com", "ypass", 5000]
}

def init():
    print("Welcome to BankZi")
    haveAcoount = int(input("Do you have an account? 1(LOGIN) 2(REGISTER) \n"))
    if (haveAcoount == 1):
        login()
    elif (haveAcoount == 2):
        register()
    else:
        print("Invalid Option Selected. Please Try Again")
        init()


def register():
    print("Join Us Today")
    Email = input("Enter A Valid Email Address \n")
    firstName = input("Enter First Name \n")
    lastName = input("Enter Your Last Name \n")
    Password = input("Enter A Secured Pasword \n")

    accountNumber = generateAccountNumber()
    database[accountNumber] = [firstName, lastName, Email, Password]
    print("Your Account Was Created Successfully")
    print("**********************")
    print("Your Account Number is %d" % accountNumber)
    print("Kindly Keep It Safe")
    print("**********************")
    login()


def login():
    print("Login")
    accFromUser = int(input("Enter Your Account Number \n"))
    password = input("Enter Your Password \n")
    for accountNumber, userDetails in database.items():
           if(accountNumber == accFromUser):
            if(userDetails[3] == password):
                bankOperation(userDetails)

            else:
                print("Invalid Account or Password")
                login()


def bankOperation(user):
    print("Welcome %s %s" % (user[0], user[1]))
    print("1. Deposit Money")
    print("2. Withdraw Money")
    print("3. Logout")
    print("4. Exit")

    selectedOption = int(input("Enter Number to Start Operation. \n"))
    if (selectedOption == 1):
        depositOperation()
    elif (selectedOption == 2):
        withdrawOperation()
    elif (selectedOption == 3):
        logout()
    elif (selectedOption == 4):
        exit()
    else:
        print ("Invalid Option Selected. Try Again")
        bankOperation(user)
    



def depositOperation():
    for getCurrentBalance, userDetails in database.items():
        print("Your current Balance is %d" % userDetails[4])
        depositAmount = int(input("Enter Amount To Deposit \n"))
        print("**********************")
        print("You have Deposited:")
        print(depositAmount)
        print("**********************")
        print("New Balance:")
        print(depositAmount + userDetails[4])
        print("**********************")
        print("Do You Want To Perform Another Transaction")
        print("1. YES")
        print("2. NO (Logout)")
        anotherTrans = int(input("YES OR NO\n"))
        if (anotherTrans == 1):
            bankOperation(user)
        elif (anotherTrans == 2):
            logout()
        

def withdrawOperation():
    for getCurrentBalance, userDetails in database.items():
        print("Your current Balance is %d" % userDetails[4])
        withdrawAmount = int(input("Enter Amount To Withdraw \n"))
        if (withdrawAmount <= userDetails[4]):
            print("Take Your Cash")
            print("**********************")
            print("New Balance is")
            print(userDetails[4] - withdrawAmount)
            print("**********************")
            print("Do You Want To Perform Another Transaction")
            print("1. YES")
            print("2. NO (Logout)")
            anotherTrans = int(input("YES OR NO \n"))
            if (anotherTrans == 1):
                bankOperation(user)
            elif (anotherTrans == 2):
                logout()

        else:
            print("Insufficient Funds. Please Try Again")
            withdrawOperation()

def getCurrentBalance(userDetails):
    return userDetails[4]


def logout():
    print("**********************")
    print("You're Logged Out. Login Again")
    print("**********************")
    login()

def exit():
    init()

def generateAccountNumber():
    return random.randrange(0000000000, 9999999999)







init()