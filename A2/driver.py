import Assignment2 as a2
# q1


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


# print(a2.listComprehensionOdd())
# print(a2.listComprehensionPrime())
f1 = a2.listComprehensionSum1()
# print(a2.divisibleByThree())
f2 = a2.listSum()
x = f1 == f2
print(x)

title = []
author = []
year = []
for index in range(1,11):
    title.append('Book{}'.format(index))
    author.append('Author{}'.format(index))
    year.append(2000+index)

print(title)
print(author)
print(year)