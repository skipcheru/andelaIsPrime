def prime_number():
    N = input("input start : ")
    # modify this code later today to accept start and end of range of the prime numbers needed

    for n in range(0, N):
        if n > 1:
            for i in range(2, n):
                if n % i == 0:  # loop until the number is divisible by itself only
                    break  # jump out of here
            else:
                print(n)

  #  check if number is prime number


def is_prime():
    N = input("Input a number : ")
    n = int(N)

    if n % 2 == 0 or n < 2:
        return False
    if n == 2 or n == 3:
        return True

    for i in range(3, int(n**0.5) + 1, 2):   #check for numbers > 3 only here
        if n % i == 0:
            return False

    return True

print(is_prime())