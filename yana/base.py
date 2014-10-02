import os

class BasePost :
    def __init__(self,path="",postfix=""):
        self.path = path
        self.postfix = postfix
        self.done = 0

    #for add file
    def add(self,file_name):
        self.file_name = file_name
        self.check_path();

        self.create_file = open(self.path +'/' + self.file_name + self.postfix, 'w+')
        self.create_file.close()

        self.done = 1

    #remove file
    def remove(self,file_name):
        self.file_name = file_name
        self.is_exists = self.check_file_exists()

        if self.is_exists :
            os.remove(self.path+'/' + self.file_name + self.postfix)

        self.done = 1

    #check file is exists or not
    def check_file_exists(self):
        if os.path.exists(self.path+'/' + self.file_name + self.postfix):
            return 1
        else :
            return 0

    #check path is exists or not.
    def check_path(self):
        if not os.path.exists(self.path):
            os.makedirs(self.path);

class BasePath:
    def __init__(self):
        pass

    def get_path(self):
        #get current directory
        pass

    def make_path(self,directory_type,file_name):
        #make Path using current position, dirctory type (like posts) and file name like(hello.md)
        pass

class BaseFileName:
    def __init__(self,filename):
        self.filename = filename

    def get_filename(self):
        #return filename with complete path
        pass
        
        


