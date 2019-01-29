class Car():
    __make = None
    __model = None
    __year = None
    __color = None
    __consumption = None
    __tank_size = None
    __type = None
    __mileage = None
    __fuel = None
    __drivingLog = None
    __gasAddedLog = None
    __gasConsumedLog = None
    #__price = None


    def __init__(self, make, model, year, color, consumption, tank_size, mileage):
        self.__make = make; 
        self.__model = model
        self.__year = year
        self.__color = color
        self.__consumption = consumption
        self.__tank_size = tank_size
        self.__type = type 
        self.__mileage = mileage
        self.__fuel = 0
        self.__drivingLog = []
        self.__gasAddedLog = []
        self.__gasConsumedLog = []
        
    def print(self):
        print(self.__make + " " + self.__model + " " + str(self.__mileage) + " " + str(self.__fuel))

    def Drive(self, miles): 
        if (miles < 0):
            print("Exiting due to negative miles.")
            return

        if ( not isinstance(miles, float) and not isinstance(miles, int)):
            print("Miles is not a float")
            return
        
        gasNeeded = miles/self.__consumption

         
        if (self.__fuel - gasNeeded < 0):
            print("Sorry, you don't have enough gas for the trip!")
        else:
            self.__fuel = self.__fuel - gasNeeded
            self.__mileage = self.__mileage + miles
            self.__drivingLog.append(miles)
            self.__gasConsumedLog.append(gasNeeded)


    def fuel(self, amount):
        if (amount < 0):
            print("Negative amount of fuel")
            return

        if (not isinstance(amount, float) and not isinstance(amount, int)):
            print("Amount is not a float/integer.")
            return 
    
        if (( self.__fuel + amount) > self.__tank_size):
            print("You are adding too much gas")
        else:
            self.__fuel = self.__fuel + amount
            self.__gasAddedLog.append(amount)

    def getDriversLog(self):
        return self.__drivingLog.copy()
    
    def getGasAddedLog(self):
        return self.__gasAddedLog.copy()

    def getGasConsumedLog(self):
        return self.__gasConsumedLog.copy()
    
    def getTotalGasAdded(self):
        #returns the total amount of gass added
        return sum(self.__gasAddedLog.copy())

    def getTotalGasConsumed(self):
        #returns the total gas consumed.
        return sum(self.__gasConsumedLog.copy())
    
    def getTotalMoneySpent(self, price):
        #returns the total amount of money spent on gas.
        if (price < 0):
            print("Not a valid Price")
            return
        if (not isinstance(price, float) and not isinstance(price, int)):
            print("Not a valid Price")
            return
        return round((price * (sum(self.__gasAddedLog.copy()))))
#####
from Car import Car 
