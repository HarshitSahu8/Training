from abc import ABC, abstractclassmethod
'''
person object->vehical implement
call: person(vehical obj)
'''
class Vehical(ABC):
    def __init__(self,vBrand,vType,vModel,vColor):
        self.vBrand=vBrand
        self.vModel=vModel
        self.vType=vType
        self.vColor=vColor
    def display_info(self):
        print('Vehical Brand: {}\nVehical Type: {}\nVehical Model: {}\nVehical Color: {}\n--------'.format(self.vBrand,self.vType,self.vModel,self.vColor))
        


class Car(Vehical):
    def __init__(self, vBrand, vType, vModel, vColor):
        super().__init__(vBrand, vType, vModel, vColor)
        self.vType='Four Wheeler'
    def display_info(self):
        return super().display_info(self)
        
class Bike(Vehical):
    def __init__(self, vBrand, vType, vModel, vColor):
        super().__init__(vBrand, vType, vModel, vColor)
        self.vType='Two Wheeler'
    def display_info(self):
        return super().display_info()

class Person:
    def __init__(self, name, obj):
        self.name = name
        self.obj=obj.copy()
    def get_info(self):
        print('Person Name:', self.name)
        for i in obj:
            Vehical.display_info(i)

objCar = Car('volvo','Four Wheeler','Z1','Grey')
objBike = Bike('Ducati','Two Wheeler','DesertX','Blue&Black')
obj=[objCar,objBike]
person=Person('Anuj',obj)
person.get_info()

# print('-----Details--------')

