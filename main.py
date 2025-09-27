class Student:
    amount_of_students = 0
    def __init__(self,name=None,height=170):
        self.name = name
        self.height = height 
    

    def __bool__(self):
        #return bool(self.name)
        return self.name != None 
    
    def __len__(self):
        return self.height
    
Nick = Student("Nick")
print(Nick.__len__())
print(Nick.__bool__())
print(len(Nick))
print(bool(Nick))