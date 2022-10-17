import Assignment2 as a2

# helper funcs
# q1 Check if a num is prime or not. You can add/delete values from this list to test.
primeNums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 97]
a2.prime(primeNums)
# q2 a
print('\nQ2.a\n\n',a2.listComprehensionOdd(),
      '\n=========================================================')
# q2 b
nums = [i for i in range(10, 511)]
allPrime = [i for i in nums if a2.isPrime(i)]
print('\nQ2.b\n\n', allPrime, '\n===============================================')
# q2 c
print('\nQ2.c\n\n', a2.listComprehensionSum1(),
      '\n===============================================')
# q2 d
print('\nQ2.c\n\n', a2.divisibleByThree(),
      '\n===============================================')
#q3
key, title, author, year = a2.seed(10)
a2.readingBooks(key, title, author, year)



