def prime_numbers():
    number = input("input range: ")
    number_range = int(number)
    for number in range(0, number_range):
        if is_prime(number):
            print(number)


def is_prime(number):

    if number % 2 == 0 and number is not 2:
        return False
    if number < 2:
        return False
    if number == 2 or number == 3:
        return True

    for i in range(3, int(number**0.5) + 1, 2):  # check for numbers > 3 only here
        if number % i == 0:
            return False

    return True

prime_numbers()