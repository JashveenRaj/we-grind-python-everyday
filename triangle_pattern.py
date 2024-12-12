def traingle(num):
    for i in range (num):
        for j in range (i+1):
            print("*", end=" " )
        print()

num = int(input("Enter a number: "))
traingle(num)