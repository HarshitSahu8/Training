class Person:
    def __init__(self,name) -> None:
        self.name=name
        print(f"{self.name} object Created")

    def get_info(self):
        print(f'person name:{self.name}\n-----------------------------')

class Country:
    def __init__(self,name,area) -> None:
        self.name=name
        self.area=area
        self.city=[]
    
    def add_city(self,city):
        self.city.append(city)
        # print(f'City({self.city[-1].name}) added sucessfuly')
    
    def get_info(self):
        print(f"country name:{self.name}\narea:{self.area}\n-----------------------------")
        City.printCityList(self.city)

class City:
    def __init__(self,name,area) -> None:
        self.name=name
        self.area=area
        self.wall=[]
    
    def add_wall(self,wall):
        self.wall.append(wall)
        # print(f'Wall({self.wall[-1].name}) added sucessfully')
    
    def printCityList(cities):
        for city in range(len(cities)):
            print(f"city name:{cities[city].name}\narea:{cities[city].area}\n-----------------------------")
            # wall:{cities[city].wall}
            Wall.printInfoOfWallList(cities[city].wall)
        return
    
    def get_info(self):
        print(f"city name:{self.name}\narea:{self.area}\nwall:{self.wall}\n-----------------------------")
        return

class Wall:
    def __init__(self,name,owner,brickNo) -> None:
        self.name=name
        self.owner=owner
        if brickNo<=90:
            self.brickNo=brickNo
            self.bricks=["-"]*brickNo
        else:
            print('Bricks must be less than 90')
            return
    
    
    def printInfoOfWallList(wallList):
        for wall in wallList:
            print(f"name of wall:{wall.name}\nOwner Name:{wall.owner}\n-----------------------------")
            for i in range(len(wall.bricks)):
                if wall.bricks[i]=="-":
                    return
                else:
                    print(f'Brick NO.:{i+1}')
                    Brick.get_info(wall.bricks[i])
        return


    def get_wall_info(self):
        print(f"name of wall:{self.name}\nOwner Name:{self.owner}\n-----------------------------")

        #loop for print brick(delicated person name)
        for i in range(len(self.bricks)):
            if self.bricks[i]=="-":
                return
            else:
                print(f'Brick NO.:{i+1}')
                Brick.get_info(self.bricks[i])
                
    
    def add_brick(self,brickobj):
        for brick in range(self.brickNo):
            if self.bricks[brick]=='-':
                self.bricks[brick]=brickobj
                return
        else:
            print('insufficient space')
        




class Brick:
    def __init__(self) -> None:
        self.color=''
        self.message=''
        self.delicated_to=''
    
    def add_color(self,color):
        self.color=color
    
    def add_message(self,message):
        self.message=message
    
    def add_delicated(self,delicated):
        self.delicated=delicated

    
    def get_info(self):
        print(f"Brick color: {self.color}\nDelicated to:{self.delicated.name}\nmessage:{self.message}\n-----------------------------")


harsh=Person('Harsh')
# harsh.get_info()
ind=Country('india',50000000)
# ind.get_info()
knp=City('Kanpur',2000)
# knp.get_info()
eet=Brick()
eet.add_color('saffron')
eet.add_delicated(harsh)
eet.add_message('Awesome')
# eet.get_info()

streetWall=Wall('harsh','harshit',10)
streetWall.add_brick(eet)
# streetWall.get_wall_info()
knp.add_wall(streetWall)
ind.add_city(knp)
ind.get_info()
