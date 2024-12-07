def want_to_use (use):
    if(use.lower() == "yes"):
        operation = input("What operation do you want to perform? : + (or) - (or) / (or) *  ")
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))
        return num1,num2,operation
    else:
        pass

def choose_op(operation,num1,num2):
    if(operation == "+"):
        return num1+num2
    elif(operation == "-"):
        return num1-num2
    elif(operation == "/"):
        return num1/num2
    elif(operation == "*"):
        return num1*num2
    else:
        print ("Enter a valid operation method")

use = input("Do you want to use the calci ? ")
use_inp = want_to_use(use) 
if use_inp:
    num1, num2, operation = use_inp 
    result = choose_op(operation, num1, num2)
    print(result)
