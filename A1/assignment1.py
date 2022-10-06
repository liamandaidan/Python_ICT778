# constants
ENCODING = {
    '8': "utf-8",
    '16': "utf-16",
    '32': "utf-32"
}
FILE_NAME = {
    'book': 'book.txt',
    'dev': 'dev.txt'
}


def sumOfMultiples(x, y) -> int:
    """**Q1**Get the sum of all multiples passed in.
    Args:
        x (int): First number
        y (int): Second number

    Returns:
        int: Total sum
    """
    sum = 0
    for i in range(1, 4097):
        if(i % x == 0 or i % y == 0):
            sum += i
    return sum


def readSecondWord(filename=FILE_NAME.get('book')) -> str:
    """**Q2.A**Used to read every second word and add to a string.

    Args:
    -------
    filename := the file passed in

    Returns:
    -------
    secondWords := every second word passed in.
    """
    words = readFile(filename)
    secondWords = []
    for second in words[::2]:
        # I added the ' ' for readability of output. Can cut it.
        secondWords.append(second + ' ')
    return secondWords


def findWords(filename=FILE_NAME.get('book'), letter='f') -> str:
    """**Q2.B**Find words thats begin with the letter param passed in.

    Args:
        filename (str, optional): Name of file to be read. Defaults to 'book.txt'.
        letter (str, optional): Letter used in search. Defaults to 'f'.

    Returns:
        str: All words in str.
    """
    letter = letter.lower()
    words = [word.lower() for word in readFile(filename)]
    # Wrote findwords a second way
    # save our output as a list, add ' ' for readability..
    output = [word+' ' for word in words if letter in word[0]]
    # return string using join
    return ''.join(output)


def reverseWords(filename=FILE_NAME.get('book')) -> str:
    """Reverse words, but keep their position.

    Args:
        filename (str, optional): filename. Defaults to FILE_NAME.get('book').

    Returns:
        str: Output str
    """
    words = readFile(filename)
    output = [''.join(list(word)[::-1])+' ' for word in words]
    return ''.join(output)


def userApplication():
    """User application front
    """
    while True:
        print('==================\nPlease enter an integer option for the action you wish to preform. \n\n 1. Sum of multiples. \n' +
              ' 2. Find the second word from file. \n 3. Find words that start with a letter. ' +
              '\n 4. Reverse words. \n 5. Exit.\n==================\n ')
        inp = int(input('Integer: '))

        match inp:
            case 1:
                print('Total sum is: {}'.format(
                    sumOfMultiples(3, 7)))
            case 2:
                secondWord = readSecondWord()
                show = int(input(
                    "How many words should i display? From - 1-{}, for all type 0.\n".format(len(secondWord))))
                if show < 1 or show > len(secondWord):
                    raise('Invalid number choice, please try again.')
                output = ''
                for x in range(show):
                    output += secondWord[x]
                print(output)
            case 3:
                lett = input(
                    "Please enter a letter to search for words with that key.\n")
                print(findWords(letter=lett))
            case 4:
                print(reverseWords())
            case 5:
                break
            case default:
                print('Invalid input try again: '+inp)
                break
        if(inp == 5):
            break


# Helper functions *************


def readFile(filename=FILE_NAME.get('book'), encoder=ENCODING.get('8')) -> list:
    """Read file, return list of words.

    Args:
        filename (str, optional): filename. Defaults to 'book.txt'.
        encoder (str, optional): encoder mode. Defaults to ENCODING.get('8').

    Returns:
        list: All words split by space
    """
    words = []
    with open(filename, encoding=encoder) as file:
        for line in file:
            words += line.split()
    return words
