from xml.dom import IndexSizeErr


class ShoppingCart:
    """ShoppingCart object used to keep track of all shopping cart and related functions.

    Raises:
        KeyError: If Item does not exist.
        IndexError: If index is out of bounds.

    Returns:
        ShoppingCart: ShoppingCart Object
    """
    FILE_NAME = './shopStock.csv'

    def __init__(self) -> None:
        """Initiatilize shopping cart object.
        """
        self.cart = [] #items user adds
        self.total = 0 #total price of items
        self.stock = {} #All stock items with price
        self.time = 0 #how long user spends shopping
        #generate shopping cart list. Normally not a good idea to have inside of object, but for the scope of the project its ok.
        self.__populateCSV__() 
        #read in the stock of the store.
        self.__inventory__()

    def __str__(self) -> str:
        """ToString method

        Returns:
            str: The shopping cart contents
        """
        output = "User shopping cart contains:"
        for item in self.cart:
            output += '\n${:6.2f}, {}'.format(self.stock[item], item)
        output += '\nTotal so far is: ${:6.2f}'.format(self.total, self.time)
        return output

    def addItem(self, item: str) -> str:
        """Add item to cart

        Args:
            item (str): The item to add

        Raises:
            KeyError: If item added does not exist in stock

        Returns:
            str: Item added.
        """
        if not item in self.stock:
            raise KeyError('Item was not found in stock')
        else:
            self.cart.append(item)
            self.total += self.stock[item]
            return 'Item was added to cart.'

    def removeItem(self, item: str) -> str:
        """Remove an item from the cart

        Args:
            item (str): Item to be removed

        Raises:
            IndexError: If quantity exceeds cart.

        Returns:
            str: Item removed.
        """
        index = [i for i, x in enumerate(self.cart) if x == item]
        length = len(index)
        if length > 1:
            amt = int(input(
                "Found {} matching items. How many would you like to remove?\n".format(length)))
            if amt > length or amt < 0:
                raise IndexError(
                    'Index was greater or than the amount of items. Please try again.')
            for i in range(amt):
                self.cart.remove(item)
                self.total -= self.stock[item]
        else:
            self.cart.remove(item)
            self.total -= self.stock[item]
        return 'Items where removed.'
    
    def checkout(self, time:float ) -> dict:
        """Checkout all items

        Args:
            time (float): The value of time

        Returns:
            dict: containing all relevant transactions
        """
        if len(self.cart) == 0:
            raise IndexSizeErr #if checkout does not exist.
        self.time = time
        # for count, item in enumerate(self.cart):
        #     output[count] = [item, self.stock[item]]
        output = {count:[item, self.stock[item]] for count, item in enumerate(self.cart)}
        output[len(output)] = ['Time spent shopping: ', '{:3.0f} seconds'.format(time)]
        return output
    
    
    def __populateCSV__(self):
        """Add hardcoded values to csv
        """
        import csv
        data = [
            ['Name', 'Price'],
            ['tomato', 2.99],
            ['carrot', 1.99],
            ['chips', 4.99],
            ['fries', 5.99]
        ]
        with open(self.FILE_NAME, 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            for item in data:
                writer.writerow(item)
        pass

    def __inventory__(self):
        """read in from inventory
        """
        import csv
        file = open(self.FILE_NAME,  encoding='UTF8')
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            sanitizedOutput = str(line).replace('[', "").replace("]", "")
            temp = sanitizedOutput.split(',')
            self.stock[temp[0].replace("'", "")] = float(
                temp[1].replace("'", ""))
        file.close()
        pass

    def checkStock(self):
        """Check the stock of the store
        """
        print(self.stock)
        pass


if __name__ == '__main__':
    cart = ShoppingCart()
    cart.addItem('Tomato')
    cart.addItem('Carrot')
    cart.addItem('Tomato')
    cart.addItem('Tomato')
    print(cart.checkout())

