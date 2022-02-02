class Atm:
    def __init__(self,location) -> None:
        self.balance=0
        self.location=location
        self.notes={100:0,200:0,500:0,2000:0}
    
    def topUp(self,currency,frequency):
        self.notes[currency]+=frequency
        self.balance+=self.notes[currency]*frequency
    
class Withdraw:
    def __init__(self,cardNo):
        self.cardNo=cardNo
    
    def isValid(self,cardNo):
        pass
        
    



