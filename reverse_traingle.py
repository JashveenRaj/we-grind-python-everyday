def reverse_traingle(num):
    for i in range(num):
        for j in range(num-i):
            print("*" , end=" ")
        print()

num = int(input("Enter a number: "))
reverse_traingle(num)