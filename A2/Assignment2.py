
def isPrime(number: int) -> bool:
    """Q1. Will check number to make sure it is prime.

    Args:
        number (int): Checked prime

    Returns:
        bool: T/F depening on if the provided num is prime.
    """
    if not isinstance(number, int):
        raise TypeError

    output = (number % 1 == 0 and number % number == 0)
    for x in range(2, number):
        if number % x == 0:
            return False
    print(output)
    return output


def listComprehensionOdd(x=9, y=511, z=2) -> list[int]:
    """Q2.a List of odd integers between 8-512

    Args:
        x (int, optional): Index to start at. Defaults to 9.
        y (int, optional): Index to end before. Defaults to 511.
        z (int, optional): Offset index. Defaults to 2.

    Returns:
        list[int]: List of odd numbers.
    """
    return [i for i in range(x, y, z)]


def listComprehensionPrime(x=10, y=511, z=2) -> list[int]:
    """Q2.b List of all comprehensions checking for prime nums

    Args:
        x (int, optional): Index to start at. Defaults to 9.
        y (int, optional): Index to end before. Defaults to 511.
        z (int, optional): Offset index. Defaults to 2.

    Returns:
        list[int]: List of prime numbers.
    """
    return [i for i in range(x, y, z) if isPrime(i)]


def listComprehensionSum1(x=10, y=511, z=2) -> list[int]:
    """Q3.c.1 Pretty complicated comprehension where i turn the values into tuples. Iterate through each tuple, look for the 0th one and add sum of tuples previously.

    Args:
        x (int, optional): Index to start at. Defaults to 10.
        y (int, optional): Index to end before. Defaults to 511.
        z (int, optional): Offset index. Defaults to 2.

    Returns:
        list[int]: A list of the sum of numbers.
    """
    output = []
    sum = -1
    test = [p for o in (range(x, y, z)) for p in enumerate(str(o))]
    #n*('key', 'val')
    for key, val in test:
        # each time we loop back our tuple will start at 0. Take sum
        if(sum == -1):
            # first run
            sum = int(val)
        elif(key == 0):
            output.append(sum)
            # reset sum for next iteration
            sum = int(val)
        else:
            sum += int(val)
    # add final index for last val
    output.append(sum)
    return output


