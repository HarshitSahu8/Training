class Atm:
    def __init__(self) -> None:
        self.denomination=[100,200,500,2000]
        self.frequency=[0,0,0,0]
        self.cashLimit=0

    def topUp(self,denomination,freq):
        for i in range(len(self.denomination)):
            if self.denomination[i]==denomination:
                self.frequency[i]+=freq
                self.cashLimit+=self.denomination[i]*freq
                # print(self.denomination[i],':',self.frequency[i])
                self.cashLimit
                return  

    def withdrawMoney(self,amount):
        amt=amount
        balance=0
        dispatchFrequency=[0]*len(self.denomination)
        if self.cashLimit>=amount:
            for i in range(len(self.denomination)-1,-1,-1):
                if self.frequency[i]>0:
                    dispatchFrequency[i]=amount//self.denomination[i]
                    # print(self.denomination[i],':',amount//self.denomination[i])
                    self.frequency[i]-=(amount//self.denomination[i])
                    amount%=self.denomination[i]
                    balance+=self.denomination[i]*dispatchFrequency[i]
                    # print('balance:',balance,' amount:',amount,'cash: ',self.cashLimit)
            if balance == amt:
                for i in range(len(self.denomination)):
                    print(self.denomination[i],':',dispatchFrequency[i])
                self.cashLimit-=balance
                print(self.cashLimit)
            else:
                print('balance Error')
                return
        else:
            print('insufficient balance')
        return
    
    def demonitization(self,banned,newCurrency,frequency):
        for i in range(len(self.denomination)):
            if self.denomination[i]==banned:
                print(self.cashLimit)
                self.cashLimit-=self.denomination[i]*self.frequency[i]
                self.denomination[i]=newCurrency
                self.frequency[i]=frequency
                self.cashLimit+=newCurrency*frequency
                print(self.cashLimit)
                return

            

obj=Atm()
obj.topUp(2000,4)
obj.topUp(500,4)
obj.topUp(200,4)
obj.topUp(100,4)
obj.withdrawMoney(3300)
# obj.demonitization(2000,5000,10)
