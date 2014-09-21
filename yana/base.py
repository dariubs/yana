import os

class BasePost :
    def __init__(self,file_name="",path="",prefix=""):
        self.file_name = file_name
        self.path = path
        self.prefix = prefix
        self.done = 0

    #for add file
    def add(self):
        pass

    #remove file
    def remove(self):
        pass

    #check if exists
    def isExists(self):
        pass

