# Person
class Person:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation

    def getDigination(self):
        return self.designation

    def getname(self):
        return self.name


# Constituency
class Constituency:
    def __init__(self, name, areaInKM, MPofConstituency):
        self.name = name
        self.areaInKM = areaInKM
        self.MPofConstituency = MPofConstituency

    def getConstituencyInfo(self):
        print("Place Name : ", self.name)
        print("Area In KM :", self.areaInKM)
        print("MP of Constituency : ", self.MPofConstituency.name)

# Car
class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def getDetails(self):
        print("Car Name : ", self.name)
        print("Car Color : ", self.color)


# Driver
class Driver(Person):
    def __init__(self, name):
        super().__init__(name, "Driver")

    def getDetails(self):
        print("Driver Name : ", self.name)


# CarDriver
class CarDriver(Driver):
    def __init__(self, name, yearsOfCarDrivingExperience):
        self.yearsOfCarDrivingExperience = yearsOfCarDrivingExperience
        super().__init__(name)

    def getDetails(self):
        super().getDetails()


# Aircraft
class Aircraft:
    def __init__(self, name):
        self.name = name

    def getDetails(self):
        print("Aircraft Name : ", self.name)


# Pilot
class Pilot(Person):
    def __init__(self, name):
        super().__init__(name, "Pilot")

    def getDetails(self):
        print("Pilot Name : ", self.name)


# Aircraft Pilot
class AircraftPilot(Pilot):
    def __init__(self, name, yearsOfAircraftFlyExperience):
        self.yearsOfAircraftFlyExperience = yearsOfAircraftFlyExperience
        super().__init__(name)

    def getDetails(self):
        super().getDetails()


# MP
class MP(Person):
    def __init__(self, name, car, assignedDriver):
        super().__init__(name, "MP")
        self.car = car
        self.assignedDriver = assignedDriver
        self.spendingLimit = 100000
        self.expense = 0

    def upadteExpense(self, expense):
        self.expense += expense

    def getExpenses(self):
        return self.expense

    def getSpendingLimit(self):
        return self.spendingLimit

    def getDetails(self):
        print("MP Name : ", self.name)
        print("MP Spending : ", self.spendingLimit)
        print("Expenses : ", self.expense)
        self.car.getDetails()
        self.assignedDriver.getDetails()


# Minister
class Minister(MP):
    def __init__(self, name, car, assignedDriver):
        super().__init__(name, car, assignedDriver)
        self.designation = "Minister"
        self.spendingLimit = 1000000

    def getDetails(self):
        print("MP Name : ", self.name)
        print("spending Limit: ", self.spendingLimit)
        print("Expenses : ", self.expense)
        self.car.getDetails()
        self.assignedDriver.getDetails()

# PM
class PM(Minister):
    def __init__(self, name, car, assignedDriver, aircraft, assignedPilot):
        super().__init__(name, car, assignedDriver)
        self.designation = "Prime Minister"
        self.aircraft = aircraft
        self.assignedPilot = assignedPilot
        self.spendingLimit = 10000000

    @staticmethod
    def getPermission():
        return False

    def getDetails(self):
        print("PM Name : ", self.name)
        print("Spending Limit: ", self.spendingLimit)
        print("Expenses : ", self.expense)
        self.car.getDetails()
        self.assignedDriver.getDetails()
        self.aircraft.getDetails()
        self.assignedPilot.getDetails()

# Commisioner


class Commisioner(Person):
    def __init__(self, name):
        super().__init__(name, "Commisioner")

    def arrest(self, victim):
        if victim.getDigination() == "Prime Minister":
            print("Prime Minister can not be arrest")

        elif victim.getExpenses() > victim.getSpendingLimit():
            if victim.getDigination() == "Minister":
                if PM.getPermission():
                    print(victim.getname(), " got Arrested By", self.name)
                else:
                    print("Not get permission")

            else:
                print(victim.getname(), " got Arrested By", self.name)

        else:
            print(victim.getname(), "is not a victim")


# Indian Politics
class IndianPoliticalSystem:
    noidaConstituency = Constituency("Noida", 300, MP("Ramesh", car=Car(name="Safari", color="White"),
                                                      assignedDriver=CarDriver(name="Raj Kumar",
                                                                               yearsOfCarDrivingExperience=5)))
    ministerOfDelhi = Minister(name="Arvind Kejrival", car=Car(name="Dzire", color="Red"),
                               assignedDriver=CarDriver(name="Satyam", yearsOfCarDrivingExperience=5))
    PMOfIndia = PM(name="Narendra Modi", car=Car(name="Land Rover Range Rover HSE", color="purple"),
                   assignedDriver=CarDriver(
                       name="Vikram", yearsOfCarDrivingExperience=5),
                   aircraft=Aircraft("Rafale"),
                   assignedPilot=AircraftPilot("Abhinandan", yearsOfAircraftFlyExperience=1))
    print("-------------------------------------------------------------------")
    PMOfIndia.getDetails()
    print("-------------------------------------------------------------------")
    ministerOfDelhi.getDetails()
    print("-------------------------------------------------------------------")
    noidaConstituency.getConstituencyInfo()
    print("-------------------------------------------------------------------")

    ministerOfDelhi.upadteExpense(10000000)
    print(ministerOfDelhi.getExpenses())
    print("-------------------------------------------------------------------")
    PMOfIndia.upadteExpense(100000000)
    print(PMOfIndia.getExpenses())

    noidaConstituency.MPofConstituency.upadteExpense(1000000)

    print("-------------------------------------------------------------------")
    commisioner = Commisioner("Ramsanker")
    commisioner.arrest(PMOfIndia)
    commisioner.arrest(ministerOfDelhi)
    commisioner.arrest(noidaConstituency.MPofConstituency)
