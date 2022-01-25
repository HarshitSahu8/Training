


class Person():
    def __init__(self,name, designation):
        self.name=name
        self.designation=designation
    def get_designation(self):
        return self.designation
    def get_name(self):
        return self.name

class MP(Person):
    def __init__(self,name,designation,constituency,spend,driverName,vehical='Car'):
        super().__init__(name,designation)
        self.constituency=constituency
        self.spend=spend
        self.set_spend_limit()
        self.exceedsSpendingLimit()
        self.driverName=driverName
        self.vehical=vehical
    def set_spend_limit(self):
        if self.designation=='MP':
            self.set_spend_limit=100000
        elif self.designation=='Minister':
            self.set_spend_limit=1000000
        elif self.designation=='PM':
            self.set_spend_limit=10000000

    def getConstituency(self):
        return self.constituency
    def getDriver(self):
        print('Driver Name: ',self.driverName)
        print('Driver Vehical: ',self.vehical)
    def exceedsSpendingLimit(self):
        if self.spend>self.set_spend_limit:
            return True
        

class Ministers(MP):
    def __init__(self, name, designation, constituency, spend, driverName, vehical='Car'):
        super().__init__(name, designation, constituency, spend, driverName, vehical)
        self.designation='Minister'
    def exceedsSpendingLimit(self):
        return super().exceedsSpendingLimit()
        

class PM(Ministers):
    def __init__(self, name, designation, constituency, spend, driverName, vehical='Car'):
        super().__init__(name, designation, constituency, spend, driverName, vehical)
        self.designation='PM'
    def canArrest(self):
        return True


class  Commisioner():
    def __init__(self,obj):
        if obj.designation != 'PM':
            if MP.exceedsSpendingLimit(obj):
                if PM.canArrest(self):
                    print(obj.name,'arrested')
        else:
            print(obj.name,'is safe')
    
obj=MP('JAI','MP','BHOO',200000,'AJAY')
print('Constituency:',obj.getConstituency())
obj.getDriver()
print(obj.exceedsSpendingLimit())
Commisioner(obj)
print('---------------------')
obj2=Ministers('Ankush','Minister','Ne',25000000,'ak')
Commisioner(obj2)