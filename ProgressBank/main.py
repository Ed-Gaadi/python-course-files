
import json
import createStatementEntry
def updateFile():
    usersFile = open('users.txt', "w")
    contentString = ""
    for i in usersListConverted:
        contentString = contentString + str(i) + "\n"
    usersFile.write(contentString)
def viewAccountDetails():
    for i in userData:
        if(i=="password"):
            continue
        print(i,":",userData[i])
def deposit(user):
    amount=float(input("Enter amount:"))
    for i in usersListConverted:
        if i['userName']==user:
            i['accountBalance']=i['accountBalance']+amount
    # print(usersListConverted)
    updateFile()
    createStatementEntry.createEntry(user,amount,"Credit")
    print("Amount deposited!")
def withdraw(user):
    amount=float(input("Enter amount:"))
    if(amount>userData['accountBalance']):
        print("Not enough balance in your account")
        return
    for i in usersListConverted:
        if i['userName']==user:
            i['accountBalance']=i['accountBalance']-amount
    # print(usersListConverted)
    updateFile()
    createStatementEntry.createEntry(user, amount, "Debit")
    print("Withdraw successful")
def transfer(user):
    accountNumber=int(input("Enter account number to which you want to deposit money:"))
    amount=float(input("Enter amount you want to deposit:"))
    if (amount > userData['accountBalance']):
        print("Not enough balance in your account")
        return
    accountExists=0
    for i in usersListConverted:
        if i['accountNumber']==accountNumber:
            accountExists=1
    if(accountExists==0):
        print("This account number does not belong to a user")
        return
    for i in usersListConverted:
        if(i['userName']==user):
            i['accountBalance']=i['accountBalance']-amount
        if(i['accountNumber']==accountNumber):
            i['accountBalance']=i['accountBalance']+amount
    updateFile()
    createStatementEntry.createEntry(user, amount, "Debit")
    print("Transfer successful")

def viewAccountStatement():
    statementFile=open("accountStatement.txt")
    fileContent=statementFile.read()
    fileContentSplit=fileContent.split("\n")
    for i in fileContentSplit:
        lineSplit=i.split(" ")
        if(lineSplit[0]==userName):
            print(i)

userData={}
usersListConverted=list()
def validateUser(username,password):
    global userData
    global usersListConverted
    usersFile=open("users.txt")
    fileContent=usersFile.read()
    fileContentSplit=fileContent.split("\n")
    # print(fileContentSplit)
    for i in fileContentSplit:
        if i=="":
            continue
        stringConverted=i.replace("'","\"")
        usersListConverted.append(json.loads(stringConverted))
    userFound=0
    foundPassword=""
    for value in usersListConverted:
        if(value["userName"]==username):
            userFound=1
            foundPassword=value["password"]
            userData=value
    if userFound==0:
        print("Invalid Username")
    elif userFound==1:
        if(foundPassword==password):
            print("Login successful")
            return "success"

        else:
            print("Invalid password")

initialAccountNumber=6000000000
def getNumberOfUsers():
    usersFile=open("users.txt")
    fileContent=usersFile.read()
    fileContentSplit=fileContent.split("\n")
    numberOfUsers=len(fileContentSplit)
    return numberOfUsers

def register():
    userCount=getNumberOfUsers()
    accountNumber=initialAccountNumber+userCount
    name=input("Enter name:")
    phoneNumber=(input("Enter phone number"))
    address=input("Enter address:")
    email=input("Enter email:")
    username=input("Enter Username:")
    password=input("Enter password:")
    usersFile=open("users.txt","a")
    userData={
        "name":name,
        "phoneNumber":phoneNumber,
        "address":address,
        "email":email,
        "userName":username,
        "password":password,
        "accountNumber":accountNumber,
        "accountBalance":0
    }
    userDataConverted=str(userData)
    userDataConverted=userDataConverted+"\n"
    usersFile.write(userDataConverted)
    print("Registration Successful")

# getNumberOfUsers()
print("Welcome to Progress bank. Please choose one of the following options.")
option=input("1. Login\t2.Register")
if option=="1":
    userName=input("Enter username:")
    password=input("Enter password:")
    validateResult=validateUser(userName,password)
    if(validateResult=="success"):
        print("Select one of the following options\n1.View account details\n2.Deposit\n3.Withdraw\n4.Transfer\n5.View account statement")
        option2=input()
        if(option2=="1"):
            viewAccountDetails()
        elif option2=="2":
            deposit(userName)
        elif option2=="3":
            withdraw(userName)
        elif option2=="4":
            transfer(userName)
        elif option2=="5":
            viewAccountStatement()
        else:
            print("Invalid input")
elif option=="2":
    register()
else:
    print("Invalid input.")