class Whatsapp:
    def __init__(self,name,contact):
        self.name=name
        self.contact=contact
        self.data=['']*100

class Media:
    def sendText(sender,txt,receiver):
        leng=len(receiver.data)
        if receiver in sender.contact:
            for i in range(len(receiver.data)):
                if receiver.data[i]=='':
                    receiver.data[i]=txt
                    return
    def sendVideo(self,sender,videoName,receiver):
        pass
    def sendImage(self,sender,ImageName,receiver):
        pass


objAnuj=Whatsapp('Anuj',{})
objIsfaq=Whatsapp('Isfaq',{'Anuj':objAnuj})
Media.sendText(objIsfaq,'hey hello','Anuj')
print(objAnuj.txt)




