#class Parent():
#    classmethods and attrs 
#class Child(Parent):
#   classmethods and attrs 


#class Human:
#    height = 170
#class Student(Human):
 #   pass
#class Worker(Human):
 #   pass

#nick = Student()
#ann = Worker()
#print(nick.height)
#print(ann.height)

#class Wow:
 #   def __wow(self):
 #       print("Wow")
  #  def __hello(self):
  #      print("Hello")

#wow = Wow()
#wow.__hello()
#wow.__wow()

#class Class1():
 #   var = 20
 #   def __init__(self):
 #       self.var = 10
        
#class Class2(Class1):
 #   def __init__(self):
 #       print(self.var)
##        super().__init__()
 #       print(self.var)
 #       print(super().var)
#obj = Class2()

class Computer:
    def calculate(self):
        print("I can calculate")
class Display:
    def display(self):
        print("I can show")

class Smarthone(Computer,Display):
    pass

phone = Smarthone()
phone.display()
phone.calculate()
