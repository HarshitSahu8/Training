from abc import ABC,abstractclassmethod

class User:
    def __init__(self,name,id,phoneNumber,contact,chat,status,add_contact):
        self.name=name
        self.id=id
        self.phoneNumber=phoneNumber
        self.contact=[]
        self.chat=chat
        self.chat={contact:chat}
        self.add_contact=add_contact
        self.status=status

class Contact:
    def __init__(self,id,list,name,number,image,about):
        self.id=id
        self.list=list
        self.name=name
        self.number=number
        self.image=image
        self.about=about

class Chat:
    def __init__(self,id,status,message) -> None:
        self.id=id
        self.status_id=status
        self.message=message

class Message(ABC):
    @abstractclassmethod
    def send(self):
        pass

class Text(Message):
    def send(self):
        return super().send()

class Vedio(Message):
    def send(self):
        return super().send()

class Image(Message):
    def send(self):
        return super().send()

class Document(Message):
    def send(self):
        return super().send()

class Status:
    def __init__(self,time):
        self.time=time

    def postStatus():
        pass

    def viewStatus():
        pass

    def isActive():
        pass

class Group:
    def __init__(self,id, contact):
        self.id=id
        self.contactList=contact

class Setting:
    def accountSetting():
        pass
    def chatSetting():
        pass
    def notificationSetting():
        pass
