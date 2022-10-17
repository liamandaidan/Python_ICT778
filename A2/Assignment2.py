
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


def listComprehensionSum1(x=9, y=512) -> list[int]:
    """Q3.c. Pretty complicated comprehension where i turn the values into tuples. Iterate through each tuple, 
        look for the 0th one and add sum of tuples previously.
        It could probably be done better, but I couldnt find another solution at the moment.
        Please check function ListSum as that is the way it should be done lol.
    Args:
        x (int, optional): Index to start at. Defaults to 10.
        y (int, optional): Index to end before. Defaults to 511.
        z (int, optional): Offset index. Defaults to 2.

    Returns:
        list[int]: A list of the sum of numbers.
    """
    output = []
    sum = -1 #set first value to -1 to trigger first if in for loop.
    test = [p for o in (range(x, y)) for p in enumerate(str(o))]
    #Example of our values. n*('key', 'val')
    for key, val in test:
        # each time we loop back our tuple will start at 0. Take sum
        if(sum == -1):
            # first run
            sum = int(val)
        elif(key == 0): #if key is 0, that means it is a new number. Therfore take previous values.
            output.append(sum)
            # reset sum for next iteration
            sum = int(val)
        else:
            sum += int(val)
    # add final index for last val
    output.append(sum)

    return output

def listSum(x=9, y=512) -> list[int]:
    """Generate sum from for loops. Used to check the list comprehension above.

    Args:
        x (int, optional): Index to start at. Defaults to 10.
        y (int, optional): Index to end before. Defaults to 511.
        z (int, optional): Offset index. Defaults to 2.

    Returns:
        list[int]: output of all sums
    """
    output = []
    for i in (range(x, y)):#get first integer eg -> 12
        s = [] #Store one iteration of integer values eg -> [1,2]
        for p in str(i):
            s.append(int(p)) 
        output.append(sum(s)) #add our values to output eg -> 3
    return output

def divisibleByThree(x=9, y=512, z=3) -> list[int]:
    """Q2.d Check a list of numbers and deterimine if it is divisable by z.

    Args:
        x (int, optional): Start value. Defaults to 9.
        y (int, optional): End value. Defaults to 512.
        z (int, optional): Is divisible by. Defaults to 3.

    Returns:
        list[int]: A list of ints divisible by z.
    """
    return [i for i in range(x, y) if i % z == 0]

def readingBooks(titleList, authorList, yearList):
    
    pass