import datetime
try:
    number1=int(input("Enter first number:"))
    x=sldkfj
    number2=int(input("Enter second number:"))
    print(number1/number2)
except Exception as e:
    file=open("erroHandlingLog.txt","a")
    file.write("\n"+str(e)+str(datetime.datetime.now()))