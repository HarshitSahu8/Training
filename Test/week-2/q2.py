'''
We need to find manufacturing cost of a box.

There are  5 type of Box.

1. Universal

2. AllFlapMeeting

3. HoneyComb

4. ReverseTuckIn

5. TopOpening SnapLock

Each Box has some basic properties :  length,height,width,area, flute;

A box can either use pins or pasting() to join.

A box can either single part or double part.

there are 7 types of flute : A,B,C,E,F,G and B(B is mostly used).

a flute has gsm and extra gsm;
'''
class Area:
    def area(self):
        return self.length*self.width*self.height

class Flute:
    def __init__(self,type,gsm,extraGsm) -> None:
        self.type=type
        self.GSM=gsm
        self.extraGSM=extraGsm
    

class Box:
    def __init__(self,length,height,width,steching,part,fluteobj):
        self.length=length
        self.height=height
        self.width=width
        self.flute=fluteobj
        self.steching=steching
        self.part=part

class Universal(Box):
    def __init__(self, length, height, width,fluteobj):
        super().__init__(length, height, width, fluteobj)
        self.type='Universal'

class AllFlapMeeting(Box):
    def __init__(self, length, height, width,fluteobj):
        super().__init__(length, height, width, fluteobj)
        self.type='AllFlapMeeting'

class HoneyComb(Box):
    def __init__(self, length, height, width,fluteobj):
        super().__init__(length, height, width, fluteobj)
        self.type='HoneyComb'


class ReverseTuckIn(Box):
    def __init__(self, length, height, width,fluteobj):
        super().__init__(length, height, width, fluteobj)
        self.type='ReverseTuckIn'

class TopOpeningSanapLock(Box):
    def __init__(self, length, height, width,fluteobj):
        super().__init__(length, height, width, fluteobj)
        self.type='TopOpeningSanapLock'

class ExtraGSM:
    def calculate(fluteobj):
        if fluteobj.type=='A':
            return 10
        if fluteobj.type=='B':
            return 30
        if fluteobj.type=='C':
            return 20
        if fluteobj.type=='E':
            return 40
        if fluteobj.type=='F':
            return 50
        if fluteobj.type=='G':
            return 20

class TotalGSM:
    def calculate(fluteobj):
        ExtraGSM.calculate(fluteobj)+fluteobj.GSM*100

class Pasting:
    def cost(typeOfBox):
        if typeOfBox=='Univeesal':
            return 20
        if typeOfBox=='AllFlipMeeting':
            return 30
        if typeOfBox=='HoneyComb':
            return 40
        if typeOfBox=='ReverseTuckIn':
            return 40
        if typeOfBox=='TopOpeningSanpLock':
            return 50

class Pin:
    def calculatePerPinCost(noOfPins):
        return noOfPins*10

class StechingCost:
    def calculate(typeOfBox,noOfPins=0):
        if noOfPins==0:
            return Pasting.cost(typeOfBox)
        else:
            return Pin.calculatePerPinCost(noOfPins)
       

class Cost:
    def calculateBoxCost(boxObj):
        if boxObj.part=='double':
            return Area.area(boxObj)*ExtraGSM.calculate(boxObj.flute)*StechingCost.calculate(boxObj.type)
        else:
            return Area.area(boxObj)*ExtraGSM.calculate(boxObj.flute)
