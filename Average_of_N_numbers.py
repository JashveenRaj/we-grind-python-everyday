def user_num(counts):
    numbers = []
    for count in range (counts):
        nums = int(input("Enter a number: "))
        numbers.append(nums)
    return numbers


def add_vals(numbers):
    sum=0
    for number in numbers:
        sum+=number
    return sum/user_input

user_input = int(input("How many numbers do you want to find avg for? :  "))
counts = user_num(user_input)
answer = add_vals(counts)
print(answer)