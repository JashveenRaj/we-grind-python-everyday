def largest(int_user):
    int_user.sort()
    return (int_user[-1])


def customer(user):
    # int_user is empty list
    int_user = []

    # "1","2","3","4","5"
    spl = user.split()

    for num_str in spl:
        # num_str = "1","2","3","4","5" --> num = 1 2 3 4 5
        num = int(num_str)
        # after iteration and appending - [1,2,3,4,5]
        int_user.append(num)

    return int_user


user = input("Enter some numbers: ")     # "1 2 3 4 5" - String
out = customer(user)
print(out)
print(largest(out))
