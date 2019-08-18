from .LabelList import LabelList
from .Label import Label
class Board:

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.labelList = []
        self.swimLanes =[]
        self.labels = []
   
    def createLabelList(self, newLabelList):
        self.labelList.append(LabelList(newLabelList))
        return True

    def createLabels(self ):
        action = 'y'
        listOfLabels = []
        if(self.labels is not True):
            while(action == 'y'):
                print('\nCreating new Labels:\n\n')
                newLabelName = input("Enter new name for label\n\t")
                newLabelScope = input("Enter the scope of labal\n\t")
                newLabel = Label(newLabelName, "", newLabelScope)
                listOfLabels.append(newLabel)
                newAction = input("Do you wish to add anoter Label; Y/N\n")
                if(newAction == 'n'):
                    action = 'n'
        self.labels = listOfLabels
        return True;





