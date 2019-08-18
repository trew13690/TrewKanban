from Logic.Project import Project
from Logic.Task import Task

class Headless:


    def __init__(self):
        self.title= "Headless App - TrewKanban"
        self.project = ""
        self.boards = []
        self.data = False
        self.q = False
        self.action = "d"




    def run(self):
        print("Welcome to the Headless version of TrewKanban\n")
        print("Please wait as we load the data!\n")
        if (self.data == True):
            self.loadData()
        else:
            pass



    def loadData(self):
        print("...."+ self.project.name)
        print("...."+ self.boards.printBoards)
        print("...."+ self.tasks.printTasks)
        print("...." + self.labels.printLabels)


    def createNewProject(self):
        print("Creating a new Project:\n")
        projectName = input("What is the project name?\n")
        boardName = input("What is the name of the first board?\n")
        
        self.project = Project(name=projectName)
        self.project.setBoards(boardName=boardName, description="")
    
    def app(self):
        self.boards = self.project.boards

        while(self.q != True):

            if self.action == "d":
                for i in range(0,3):
                    print('\n')
                    print('=' * 25)
                
                print("\n\nProject Name is " , self.project.name)
                print("\n\nProject Boards:", self.project.printBoards())
                self.action=""


            if self.action == 'b':
                self.displayBoard()
                self.action = ""

            else:
                print('\n\nSelect an action from the list:\n\n')
                print('To Quit - q')
                print('To Display Summary - d')
                print('To Select a Board: - b')
                newAction = input("New Action: ")


                if newAction == 'q':
                    self.q = True
                self.action = newAction

    def displayBoard(self):
       
            print("\nPrinting List of Boards:\n\n")
            for i in range(0, len(self.boards)):
                print(i, ' -  ', self.boards[i].name)
            selectedBoardIndex = input('\nSelect Board:\n\n')
            selectedBoard = self.boards[int(selectedBoardIndex)]
            mq = False
            if(selectedBoard != None):
                while(mq != True):
                    self.printLineBreak()
                    print("\n\n\n\nDisplaying Board:", selectedBoard.name)

                    
                    print("\n\n", selectedBoard.description)
            
                    self.printBoardDetails(selectedBoard)
                    print("\n\n\n\tBoard Actions:\n")
                    print("\tExit out of Board View - q")
                    print("\tSelect Another Board - 1")
                    print("\tDisplay Tasks in List View - 2")
                    print("\tCreate a New Task- 3 ")
                    print("\tMove a Task- 4")
                    print("\tDelete a Task- 5")
                    boardChoice = input("\n\tChoice an action\n\t")


                    if(boardChoice == '3'):
                        self.createNewTask(selectedBoard)
                    if(boardChoice == 'q'):
                        mq = True
                
    def createNewTask(self, selectedBoard):
        print('\n\nCreating new Task\n')
        self.printLineBreak()
        print("Checking if there are label on this board...")
        if(selectedBoard.labelList is not True):
            print("There are no labels\nWe must create at least one label before making tasks\n")

            selectedBoard.createLabels()
        action = 'n'
        taskList = []
        while(action == 'n'):
            print('\n\nTask Creation:\n')
            taskName = input("\tPlease enter the task name\n\t")
            taskDescription = input("\tPlease enter the description of the task\n\t")
            taskOwner = input("\tPlease enter the owner of this task\n\t")
            taskPoints = input("\tPlease enter the estimated story points of this task\n\t")
            taskBoard =     selectedBoard
            taskMilestone = input("\tPlease enter the milestone of this task\n\t")
            taskEpic = input("\tPlease enter the epic for this task\n\t")
            taskProject = self.project
            taskLabels = []
            for label in selectedBoard.labels:
                print("\tPlease say y or n per label to assign to task\n\t")
                print('\n\t\t',label.name,'\n\t')
                answer = input('y/n:\t')
                if(answer == 'y'):
                    taskLabels.append(label)
            print('\n', 'Checking task details','\n\t')
            self.printLineBreak()
            print('\t',taskName,'\t', taskDescription, '\t', taskOwner,
            '\n\t', taskPoints, '\t', taskBoard.name, '\t', taskMilestone,'\n', 
            taskEpic, '\t', taskProject.name, '\t')
            print('\t\t', 'Labels:')
            [print(label.name) for label in taskLabels]
            newAction = input("Is this correct? y/n")
            if(newAction == 'y'):
                action = 'y'
                taskList.append(Task(taskName, taskDescription, taskOwner, taskPoints, taskBoard, taskMilestone, taskEpic, taskLabels, taskProject))
                newTask = input('Do you wish to add another task? y/n')
                if(newTask == 'y'):
                    action = 'n'
        for task in taskList:
            selectedBoard.labelList[0].tasks.append(task)
        

            
    def printBoardDetails(self, selectedBoard):
        if(len(selectedBoard.labelList) == 0):
            selectedBoard.createLabelList('To-do')
            selectedBoard.createLabelList('Doing')
            selectedBoard.createLabelList('Done')
        print('\n\n')
        
        labelListString = [labelList.name for labelList in selectedBoard.labelList]

        labelListString = "\t\t\t\t".join(labelListString)
        
        print("\t\t",labelListString,"\t\t\n")
        self.printLineBreak()
        self.printCol(selectedBoard)

    def printCol(self, selectedBoard):
        for i in range(len(selectedBoard.labelList)):
            for j in range(len(selectedBoard.labelList[i].tasks)):
                print('\n\t\t', selectedBoard.labelList[i].tasks[j].name)
                print('\n\t\t', selectedBoard.labelList[i].tasks[j].owner)
        return True
    def printLineBreak(self):
        for i in range(0,2):
            print('='*95)
        



