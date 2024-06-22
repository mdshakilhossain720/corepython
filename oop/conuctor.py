
class Mobile:
    def __init__(self):
        print('hello counstruction is called')
realme=Mobile()



class Pepole:
    def __init__(self,m,v=80):
        self.model=m
        self.volume=v

    def show_model(self,p):
        prices=p
        print('Mobile',self.model,'prices',prices)
        print('prices',self.volume)

realm=Pepole('realme')
realm.show_model(5000)



