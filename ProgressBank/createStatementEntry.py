import datetime
def createEntry(username,amount,transactiontype):
    statementFile=open("accountStatement.txt","a")
    currentDate=datetime.datetime.now()
    currentDateConverted=str(currentDate)
    statementFile.write(username+" "+str(amount)+" "+transactiontype+" "+currentDateConverted+"\n")
