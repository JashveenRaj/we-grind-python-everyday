def triangle_without_zero(num):
    for i in range(num):
        for j in range(num-i):
            if(j==0):
                continue
            else:
                print( j ,end=" ")
        print()

num = int(input("Enter a number: "))
triangle_without_zero(num)
