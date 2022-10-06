def isPrime(number) -> bool:
    """"""
    output = (number % 1 == 0 and number % number == 0)
    for x in range(2, number):
        if number % x == 0:
            return False
    return output
