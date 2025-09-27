class Human:
    def __init__(self,name="Human"):
       self.name = name
class Auto:
    def __init__(self,brand):
        self.brand = brand
        self.passengers = []
    def add_passenger(self,*args):
        for passanger in args:
            self.passengers.append(passanger)
    def print_passengers_names(self):
        if self.passengers!= []:
            print(f"Names of {self.brand} passengers:")
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print(f"There are no passengers in {self.brand}")



bogdan = Human("Bogdan")
vika = Human("Vika")
oleg = Human("Oleg")
car = Auto("Ssang Yong")

car.add_passenger(bogdan,oleg,vika)
#car.add_passenger(bogdan)
#car.add_passenger(vika)
#car.add_passenger(oleg)
car.print_passengers_names()
