from .Board import Board
from .LabelList import LabelList

class Project:

    def __init__(self, name="Some Project"):
        self.name = name
        self.boards = []
    def getBoards(self):
        return self.boards
    
    def printBoards(self):
        boardString = ""
        for board in self.boards:
          
            boardString =  boardString +'\n' + '*  '+  board.name
     
        return boardString

    def setBoards(self, boardName, description, ):
        newBoard = Board(boardName, description)
        self.boards.append(newBoard)
        return True    

