class Country:
    def __init__(self) -> None:
        self.country_name
        self.area


class City(Country):
    def __init__(self,country_name,area) -> None:
        super().__init__(country_name,area)

    

class Brick:
    def __init__(self) -> None:
        self.color
        self.comment
        self.delecated_person_name   

class Wall(Brick):
    def __init__(self) -> None:

        super().__init__()


class Admin:
    def edit_comment():
        pass

class Map:
    def __init__(self) -> None:
        self.data=dict()
    def add_new_person(self,person_name,personObject):
        self.data[person_name]=personObject
        
class Person:
    def __init__(self,name) -> None:
        self.name=name
        print(self)
        Map.add_new_person(self.name,self)

    def add_comment(self,brick,person,message):
        pass

map=Map()
Anuj=Person('Anuj')