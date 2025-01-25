class Useraccount():
    """
    Class Account
    """

    def __init__(self):
        """
        Construct of the class account
        :param accnumber: number of the account
        :param accowner: the owner of the account
        :param accpassw: the password of the account
        :param accbalance: the amount of money stored in the account
        """
        self.accnumber = 112233
        self.accowner = "Jake"
        self.__accpassw = 1234
        self._accbalance = 2550

    def setpassword(self, password):
        """
        Method to the user set the password of the account
        :param setpassword: password of the user
        """
        self.__accpassw = password

    def setbalance(self, balance):
        """
        Method that sets the amount of money in the account
        :param balance: amount of money in the account
        """
        self._accbalance = balance

    def setowner(self, owner):
        """
        Method that set the owner of the account
        :param owner: owner of the account
        """
        self.accowner = owner

    def validatepassw(self, password):
        """
        """
        if (password == self.__accpassw):
            return 1
        else:
            return 0

    def getbalance(self, password):
        """
        Method that gets the balance of a account using a user password
        :param password: password of the user
        :return: balance of account
        """
        if (password == self.__accpassw):
            return self._accbalance

    def withdraw(self, value):
        if (value > 0.0):
            self._accbalance = self._accbalance - value
    
    def depositmoney(self, value):
        if (value > 0.0):
            self._accbalance = self._accbalance + value
    
class Savingsaccount(Useraccount):
    """
    Class Savings Account
    """
    def __init__(self):
        """
        Constructor of the sub class
        Construct of the class account
        :param accnumber: number of the account
        :param accowner: the owner of the account
        :param accpassw: the password of the account
        :param accbalance: the amount of money stored in the account
        """
        super().__init__() #take the atrributes and methods from base class (polymorphism)
        self.__rateofsavings = 0
    
    def rateofBank(self, rate):
        """
        Method to define the rate for savings
        param rate: percentage of saves per month
        """
        if (rate > 0):
            self.__rateofsavings = rate
     
    def savesPerMonths(self, months):
        """
        Method to show gains per months of the user savings
        :param months: amount of months that the money will stays in the bank
        """
        if (months > 0):
            value = 0
            value = self._accbalance + self._accbalance*(self.__rateofsavings)
            print(f'In the end of {months} months you will have ${value}.')

class Currentaccount(Useraccount):
    """
    Class Current Account
    """
    def __init__(self):
        """
        Constructor of the  Currentaccount class
        Construct of the class account
        :param accnumber: number of the account
        :param accowner: the owner of the account
        :param accpassw: the password of the account
        :param accbalance: the amount of money stored in the account
        """
        super().__init__() #take the atrributes and methods from base class (polymorphism)

