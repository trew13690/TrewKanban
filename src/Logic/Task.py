


class Task:

    def __init__(self,name: str,description: str, owner: str, points: int, board, milestone: str, epic: str, labels: [], project,  *args, **kwargs):
        self.name = name
        self.description = description
        self.owner = owner
        self.points = points
        self.board = board
        self.milestone = milestone
        self.epic = epic
        self.labels = labels
        self.project = project

    