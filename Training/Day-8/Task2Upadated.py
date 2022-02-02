class User:
    def __init__(self,card,account) -> None:
        self.card=card
        self.account=account

class Account:
    def __init__(self,balance):
        self.balance=balance

    def initialize(self,amount):
        self.balance = amount

    def update_balance(self,amount):
        self.balance += amount


class Card:
  def authenticate(pin):
      # PIN authentication login
      return True

class Cash:
    def __init__(self,total_amount) -> None:
        self.total_amount=total_amount

    def initialize(self,amount):
        self.total_amount = amount

    def valid_amount():
        # Valid amount
        pass

    def invalid_amount():
        # Invalid amount
        pass

class ATM:
    def __init__(self,user,state) -> None:
        self.user=user
        self.state=state
        self.available_cash=100000000
    
    def initialize(self,user):
        self.state = 'ready'
        self.user = user
        
    def read_inserted_card(self,enter_pin,state):
        if state=='ready':
            if Card.authenticate(enter_pin):
                return 'CardValid'
    
    def select_transection(self,transection):
        if transection == 'Deposite':
            denomination=int(input('Enter Denomination:'))
            frequency=int(input('Enter Frequency:'))
            Deposite.topUp(denomination,frequency)
            return
        
        if transection == 'Withdraw':
            amount=int(input('Enter amount:'))
            Withdraw.withdrawMoney(amount)
            return

        if transection == 'Display':
            self.available_cash
            return


class Deposite:
    def topUp(self,denomination,freq):
        for i in range(len(self.denomination)):
            if self.denomination[i]==denomination:
                self.frequency[i]+=freq
                self.cashLimit+=self.denomination[i]*freq
                # print(self.denomination[i],':',self.frequency[i])
                self.cashLimit
                return 
         
class Withdraw:
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

