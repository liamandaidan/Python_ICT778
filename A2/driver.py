import Assignment2 as a2

primeNums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 97]
flag = True
for x in range(len(primeNums)):
    if not a2.isPrime(primeNums[x]):
        print('not prime num: {}'.format(primeNums[x]))
        flag = False
        break
if flag:
    print('All nums provided are prime!')
