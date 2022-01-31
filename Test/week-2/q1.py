'''
Method/Constructor    Description

public VegetableBill(Employee clerk)    constructs a VegetableBill object for the given clerk

public void add(Item i)    adds i to this bill's total

public double getTotal()    returns the cost of these items

public void printReceipt()    prints a list of items

VegetableBill objects interact with Item objects. An Item has the following public methods:

Method/Constructor    Description

public double getPrice()    returns the price for this item

public double getDiscount()    returns the discount for this item

For example, Onion item might cost 1.35 with a discount of 0.25 for preferred customers, 
meaning that preferred customers get it for 1.10. 

(Some items will have no discount, 0.0.) Currently the above classes do not consider discounts. 
Every item in a bill is charged full price, and item discounts
are ignored.

Define a class DiscountBill that extends VegetableBill to compute discounts for preferred customers. 
The constructor for DiscountBill accepts a parameter for

whether the customer should get the discount.

Your class should adjust the amount reported by getTotal for preferred customers. 
For example, if the total would have been $80 but a preferred customer is getting $20 in discounts, 
then getTotal should report the total as $60 for that customer. 
You should also keep track of how many items a customer is getting a non-zero 
discount for and the overall discount, both as a total amount and as a percentage of 
the original bill. Include the extra methods below that allow a client to ask about the discount:

Method/Constructor    Description

public DiscountBill(Employee clerk, boolean preferred)    constructs bill for given clerk

public int getDiscountCount()    returns the number of items that were discounted, if any

public double getDiscountAmount()    returns the total discount for this list of items, if any

public double getDiscountPercent()    returns the percent of the total discount as a percent
 of what the total would have been otherwise

If the customer is not a preferred customer the DiscountBill behaves at all times 
as if there is a total discount of 0.0 and no items have been discounted.
'''
class Employee:
    def __init__(self,name,position) -> None:
        self.name=name
        self.position=position

class Item:
    def __init__(self) -> None:
        self.itemMenu=dict()
        self.count=0
    def addItem(self,itemName,itemPrice):
        self.itemMenu[itemName]=itemPrice
        self.count+=1
    def getPrice(self,item):
        return self.itemMenu[item]

class VegetableBill():
    def __init__(self,emp) -> None:
        self.billList=dict()
        self.totalAmount=0
        self.emp=emp

    def add(self,item,quantity,itemobj):
        self.totalAmount+=itemobj.getPrice(item)
        self.billList[item]=(itemobj.getPrice(item)*quantity)
        return
        
    def getTotal(self):
        return self.totalAmount

    def PrintReceipt(self):
        for itm in self.billList:
            print(itm,':',self.billList[itm])

    def getPrice(self,item):
        return Item.getPrice(item)
           
class DiscountBill:
    def __init__(self,preferred=False) -> None:
        self.preferred=preferred
        self.discountStatus=False
        self.totalDiscount=0
        self.count=0

    def getDiscountCountitem(self,billList,item,discount):
        self.totalDiscount+=billList[item]*discount
        billList[item]-=billList[item]*discount
        self.discountStatus=True
        self.count+=1
        return

    def getTotal(self,billList):
        self.totalCost=0
        for i in billList:
            self.totalCost+=billList[i]
        return self.totalCost
    
    def getDiscountPercentage(self,veg):
        return (self.totalCost/veg.totalAmount)*100

objEmp=Employee('Anuj','cleck')
objVeg=VegetableBill(objEmp)
itemobj=Item()
itemobj.addItem('chukandar','200')
print(itemobj.getPrice('chukandar'))
# objVeg.add('chukandar',5,itemobj)
# print(objVeg.getTotal(objVeg.billList))


        
        

    



