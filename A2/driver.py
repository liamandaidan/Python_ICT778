import Assignment2 as a2
def prime():
    primeNums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 97]
    flag = True
    for x in range(len(primeNums)):
        if not a2.isPrime(primeNums[x]):
            print('not prime num: {}'.format(primeNums[x]))
            flag = False
            break
    if flag:
        print('All nums provided are prime!')
        
def listSum(x=10, y=511, z=2) -> list[int]:
    """generate sum from for loops. Used to check the list comprehension above.

    Args:
        x (int, optional): Index to start at. Defaults to 10.
        y (int, optional): Index to end before. Defaults to 511.
        z (int, optional): Offset index. Defaults to 2.

    Returns:
        list[int]: output of all sums
    """
    output = []
    sum = 0
    for i in (range(x, y, z)):
        for p in str(i):
            sum += int(p)
        output.append(sum)
        sum = 0
    return output
        
#print(a2.listComprehensionOdd())
#print(a2.listComprehensionPrime())
f1 = a2.listComprehensionSum1()
print('==================')
f2 = listSum()
print(f1==f2)

