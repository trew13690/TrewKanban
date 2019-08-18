from .Task import Task


class LabelList:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def addTasks(self, tasks:[], label):
        #  sort tasks by label and store in list
        for task in tasks:
            if(task.label.name == label):
                self.tasks.append(task)
        
        return self.printTasks()

    def printTasks(self) -> str:
        return [task.name for task in self.tasks]