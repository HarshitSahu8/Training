class Inverter:
    def __init__(self,current, voltage):
        self.current=current
        self.voltage=voltage
        self.battery=False
        self.grid=False

    def powerRating(self, current, voltage):
        return current*voltage


class SolarInverter(Inverter):
    def __init__(self, current, voltage,panels):
        super().__init__(current, voltage)
        self.panels=panels


    def rating():
        return super().powerRating(self.current,self.voltage)
    
    def hasBattery(self,battery):
        self.battery=battery
    
    def isGridOn(self,grid):
        self.grid=grid

class NonSolarInverter(Inverter):
    def __init__(self, current, voltage):
        super().__init__(current, voltage)

    def getRating(self):
        return Inverter.powerRating(self,self.current,self.voltage) 

    
