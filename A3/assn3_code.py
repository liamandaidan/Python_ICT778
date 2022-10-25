from xml.dom import IndexSizeErr
import requests

def do_everything(url):
    """ This function uses the Wikipedia API to search for articles 
        containing the word 'Python' in their title.

        It returns the matching article titles and the total
        number of matching articles.

        args:
        -----
        url: str
            valid search string for the Wikipedia API

        returns:
        --------
        total_matches, no_equals: tuple
            total number of matches, matching article titles
    """

    # get Wikipedia articles with Python in the title as a dictionary
    response = requests.get(url=url).json()
    #print(response) # uncomment this line to see the data that we're dealing with

    # get the key corresponding to the actual results
    key = list(response['query']['pages'].keys())[0]
    # get the returned text from the Wikipedia search
    text = response['query']['pages'][key]['extract']
    # split up the text by the \n character
    split_text = text.split('\n')

    # remove any empty strings from the split text
    no_empty = [item for item in split_text if item]

    # remove any strings that begin with the '=' character (topic headings)
    no_equals = [item for item in no_empty if not item[0] == '=']

    # remove the first element of no_equals, since it doesn't add anything
    no_equals.pop(0)

    # finally, count the number of possible articles
    total_matches = len(no_equals)

    # return the total number of matches and the matching titles
    return total_matches, no_equals

def getExtractFromUrl(url: str) -> str:
    """Request body from get request.

    Args:
        url (str): Url to be passed in

    Returns:
        str: response body
    """
    response = requests.get(url=url).json() #get request store into json format
    return response['query']['pages'][list(response['query']['pages'].keys())[0]]['extract'] #return extract from json
def formatResponse(response: str):
    """Format response to return content length along with queries

    Args:
        response (str): The non-formated string text

    Returns:
        int: length of matches
        list: all matches
    """
    matches = [item for item in response.split('\n')[1:] if item and '=' not in item] #return only title, and text.
    return len(matches), matches


def application():
    """Used to run the application interface.
    """
    while True:
        print('==================\nWelcome to the menu, enter an integer for your option. \n\n 1. Wikipedia articles. \n' +
              ' 2. Shopping Cart.\n 3. Exit.\n==================\n ')
        try:
            inp = int(input('Integer: '))     
            match inp:
                case 1:
                    wikiListener()
                case 2:
                    cartListener()
                case 3:
                    break 
        except ValueError:
              print('Invalid input try again.')    
    pass

#Helper functions
def wikiListener():
    """Wiki controller.
    """
    url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&titles=Python&explaintext=true&format=json'
    response = getExtractFromUrl(url)
    print(formatResponse(response))
    pass

def cartListener():
    """Shopping cart controller
    """
    import time
    import ShoppingCart as cart
    
    start_time = time.time()
    userCart = cart.ShoppingCart()
    while True:
        print('==================\nWelcome to the store. Below are your options. \n\n1. View inventory. \n' +
              '2. Add item.\n3. Remove item.\n4. Check your cart.\n5. Checkout your cart. \n6. Exit.\n==================\n ')
        try:    
            inp = int(input('Integer: '))       
            
            match inp:
                case 1:
                    userCart.checkStock()
                case 2:
                    try:
                        print(userCart.addItem(input('The item you wish to add is: ').lower()))
                    except:
                        print("Item was not found in stock. Please try again.")
                case 3:
                    try:
                        print(userCart.removeItem(input("What item do you wish to remove: ").lower()))
                    except IndexError: 
                        print('Index was greater than the amount of items. Please try again.')
                    except:
                        print('Item was not found. Please try again.')
                case 4:
                    print(userCart)
                case 5:          
                    try:
                        finTime = time.time() - start_time
                        checkout = userCart.checkout(finTime)
                        print("Thanks for shopping with us, your items are as followed\n{}".format(checkout))
                        break
                    except IndexSizeErr:
                        print('Nothing to checkout! Please add some items or exit.')
                case 6: 
                    break
        except ValueError:
            print('Invalid input try again.')    
    pass

if __name__ == '__main__':
    
    url = 'https://en.wikipedia.org/w/api.php?action=query&prop=extracts&titles=Python&explaintext=true&format=json'
    #matches = do_everything(url)
    response = getExtractFromUrl(url)
    print(formatResponse(response))
