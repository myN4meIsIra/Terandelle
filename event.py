# todoItemObject
"""
object that holds info for a todo item
"""


class Event:
    def __init__(self):
        self.priority = None
        self.date = None
        self.description = None
        self.isCompleted = None

    def makeEvent(self, priority, date, description, isCompleted):
        self.priority = priority
        self.date = date
        self.description = description
        self.isCompleted = isCompleted

        return self

    def getEvent(self):
        return self