def calculater(num1,num2):
    
    l=['+','-','*','/','//','%','^']
    result=0


    
    print("Choose operation to be performed")
    print(l)
    calc=input()
    if calc=='+':
        result=num1+num2
    elif calc=='-':
        result=num1-num2
    elif calc=='*':
        result=num1*num2
    elif calc=='/':
        result=num1/num2
    elif calc=='//':
        result=num1//num2
    elif calc=='%':
        result=num1%num2
    elif calc=='^':
        result=pow(num1,num2)
    else:
        print("Invalid choice")
    
    ch=input("Do you want to continue the calculation:y/n")
    if ch=='y':
        ch1=input("Do you want to continue the calculation with same result as number 1:y/n")
        if ch1=='y':
            num3=float(input("Enter number"))
            calculater(result,num3)
        else:
            print(result)
            num4=float(input("Enter number"))
            num5=float(input("Enter number"))
            calculater(num4,num5)
    else:
        print("Calculation performed")
        print(result)
    

print("WELCOME TO CALCULATOR")    
num1=float(input("Enter first number"))
num2=float(input("Enter second number"))
calculater(num1,num2)

