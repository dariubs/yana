import os

class Page:
    def __init__(self):
        self.pageName = ""
        self.done = 0

    def add(self, pageName):
        self.pageName = pageName;
        if not os.path.exists("pages"):
            os.makedirs("pages");

        self.page = open("pages/" + self.pageName + ".md", 'w+')

        self.page.close()
        self.done = 1




    def delete(self, pageName):
        self.pageName = pageName;

        if os.path.exists("pages/" + self.pageName + ".md"):
            os.remove("pages/" + self.pageName + ".md");
        else:
            print("This page not exists.");

        self.done = 1