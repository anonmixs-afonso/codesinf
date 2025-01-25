from account import Useraccount, Savingsaccount, Currentaccount

class Bank():
    """
    """
    accounts = [Savingsaccount(), Currentaccount()]
    def __init__(self):
        """
        """
        

    def findAccount (self, numberacc):
        """
        """
        for i in self.accounts:
            if (i.accnumber == numberacc):
                return i
        else:
            print("Account not found.")
    
class Clientservice(Bank):
    """
    """
    def __init__(self):
        """
        """
        super().__init__() #take the atrributes and methods from base class (polymorphism)
        self.test=0

    def clientService (self):
            print("Welcome to Anon's bank: ")
            numberacc = input("Type your account number: ")
            classacc = self.findAccount(int(numberacc))
            passw = input("Type your password:")
            if(classacc.validatepassw(int(passw))):
                while(True):
                    choice = input("What you wanna do?\n(1- See balance; 2- Withdraw money; 3- Deposit money; 4- Transfer money to another account; 5- Exit):\n ")
                    if ((int(choice) == 1)):
                        print(f'Your current balance is ${float(classacc.getbalance(int(passw)))}.')
                    
                    elif (int(choice) == 2):
                        value = input("How much do you wanna withdraw?: ")
                        classacc.withdraw(float(value))
                        print(f'You had {classacc.getbalance(int(passw)) + float(value)}, now you have {classacc.getbalance(int(passw))}.')

                    elif (int(choice) == 3):
                        value = input("How much do you wanna deposit?: ")
                        classacc.depositmoney(float(value))
                        print(f'You had {classacc.getbalance(int(passw)) - float(value)}, now you have {classacc.getbalance(int(passw))}.')

                    elif (int(choice) == 4):
                        depnumber = input("Type the number of the destination account: ")
                        depacc = self.findAccount(int(depnumber))
                        value = input(f'Type the value to deposit in {depacc.accowner} account: ')
                        classacc.withdraw(float(value))
                        depacc.depositmoney(float(value))
                        print(f'Now you have: ${classacc.getbalance(int(passw))}')

                    elif (int(choice) == 5):
                        break
                for i in self.accounts:
                    print(f'Name: {i.accowner};\n')
            else:
                print("Wrong password...")
            
            returnchoice = Chooseservice()
            returnchoice.macliservice()
            

class ManagerService(Bank):
    """
    """
    def __init__(self):
        """
        """
        super().__init__() #take the atrributes and methods from base class (polymorphism)
        self.__passwmanager=1234   

    def changepassw(self, newpassword):
        oldpassw = self.__passwmanager
        validation = input("Type the old password: ")
        if (int(validation) == int(oldpassw)):    
            self.__passwmanager = int(newpassword)
        else:
            print("Wrong password...")
    
    def managerService(self):
        print("Welcome to Anon's bank(Manager Division): ")
        password = input ("Type the manager password: ")
        if (int(password) == self.__passwmanager):
            while(True):
                choice = input("What do you wanna implement? (1- Change Manager Password; 2- Add Account; 3- Delete Account; 4- exit): ")


                if (int(choice) == 1):
                    newpassw = input("Type the new password: ")
                    self.changepassw(int(newpassw))
                    password = newpassw

                if (int(choice) == 2):
                    typeacc = input ("Do you wanna create current or savings account?(c/s): ")

                    if (str(typeacc) == 'c'):
                        newclient = Currentaccount()
                        name = input("Type the owner name: ")
                        number = input("Type the number of the account: ")
                        passwordacc = input("Type the password of the account: ")
                        balance = input("Type the initial balance: ")  
                        newclient.accowner = name
                        newclient.accnumber = int(number)
                        newclient.setpassword(int(passwordacc))
                        newclient._accbalance = float(balance)             
                        Bank.accounts.append(newclient)

                    elif (str(typeacc) == 's'):
                        newclient = Savingsaccount()
                        name = input("Type the owner name: ")
                        number = input("Type the number of the account: ")
                        passwordacc = input("Type the password of the account: ")
                        balance = input("Type the initial balance: ")  
                        newclient.accowner = name
                        newclient.accnumber = int(number)
                        newclient.setpassword(int(passwordacc))
                        newclient._accbalance = float(balance)             
                        Bank.accounts.append(newclient)

                    else:
                        print("Wrong Type...")
                
                if (int(choice) == 3):
                    numbertodelet = input ("Type the number of the account to be deleted: ")
                    accountdel = self.findAccount(int(numbertodelet))
                    Bank.accounts.remove(accountdel)

                if (int(choice) == 4):
                    break


        for i in self.accounts:
            print(f'Name: {i.accowner};\n')


        if (int(password) != self.__passwmanager):
            print("Wrong password...")
        
        returnchoice = Chooseservice()
        returnchoice.macliservice()

class Chooseservice(Bank):

    def macliservice(self):
        choice = input("Type the type of service you want: (manager/client): ")

        if (choice == "manager"):
            mangerservice = ManagerService()
            mangerservice.managerService()
            
        elif (choice == "client"):
            clientservice = Clientservice()
            clientservice.clientService()

        else:
            print("Wrong option (type manager or client)...")

