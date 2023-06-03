number1=float(input("Enter first number"))
number2=float(input("Enter second number"))
operation=input("Enter operation(+ or - or * or /):")

if operation=="+":
    sum1=number1+number2
    print("The sum of 2 numbers is",sum1)
elif operation=="*":
    prod=number1*number2
    print("The product is",prod)
elif operation=="/":
    div=number1/number2
    print("The quotient is",div)
elif operation=="-":
    diff=number1-number2
    print("The difference is",diff)
