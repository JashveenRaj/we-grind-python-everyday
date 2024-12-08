def prime_checker(start,end):
    primes = []
    for num in range (start, end+1):
        if num>1:
            for i in range(2,num):
                if(num%i ==0):
                    break
            else:
                primes.append(num)
    return primes

start = int(input("Enter first num from the interval: "))
end = int(input("Enter the second num from the interval: "))
result = prime_checker(start,end)
print(result)

# print(prime_checker(int(input("Enter the first number: ")), int(input("Enter the second number: "))))