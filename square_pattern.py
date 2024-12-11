def sqaure(num):
    for i in range (num):
        for j in range(num):
            print("*", end="")
        print()

user = int(input("Enter the number of * you need to form square: "))
sqaure(user) # directly assigned the value since there's no return from our function