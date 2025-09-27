class Human:
    def __init__(self,name="Human"):
       self.name = name
class School_1:
    def __init__(self,group):
        self.group = group
        self.peoples = []
    def add_humans(self,*args):
        for people in args:
            self.peoples.append(people)
    def print_humans_names(self):
        if self.peoples!= []:
            print(f"Names of {self.group}1 human:")
            for passenger in self.peoples:
                print(passenger.name)
        else:
            print(f"There are no humans in {self.group}")
class School_2:
    def __init__(self,group):
        self.group = group
        self.peoples = []
    def add_humans(self,people_s):
            self.peoples.append(people_s)
    def print_humans_names(self):
        if self.peoples!= []:
            print(f"Names of {self.group}2 human:")
            for passenger in self.peoples:
                print(passenger.name)
        else:
            print(f"There are no humans in {self.group}")




bogdan = Human("Bogdan")
vika = Human("Vika")
oleg = Human("Oleg")
maks = Human("Maksim")
oleksiy = Human("Oleksiy")
dasha = Human("Dasha")
schooln1 = School_1("School")
schooln2 = School_2("School")

schooln1.add_humans(bogdan,oleg,vika,maks,oleksiy,dasha)
schooln2.add_humans(maks)
schooln2.add_humans(oleksiy)
schooln2.add_humans(dasha)
schooln1.print_humans_names()
schooln2.print_humans_names()
