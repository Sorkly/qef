class Task:
    def __init__(self,descrips,deadline,name=""):
       self.name = name
       self.description = descrips
       self.deadline = deadline
       self.task_complited = False
    def task_done (self):
        self.task_complited = True

class Task_manager:
    def __init__(self,group):
        self.group= group
        self.tasks = []
    def add_tasks(self,*args):
        for task in args:
            self.tasks.append(task)
    def del_tasks(self,name):
        for task in self.tasks:
            if task.name == name:
                self.tasks.remove(task)
                print(f"task {name} deleted ")
                return
        print(f" task {name} not found ")
    def task_done(self,name):
        for task in self.tasks:
            if task.name == name:
                task.task_done()
                print(f"task {name} done")
                return
        print(f" task {name} not found ")
            

    def print_task_names(self):
        if self.tasks!= []:
            print(f"Names of {self.group}")
            for task in self.tasks:
                print(task.name)
        else:
            print(f"There are no task in {self.group}")



manager = Task_manager("tasks")
sleep = Task("need sleep to get good dream " , "today", "sleep")
homework = Task("need completed homework" , "12.10.25","homework")
sport = Task("Go to the street and run","13.10.25","sport")
manager.add_tasks(sleep)
manager.add_tasks(homework)
manager.add_tasks(sport)




manager.print_task_names()
manager.task_done("sleep")
manager.del_tasks("sleep")
manager.del_tasks("run")