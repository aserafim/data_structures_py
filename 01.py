class CreditCard:

    """ A consumer credit card"""

    def __init__(self, customer, bank, account, limit):

        """Create a new credit card instance

        The initial balance is zero.
        customer the name of the customer (e.g.,'John Bowman')
        bank     the name of the bank (e.g., 'Banco do Brasil')
        acount   then account identifier (e.g., '5391 0375 9387 5309')
        limit    credit limit (measured in reais)
        """
    
        self._customer = customer

        self._bank = bank

        self._account = account

        self._limit = limit

        self._balance = 0       

    def get_customer(self):

        """Return name of the customer"""

        return self._customer

    def get_bank(self):

        """Return the name of the bank"""

        return self._bank

    def get_account(self):

        """Return the account identifier"""

        return self._account
   
    def get_limit(self):

        """Return limit of the account"""

        return self._limit
   
    def get_balance(self):

        """Return balance of the account"""

        return self._balance   

    def charge(self, price):

        """Charge given price to the card, assuming sufficient credit limit.

        Return True if charge was processed; False if charge was denied.

        """
       
        if price + self._balance > self._limit:

            return False

        else:

            self._balance += price

            return True
   
    def make_payment(self, amount):

        """Process customer payment that reduces balance"""

        self._balance -= amount

if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard('John Bowman', 'California Savings', '5391 0375 9387 5309', 2500))
    wallet.append(CreditCard('Peter Sawyer', 'California Savings', '5391 0375 9355 0048', 3700))
    wallet.append(CreditCard('Mary Bowman', 'California Savings', '5391 7589 4577 5309', 1000))

    for value in range(1,17):
        wallet[0].charge(value)
        wallet[1].charge(value * 2)
        wallet[2].charge(value * 3)

    for customer in range(3):
        print('Customer: ', wallet[customer].get_customer())
        print('Bank: ', wallet[customer].get_bank())
        print('Account: ', wallet[customer].get_account())
        print('Limit: ', wallet[customer].get_limit())
        print('Balance: ', wallet[customer].get_ballance())

        while wallet[customer].get_balance() > 100:
            wallet[customer].make_payment(100)
            print('New ballance: ', wallet[customer].get_ballance())
            print()