class Animal:
    def print(self):
        print("Я тварина")
    def __init__(self,name,age,why_animal):
        self.name = name
        self.age = age
        self.why_animal = why_animal
    def info(self):
        print(f"Ім'я: {self.name}, вік: {self.age} роки(-ів), я {self.why_animal}")
    def eat(self):
        print(f"зараз {self.name} їсть")
    def sleep(self):
        print(f"зараз {self.name} не спить")
        


class Cat(Animal):
    def make_sound(self):
        print(f" {self.name} Мяу")

class Dog(Animal):
     def make_sound(self):
        print(f" {self.name} Гав-гав")

class Rabbit(Animal):
     pass

cat = Cat("Richi",1,"Кіт")
dog = Dog("Loily",3,"Собака")
rabbit = Rabbit("Rally", 7 ,"Кролик" )

dog.info()
dog.eat()
dog.make_sound()

cat.info()
cat.sleep()
cat.make_sound()

rabbit.info()
rabbit.sleep()
rabbit.eat()