
def prime_or_not(result):
    is_prime = True
    if(num ==1):
        print(f"{num} is not a prime number")
    elif (num>1):
        for i in range(2,num):
            if (num % i==0):
                is_prime = False
            break
        if is_prime:
            print(f"{num} is Prime number.")
        else:
            print(f"{num} is not a prime number")
    else:
        print(f"{num} is not a prime number")   

num = int(input("Enter a number: "))
result = prime_or_not(num)